import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.title("🗺 National Risk Heatmap")

m=folium.Map(location=[22.5,78.9],zoom_start=5,tiles="CartoDB dark_matter")

for _ in range(40):
    lat=random.uniform(8,35)
    lon=random.uniform(68,97)
    risk=random.random()

    color="green"
    if risk>0.7: color="red"
    elif risk>0.4: color="orange"

    folium.Circle(
        location=[lat,lon],
        radius=60000,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(m)

st_folium(m,height=650)