import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path
import joblib

# Serve frontend from the same directory as this file (safer and simpler)
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR  / "frontend"
MODELS_DIR = BASE_DIR / "models"

# print("BASE_DIR:", BASE_DIR)
# print("FRONTEND_DIR:", FRONTEND_DIR)
# print("MODELS_DIR:", MODELS_DIR)

app = Flask(__name__, static_folder=str(FRONTEND_DIR))
CORS(app)

# LOAD MODEL (guarded)
try:
    MODEL = joblib.load(MODELS_DIR / "best_model.pkl")
    MODEL_TYPE = "xgboost"
    # # If it's XGBoost scikit wrapper
    # try:
    #     print("\nMODEL FEATURES:")
    #     print(MODEL.get_booster().feature_names, "\n")
    # except Exception:
    #     pass
except Exception as e:
    print("Warning: could not load model:", e)
    MODEL = None
    MODEL_TYPE = "unknown"

XGB_FEATURES = [
    "hour", "dayofweek", "is_weekend", "month", "dayofyear",
    "hour_sin", "hour_cos", "dow_sin", "dow_cos",
    "month_sin", "month_cos",
    "temperature_C", "humidity_pct",
    "temp_change", "humidity_change",
    "lag_1", "lag_6", "lag_12", "lag_24", "lag_48", "lag_72",
    "rolling_6h", "rolling_12h", "rolling_24h", "rolling_7d",
    "rolling_24h_std", "rolling_7d_std"
]

history = []

def build_features(current_usage, temp, hum, ts):
    global history
    history.append(current_usage)
    if len(history) > 300:
        history = history[-300:]

    hour = ts.hour
    dow = ts.dayofweek
    month = ts.month
    dayofyear = ts.dayofyear

    f = {
        "hour": hour,
        "dayofweek": dow,
        "is_weekend": 1 if dow >= 5 else 0,
        "month": month,
        "dayofyear": dayofyear,
        "hour_sin": np.sin(2 * np.pi * hour / 24),
        "hour_cos": np.cos(2 * np.pi * hour / 24),
        "dow_sin": np.sin(2 * np.pi * dow / 7),
        "dow_cos": np.cos(2 * np.pi * dow / 7),
        "month_sin": np.sin(2 * np.pi * month / 12),
        "month_cos": np.cos(2 * np.pi * month / 12),
        "temperature_C": temp,
        "humidity_pct": hum,
        "temp_change": 0.0,
        "humidity_change": 0.0
    }

    def lag(L):
        return history[-L] if len(history) >= L else (history[0] if history else 0.0)

    for L in [1, 6, 12, 24, 48, 72]:
        f[f"lag_{L}"] = lag(L)

    def roll_mean(w):
        return float(np.mean(history[-w:])) if len(history) >= 1 else 0.0

    def roll_std(w):
        return float(np.std(history[-w:])) if len(history) >= 1 else 0.0

    f["rolling_6h"] = roll_mean(6)
    f["rolling_12h"] = roll_mean(12)
    f["rolling_24h"] = roll_mean(24)
    f["rolling_7d"] = roll_mean(24 * 7)
    f["rolling_24h_std"] = roll_std(24)
    f["rolling_7d_std"] = roll_std(24 * 7)

    df = pd.DataFrame([[f.get(col, 0.0) for col in XGB_FEATURES]], columns=XGB_FEATURES)
    return df

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route("/api/predict", methods=["POST"])
def predict_api():
    if MODEL is None:
        return jsonify({"error": "Model not loaded on server"}), 500
    data = request.json
    try:
        ts = pd.to_datetime(data.get("timestamp")) if data.get("timestamp") else pd.Timestamp.now().floor("h")
    except:
        return jsonify({"error": "Invalid timestamp"}), 400

    try:
        X = build_features(
            data["current_energy_usage"],
            data["temperature_C"],
            data["humidity_pct"],
            ts
        )
    except Exception as e:
        return jsonify({"error": f"Invalid payload or missing fields: {e}"}), 400

    pred = MODEL.predict(X)[0]
    pred = round(float(pred), 2)

    return jsonify({
        "predicted_energy_next_hour": pred,
        "model_used": MODEL_TYPE,
        "timestamp": str(ts)
    })

@app.route("/api/predict/24h", methods=["POST"])
def forecast_24h():
    if MODEL is None:
        return jsonify({"error": "Model not loaded on server"}), 500
    data = request.json
    try:
        temp = data["temperature_C"]
        hum = data["humidity_pct"]
        curr = data["current_energy_usage"]
    except KeyError:
        return jsonify({"error": "Missing fields in request"}), 400

    ts = pd.Timestamp.now().floor("h")
    results = []
    current_val = curr

    for _ in range(24):
        ts = ts + pd.Timedelta(hours=1)
        X = build_features(current_val, temp, hum, ts)
        current_val = MODEL.predict(X)[0]
        results.append(round(float(current_val), 2))

    return jsonify({"forecast_24h": results})

@app.route("/api/predict/multistep", methods=["POST"])
def multistep():
    if MODEL is None:
        return jsonify({"error": "Model not loaded on server"}), 500
    data = request.json
    try:
        temp = data["temperature_C"]
        hum = data["humidity_pct"]
        curr = data["current_energy_usage"]
    except KeyError:
        return jsonify({"error": "Missing fields in request"}), 400

    ts = pd.Timestamp.now().floor("h")
    steps = [3, 6, 12, 24]
    outputs = {}

    for step in steps:
        local_val = curr
        ts_local = ts
        for _ in range(step):
            ts_local = ts_local + pd.Timedelta(hours=1)
            X = build_features(local_val, temp, hum, ts_local)
            local_val = MODEL.predict(X)[0]
        outputs[f"{step}h"] = round(float(local_val), 2)

    return jsonify(outputs)

@app.route("/api/health")
def health():
    return jsonify({"status": "running", "model": MODEL_TYPE})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)