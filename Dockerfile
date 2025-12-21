# NVIDIA CUDA base image
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose MLflow port (optional)
EXPOSE 5000

# Run main pipeline (change if needed)
CMD ["python3", "pipeline.py"]
