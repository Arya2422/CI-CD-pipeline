# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies safely
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port and start Flask
EXPOSE 5000
CMD ["python", "app.py"]
