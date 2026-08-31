import joblib
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

model = joblib.load(MODEL_PATH)
import pandas as pd
from datetime import datetime

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="EdgeSense AI",
    page_icon="🏭",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------
st.title("🏭 EdgeSense AI")
st.subheader("Real-Time Predictive Maintenance Dashboard")
st.caption("Edge AI-based Industrial Machinery Health Monitoring System")
st.write(f"🕒 Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
st.divider()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("⚙️ System Information")

st.sidebar.success("🟢 System Online")

st.sidebar.markdown("---")

st.sidebar.write("### Machine")
st.sidebar.info("Motor-01")

st.sidebar.write("### AI Model")
st.sidebar.info("Random Forest Classifier")
st.sidebar.success("AI Model Loaded")
st.sidebar.write("### Sensors")
st.sidebar.info("Vibration + Acoustic")

st.sidebar.write("### Deployment")
st.sidebar.info("Edge Device")

st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")

# ----------------------------
# Top Metrics
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏭 Machine", "Motor-01")

with col2:
    st.metric("🤖 AI Status", "Ready")

with col3:
    st.metric("🎯 Model Accuracy", "99.0%")

with col4:
    st.metric("⚡ Latency", "42 ms")

st.divider()

# ----------------------------
# Main Dashboard
# ----------------------------
left, right = st.columns([2, 1])

with left:

    st.subheader("📈 Machine Health Trend")

    chart_data = pd.DataFrame(
        {
            "Health Score": [99, 98, 97, 98, 99, 97, 96, 98, 99, 98]
        }
    )

    st.line_chart(chart_data)

with right:

    st.subheader("🖥 Current Status")

    st.success("Machine Operating Normally")

    st.info("No anomaly detected.")

    st.metric("Temperature", "41°C")

    st.metric("Vibration", "0.13 g")

    st.metric("Sound Level", "42 dB")

st.divider()

# ----------------------------
# Recent Activity
# ----------------------------
st.subheader("📋 Recent Activity")

alerts = pd.DataFrame({
    "Time": [
        "10:02",
        "10:20",
        "10:45",
        "11:10"
    ],
    "Machine": [
        "Motor-01",
        "Motor-01",
        "Motor-01",
        "Motor-01"
    ],
    "Status": [
        "Healthy",
        "Healthy",
        "Healthy",
        "Healthy"
    ]
})

st.dataframe(alerts, use_container_width=True)

st.divider()

# ----------------------------
# Fault Simulation
# ----------------------------
st.subheader("🧪 Virtual PoC Demonstration")

if st.button("🚨 Simulate Fault", use_container_width=True):

    st.error("## ⚠ Bearing Wear Detected")

    st.progress(92)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk Level", "High")

    with col2:
        st.metric("Confidence", "92%")

    st.warning("Immediate maintenance is recommended.")

    st.write("### AI Analysis")

    st.write("""
- Abnormal vibration detected.
- Frequency spectrum deviation observed.
- Possible bearing wear.
- Maintenance should be scheduled immediately.
""")

else:

    st.success("System is operating normally.")

st.divider()

# ----------------------------
# AI Prediction
# ----------------------------

st.divider()
st.header("🤖 AI Prediction")

air_temp = st.number_input("Air Temperature (K)", value=300.0)
process_temp = st.number_input("Process Temperature (K)", value=310.0)
speed = st.number_input("Rotational Speed (RPM)", value=1500)
torque = st.number_input("Torque (Nm)", value=40.0)
tool_wear = st.number_input("Tool Wear (min)", value=10)

machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

st.write("### Failure Type (Optional)")

twf = st.checkbox("Tool Wear Failure (TWF)")
hdf = st.checkbox("Heat Dissipation Failure (HDF)")
pwf = st.checkbox("Power Failure (PWF)")
osf = st.checkbox("Overstrain Failure (OSF)")
rnf = st.checkbox("Random Failure (RNF)")

type_L = 1 if machine_type == "L" else 0
type_M = 1 if machine_type == "M" else 0

if st.button("🔍 Predict Machine Health"):

    input_data = pd.DataFrame([[
        air_temp,
        process_temp,
        speed,
        torque,
        tool_wear,
        int(twf),
        int(hdf),
        int(pwf),
        int(osf),
        int(rnf),
        type_L,
        type_M
    ]], columns=[
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "TWF",
        "HDF",
        "PWF",
        "OSF",
        "RNF",
        "Type_L",
        "Type_M"
    ])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    confidence = max(probability) * 100

    if prediction == 0:
        st.success("🟢 Machine Healthy")
        st.metric("Confidence", f"{confidence:.2f}%")
    else:
        st.error("🔴 Machine Failure Detected")
        st.metric("Confidence", f"{confidence:.2f}%")        
# ----------------------------
# Footer
# ----------------------------
st.caption(
    "EdgeSense AI | Tata Technologies InnoVent 2026 | "
    "Edge AI for Industrial Predictive Maintenance"
)

