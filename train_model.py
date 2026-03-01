import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = {
    "vehicles":[500,1200,2500,4000,1800,3200,600,2700,1500,3800],
    "weather":["Clear","Rain","Fog","Rain","Clear","Fog","Clear","Rain","Clear","Fog"],
    "road":["Highway","Urban","Highway","Highway","Urban","Highway","Rural","Urban","Rural","Highway"],
    "hour":[9,18,22,20,14,23,7,19,10,21],
    "accident":[0,1,1,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

encoders={}
for col in ["weather","road"]:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col])
    encoders[col]=le

X=df.drop("accident",axis=1)
y=df["accident"]

model=RandomForestClassifier(n_estimators=300,max_depth=12)
model.fit(X,y)

joblib.dump(model,"model/risk_model.pkl")
joblib.dump(encoders,"model/encoders.pkl")

print("Model Ready 🔥")