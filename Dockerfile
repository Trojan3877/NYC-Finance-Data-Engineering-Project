# Use a slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# If you rely on environment variables, you can define defaults here
ENV DATA_DIR=/app/data

# Default command can be overridden; this example assumes a run script exists
ENTRYPOINT ["bash", "run_etl.sh"]
