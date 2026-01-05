import joblib
import pandas as pd
import json
from kafka import KafkaConsumer

# 1. Load the pre-trained model and scaler
model = joblib.load('titanic_model.pkl')
scaler = joblib.load('scaler.pkl')

# 2. Initialize Kafka Consumer
# We point to 'kafka:9092' because that's the service name in Docker
consumer = KafkaConsumer(
    'titanic_topic',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🚢 [CONSUMER] Connected to Kafka. Waiting for passenger data...")

for message in consumer:
    passenger_data = message.value
    
    # 3. Data Processing
    # Ensure the dictionary matches the features used in training
    df_input = pd.DataFrame([passenger_data])
    
    # 4. Prediction
    X_scaled = scaler.transform(df_input)
    prediction = model.predict(X_scaled)[0]
    
    result = "SURVIVED" if prediction == 1 else "PERISHED"
    print(f"📥 Received: {passenger_data.get('Name', 'Unknown')} | Prediction: {result}")