import streamlit as st
import joblib
import pandas as pd
import time

model=joblib.load("model/risk_model.pkl")
encoders=joblib.load("model/encoders.pkl")

st.title("🛰 National Command Center")

vehicles=st.slider("Vehicles per hour",100,5000,1500)
weather=st.selectbox("Weather",["Clear","Rain","Fog"])
road=st.selectbox("Road Type",["Highway","Urban","Rural"])
hour=st.slider("Hour",0,23,18)

weather_enc=encoders["weather"].transform([weather])[0]
road_enc=encoders["road"].transform([road])[0]

input_df=pd.DataFrame([{
    "vehicles":vehicles,
    "weather":weather_enc,
    "road":road_enc,
    "hour":hour
}])

if st.button("🔥 Activate Prediction Engine"):
    risk=model.predict_proba(input_df)[0][1]

    col1,col2,col3=st.columns(3)
    col1.markdown(f'<div class="card"><h2>🚗 Traffic</h2><h1>{vehicles}</h1></div>',unsafe_allow_html=True)
    col2.markdown(f'<div class="card"><h2>⏰ Hour</h2><h1>{hour}</h1></div>',unsafe_allow_html=True)
    col3.markdown(f'<div class="card"><h2>⚠ Risk</h2><h1>{risk*100:.2f}%</h1></div>',unsafe_allow_html=True)

    time.sleep(0.5)

    if risk>0.7:
        st.markdown('<div class="alert">🚨 CRITICAL RISK DETECTED 🚨</div>',unsafe_allow_html=True)
    elif risk>0.4:
        st.warning("⚠ Moderate Risk")
    else:
        st.success("✅ Safe Zone")