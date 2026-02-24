/* Clean Dual-Theme UI + Success Check + Full History */
console.log("UI Loaded");

const API_BASE = "http://127.0.0.1:8000";
const API_PRED = `${API_BASE}/api/predict`;

document.addEventListener("DOMContentLoaded", () => {

  const predictBtn = document.getElementById("predictBtn");
  const clearBtn = document.getElementById("clearBtn");
  const exportBtn = document.getElementById("exportBtn");
  const clearHistoryBtn = document.getElementById("clearHistoryBtn");
  const errEl = document.getElementById("err");
  const resultCard = document.getElementById("resultCard");
  const successCheck = document.getElementById("successCheck");
  const themeToggle = document.getElementById("themeToggle");

  // Show API URL
  document.getElementById("apiUrlDisplay").innerText = API_PRED;

  /* Restore theme from localStorage */
  const savedTheme = localStorage.getItem("theme") || "light";
  if (savedTheme === "dark") {
    document.body.classList.add("dark-theme");
    themeToggle.checked = true;
  }

  /* Toggle Theme */
  themeToggle.addEventListener("change", () => {
    if (themeToggle.checked) {
      document.body.classList.add("dark-theme");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark-theme");
      localStorage.setItem("theme", "light");
    }
  });

  function showError(msg) {
    errEl.hidden = !msg;
    errEl.innerText = msg || "";
  }

  /* Add a row to the history table */
  function addHistory(pred, energy, temp, hum) {
    const tbody = document.getElementById("historyTableBody");
    const tr = document.createElement("tr");

    const timestamp = new Date().toLocaleString();

    tr.innerHTML = `
      <td>${timestamp}</td>
      <td>${energy.toFixed(2)}</td>
      <td>${temp.toFixed(2)}</td>
      <td>${hum.toFixed(2)}</td>
      <td>${pred.toFixed(2)}</td>
    `;

    tbody.prepend(tr);
  }

  /* Clear history */
  clearHistoryBtn.addEventListener("click", () => {
    document.getElementById("historyTableBody").innerHTML = "";
  });

  /* Export CSV */
  exportBtn.addEventListener("click", () => {
    const rows = [["timestamp", "energy", "temp", "humidity", "predicted"]];

    document.querySelectorAll("#historyTableBody tr").forEach(tr => {
      const row = [...tr.children].map(td => td.innerText);
      rows.push(row);
    });

    const csv = rows.map(r => r.join(",")).join("\n");
    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "energy_history.csv";
    a.click();

    URL.revokeObjectURL(url);
  });

  /* Clear all input fields */
  clearBtn.addEventListener("click", () => {
    ["current_energy", "temp", "hum", "ts"].forEach(id => {
      document.getElementById(id).value = "";
    });
    showError("");
  });

  /* Predict Energy */
  predictBtn.addEventListener("click", async () => {
    showError("");

    const energy = parseFloat(document.getElementById("current_energy").value);
    const temp = parseFloat(document.getElementById("temp").value);
    const hum = parseFloat(document.getElementById("hum").value);
    const tsVal = document.getElementById("ts").value;

    if (isNaN(energy)) return showError("Enter energy usage.");
    if (isNaN(temp)) return showError("Enter temperature.");
    if (isNaN(hum)) return showError("Enter humidity.");

    const payload = {
      current_energy_usage: energy,
      temperature_C: temp,
      humidity_pct: hum
    };

    if (tsVal) payload.timestamp = tsVal;

    try {
      const res = await fetch(API_PRED, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) throw new Error("Prediction failed");

      const data = await res.json();
      const pred = Number(data.predicted_energy_next_hour);

      document.getElementById("predictionValue").innerText = pred.toFixed(2);
      document.getElementById("metaInfo").innerText = data.timestamp || tsVal || "--";
      document.getElementById("modelName").innerText = data.model_used || "xgboost";

      resultCard.hidden = false;

      /* Success check animation */
      successCheck.hidden = false;
      successCheck.classList.remove("hide");

      setTimeout(() => {
        successCheck.classList.add("hide");
        setTimeout(() => { successCheck.hidden = true; }, 350);
      }, 1500);

      /* Add to history */
      addHistory(pred, energy, temp, hum);

    } catch (err) {
      console.error(err);
      showError("Prediction failed.");
    }
  });

});