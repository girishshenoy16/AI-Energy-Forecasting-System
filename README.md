# ⚡ AI-Powered Energy Forecasting & Consumption Intelligence Platform

An end-to-end AI-powered energy intelligence system designed to forecast future energy consumption using machine learning, API engineering, and a modern responsive frontend.

The platform combines:
- 🧠 Machine Learning Forecasting
- 🌐 Flask API Backend
- 💻 Interactive Frontend UI
- ☁️ Cloud Deployment Architecture
- 📊 Feature Engineering Pipelines
- 📁 Structured AI Project Architecture

This system predicts next-hour energy usage (kWh) while simulating real-world smart energy forecasting workflows used in intelligent infrastructure and sustainability analytics systems.

---

# 🏷️ Badges

![Stars](https://img.shields.io/github/stars/girishshenoy16/ai-energy-forecast?style=flat-square&color=blue)

![Forks](https://img.shields.io/github/forks/girishshen/ai-energy-forecast?style=flat-square)

![Python](https://img.shields.io/badge/Python-3.10-blue)

![Flask](https://img.shields.io/badge/Made%20with-Flask-black?style=flat&logo=flask)

![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)

![Testing](https://img.shields.io/badge/Tests-PyTest-yellow)

![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

![License](https://img.shields.io/badge/License-MIT-green)

![Render](https://img.shields.io/badge/Backend-Render-blue)

![Netlify](https://img.shields.io/badge/Frontend-Netlify-brightgreen)

![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)

---

<p align="center">
  <b>⚡ AI-Powered Smart Energy Forecasting • Flask API • Full-Stack AI Engineering • Cloud Deployment</b>
</p>

---

# 📌 Project Overview

Modern energy systems require intelligent forecasting solutions to optimize energy usage, infrastructure efficiency, and operational planning.

Unexpected demand spikes can lead to:
- energy inefficiencies
- infrastructure overload
- operational cost escalation
- sustainability challenges
- poor energy utilization

This project builds a complete AI-powered forecasting platform capable of:

✅ Forecasting future energy consumption  
✅ Providing intelligent energy insights  
✅ Serving predictions through APIs  
✅ Delivering responsive UI workflows  
✅ Supporting smart energy analytics  
✅ Simulating enterprise energy intelligence systems

---

# 🌐 Deployment Architecture

This project is deployed using a modern full-stack AI deployment workflow.

| Component                  | Platform                  |
|----------------------------|---------------------------|
| Frontend UI                | Netlify                   |
| Flask API Backend          | Render                    |
| Machine Learning Inference | Python + Flask            |
| Deployment Workflow        | Frontend ↔ API ↔ ML Model |

This architecture simulates production-style AI deployment workflows commonly used in AI-powered web systems.

---

# 🔗 Live Deployment

## 🌍 Frontend Application (Netlify)

```plaintext
https://ai-energy-forecasting-system.netlify.app/
```

---

## ⚙️ Backend API (Render)

```plaintext
https://ai-energy-forecasting-system.onrender.com
```

---

# 🌍 Smart Energy Intelligence

This project simulates AI-powered smart energy forecasting workflows used in:

- smart grid analytics
- industrial energy monitoring
- utility consumption forecasting
- sustainability analytics
- operational energy optimization
- intelligent infrastructure systems

The platform combines machine learning forecasting, API engineering, and frontend systems to deliver real-time energy intelligence workflows.

---

# 🚀 Core Features

---

## 🧠 Machine Learning Forecasting

Models implemented:
- XGBoost
- MLP Neural Network
- LSTM Neural Network

Capabilities:
- next-hour energy forecasting
- feature-engineered predictions
- intelligent energy analytics
- comparative ML experimentation

The best-performing model is automatically saved as:

```plaintext
best_model.pkl
```

---

## 🌐 Flask API Backend

REST API backend for serving energy forecasts.

### Backend Features
- `/api/predict` endpoint
- timestamp handling
- JSON response support
- model inference pipeline
- backend validation handling

---

## 💻 Responsive Frontend UI

Modern responsive frontend built using:
- HTML
- CSS
- JavaScript

### Frontend Features
- dark/light mode
- centered dashboard layout
- prediction visualization
- smooth interactions
- responsive design
- prediction history

---

## 🗃️ Prediction History System

The application supports:
- prediction history storage
- CSV export
- session tracking
- history clearing

This creates a more realistic AI product workflow.

---

## 📊 Data Engineering Pipeline

Pipeline flow:

```plaintext
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Prediction API
   ↓
Frontend Visualization
```

---

# 🏗️ End-to-End AI System Architecture

```text
Frontend UI
     ↓
Flask API Backend
     ↓
Feature Engineering Pipeline
     ↓
Machine Learning Models
     ↓
Energy Consumption Forecast
     ↓
Prediction History & Export System
```

---

# 📸 Application Screenshots

## 🌞 Light Mode UI

![Light Mode](screenshots/light_mode.png)

---

## 🌙 Dark Mode UI

![Dark Mode](screenshots/dark_mode.png)

---

## 📈 Energy Forecast Prediction

![Prediction Output](screenshots/output.png)

---

# 🛠️ Tech Stack

| Category         | Technologies          |
|------------------|-----------------------|
| Programming      | Python                |
| Backend          | Flask                 |
| Frontend         | HTML, CSS, JavaScript |
| Machine Learning | XGBoost, MLP, LSTM    |
| Deep Learning    | TensorFlow / Keras    |
| Data Processing  | Pandas, NumPy         |
| Testing          | PyTest                |
| Deployment       | Render, Netlify       |

---

# 📊 Dataset & Feature Engineering

The project uses energy consumption telemetry data for forecasting future energy usage patterns.

### Feature Engineering Includes
- timestamp decomposition
- rolling averages
- temporal features
- environmental variables
- normalized energy metrics

### Forecasting Objectives
- next-hour consumption prediction
- demand trend forecasting
- intelligent energy analytics
- operational energy planning

---

# 📂 Project Structure

```plaintext
ENERGY-FORECASTING/
│── app/
│   └── energy_app.py
│
│── data/
│   ├── features/
│   │   ├── features_LSTM.csv
│   │   ├── features_MLP.csv
│   │   └── features_XGBOOST.csv
│   │
│   ├── processed/
│   │   ├── cleaned_energy_data.csv
│   │   └── feature_engineered_energy_data.csv
│   │
│   └── raw/
│       └── energy_data.csv
│
│── frontend/
│   ├── index.html
│   ├── style.css
│   └── control.js
│
│── models/
│   └── best_model.pkl
│
│── notebooks/
│   ├── 01. EDA.ipynb
│   ├── 02. Feature Engineering.ipynb
│   └── 03. Modelling.ipynb
│
│── screenshots/
│   ├── dark_mode.png
│   ├── light_mode.png
│   └── output.png
│
│── tests/
│   └── test_api.py
│
│── requirements.txt
└── README.md
```

---

# 🧪 Testing & Validation

The project includes automated API validation tests using PyTest.

### Testing Coverage
- API endpoint validation
- prediction response testing
- input handling validation
- timestamp processing
- backend response integrity
- forecasting workflow verification

---

# 🚀 Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/girishshenoy16/AI-Energy-Forecasting-System.git

cd AI-Energy-Forecasting-System
```

---

## 2️⃣ Create Python Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Upgrade pip

```bash
pip install --upgrade pip
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Jupyter Notebooks

Open and run the notebooks in order:

1. `01.EDA.ipynb`
2. `02.Feature_Engineering.ipynb`
3. `03. Modelling.ipynb`

---

## ⚙️ Run the AI Forecasting System

Execute notebooks and preprocessing workflows for:
- data cleaning
- feature engineering
- model training
- forecasting optimization

Then start the backend API.

---

## 6️⃣ Run Flask Backend

```bash
python app/energy_app.py
```

Server starts at:

```plaintext
http://127.0.0.1:8000
```

---

## 7️⃣ Launch Frontend UI

Open:

```plaintext
frontend/index.html
```

The frontend automatically communicates with the Flask API backend.

---

# 📡 API Usage

## POST `/api/predict`

### Sample Request

```json
{
  "current_energy": 320,
  "temperature": 28,
  "humidity": 60,
  "timestamp": "2025-11-19 14:00"
}
```

---

### Sample Response

```json
{
  "prediction": 333.15,
  "timestamp_used": "2025-11-19 14:00",
  "model": "xgboost"
}
```

---

# 🎯 Business Impact

This platform demonstrates how AI forecasting systems can help organizations:

- optimize energy consumption
- improve operational planning
- support sustainability initiatives
- forecast utility demand
- reduce energy inefficiencies
- improve infrastructure monitoring
- enable intelligent energy analytics

---

# 📈 Future Improvements

- deploy backend on cloud infrastructure
- real-time forecasting dashboards
- live chart visualizations
- compare multiple ML models dynamically
- user authentication system
- batch forecasting workflows
- smart grid integration
- energy anomaly detection

---

# 📚 Learning Outcomes

This project demonstrates practical experience in:

- full-stack AI engineering
- machine learning deployment
- Flask API development
- frontend integration
- cloud deployment workflows
- energy forecasting systems
- ML experimentation
- responsive UI engineering
- production-style AI architecture

---

# 👨‍💻 Author

Girish Shenoy

AI • Machine Learning • Full-Stack AI Systems • Forecasting Analytics • Intelligent Infrastructure

---

# ⭐ If You Found This Project Useful

Please consider giving this repository a ⭐ on GitHub.