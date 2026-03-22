import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Simulate container metrics (CPU %, memory %, network bytes over time)
np.random.seed(42)
normal_data = np.random.normal(loc=50, scale=10, size=(200, 3))  # normal traffic

# Inject anomalies (spikes)
anomalies = np.array([
    [180, 140, 280],   # CPU + mem spike
    [160, 120, 220],
    [55, 60, 750]      # normal CPU/mem, network flood
])
data = np.vstack([normal_data, anomalies])

# Train simple isolation forest (unsupervised anomaly detection)
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Predict: -1 = anomaly, 1 = normal
predictions = model.predict(data)
anomaly_indices = np.where(predictions == -1)[0]

print("Detected anomalies at indices:", anomaly_indices.tolist())
print("Last few points (includes anomalies):")
print(data[-5:])

# Plot (shows in Codespace if matplotlib backend works)
plt.figure(figsize=(10, 6))
plt.scatter(range(len(data)), data[:, 0], c=predictions, cmap='coolwarm', alpha=0.7)
plt.title("Container Metrics Anomaly Detection (red = anomaly)")
plt.xlabel("Time step")
plt.ylabel("CPU % (example metric)")
plt.colorbar(label="Prediction (-1 = anomaly)")
plt.show()