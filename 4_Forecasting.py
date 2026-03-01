import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.title("📈 24 Hour Risk Forecast")

hours=list(range(24))
risk=[random.uniform(0.3,0.9) for _ in hours]

df=pd.DataFrame({"Hour":hours,"Predicted Risk":risk})

fig=px.line(df,x="Hour",y="Predicted Risk",markers=True)

st.plotly_chart(fig,use_container_width=True)