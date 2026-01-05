# Use a slim version of Python for faster builds
FROM python:3.11-slim

WORKDIR /app

# Install standard dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our model assets and production scripts
COPY titanic_model.pkl .
COPY scaler.pkl .
COPY consumer.py .

# Run the consumer service
CMD ["python", "consumer.py"]