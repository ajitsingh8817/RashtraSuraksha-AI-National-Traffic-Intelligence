import streamlit as st
import time
import random
import pyttsx3

st.set_page_config(
    page_title="RashtraSuraksha AI - National War Room",
    layout="wide",
    page_icon="🚨"
)

# ====== WAR ROOM CSS ======
st.markdown("""
<style>

body {
    background: radial-gradient(circle at center, #000000 0%, #0f0f0f 40%, #111 100%);
    color: white;
}

.big-title {
    font-size:65px;
    font-weight:900;
    text-align:center;
    color:#ff1a1a;
    text-shadow: 0px 0px 30px red;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { text-shadow: 0 0 20px red; }
    50% { text-shadow: 0 0 60px red; }
    100% { text-shadow: 0 0 20px red; }
}

.metric-card {
    background: rgba(255,0,0,0.1);
    border: 1px solid red;
    padding:30px;
    border-radius:15px;
    text-align:center;
    box-shadow: 0 0 25px red;
    transition: 0.4s;
}

.metric-card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 50px red;
}

.stButton>button {
    background-color:#ff0000;
    color:white;
    border-radius:10px;
    font-weight:bold;
    height:50px;
}

</style>
            with open("radar.html","r") as f:
    radar_html = f.read()

st.components.v1.html(radar_html, height=800)
""", unsafe_allow_html=True)

# ====== TITLE ======
st.markdown('<div class="big-title">🚨 RASHTRASURAKSHA AI WAR ROOM</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ====== LIVE COUNTERS ======
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h1>{random.randint(100000,150000)}</h1>
        <p>Total Accidents Monitored</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h1>{random.randint(70,95)}%</h1>
        <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h1>{random.randint(5,20)}</h1>
        <p>Active High Risk Zones</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
engine = pyttsx3.init()

# ====== AUTO ALERT SYSTEM ======
risk_level = random.randint(0,100)

if risk_level > 80:
    st.error("🚨 NATIONAL HIGH RISK ALERT")
    engine.say("Warning. National high risk alert.")
    engine.runAndWait()

elif risk_level > 50:
    st.warning("⚠️ Elevated Risk Conditions")
    engine.say("Elevated traffic risk detected.")
    engine.runAndWait()

else:
    st.success("✅ Traffic Flow Stable")