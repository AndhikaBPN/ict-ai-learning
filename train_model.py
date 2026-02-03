import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load data
data = pd.read_csv("data.csv")

X = data[['nilai_kuis', 'waktu_pengerjaan']]
y = data['level']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model AI berhasil dibuat dan disimpan!")