import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

model=joblib.load("model/risk_model.pkl")

features=["vehicles","weather","road","hour"]
importance=model.feature_importances_

df=pd.DataFrame({"Feature":features,"Importance":importance})

fig=px.bar(df,x="Feature",y="Importance",color="Importance")

st.plotly_chart(fig,use_container_width=True)