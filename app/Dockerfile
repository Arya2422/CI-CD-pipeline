# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (optional, for MySQL clients, etc.)
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
