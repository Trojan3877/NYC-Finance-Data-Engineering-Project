# 🏙️ NYC Finance Data Engineering Project (L7 Production-Ready)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-green?logo=nvidia)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8?logo=snowflake)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![CI/CD](https://img.shields.io/badge/GitHub-Actions-black?logo=github)
![Status](https://img.shields.io/badge/Production-Ready-success)
![Repo Stats](https://github-readme-stats.vercel.app/api/pin/?username=Trojan3877&repo=NYC-Finance-Data-Engineering-Project&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Trojan3877&layout=compact&theme=radical)

---

## 📌 Overview
This project is a **production-grade Data Engineering & ML pipeline** built on real-world financial datasets.  
It demonstrates **end-to-end system design**, **cloud-ready deployment**, **GPU acceleration**, and **modern MLOps practices** used by Big Tech and FinTech companies.

---

## 🧠 Core Capabilities
- Scalable ETL pipeline for NYC financial datasets  
- Snowflake-backed analytics warehouse  
- ML model training with **GPU (CUDA) support**  
- MLflow experiment tracking  
- Dockerized microservices  
- CI/CD with GitHub Actions  
- Cloud-ready (Render / GPU providers)

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7e616bb5-f566-4a33-929f-f5cdc9e1cc5e" />

## 🧰 Tech Stack

### Data Engineering
- **Python 3.10**
- **Pandas / NumPy**
- **Snowflake**
- **CSV / Parquet Pipelines**

### Machine Learning
- **Scikit-Learn**
- **PyTorch / TensorFlow (GPU-ready)**
- **MLflow**

### Infrastructure & DevOps
- **Docker (CUDA-enabled)**
- **GitHub Actions (CI/CD)**
- **Render Deployment**
- **NVIDIA CUDA**

### APIs & Monitoring
- **FastAPI**
- **MLflow Tracking UI**

---
🧩 Logical Flow 
NYC Open Finance Data
        ↓
Data Ingestion (CSV / APIs)
        ↓
ETL Processing (Python / Pandas)
        ↓
Snowflake Data Warehouse
        ↓
Feature Engineering
        ↓
ML Model Training (GPU / CUDA)
        ↓
MLflow Experiment Tracking
        ↓
FastAPI Prediction Service
        ↓
Cloud Deployment (Docker / Render
## ⚡ Quick Start (Local)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Trojan3877/NYC-Finance-Data-Engineering-Project.git
cd NYC-Finance-Data-Engineering-Project
pip install -r requirements.txt
python pipeline.py
docker build -t nyc-finance-pipeline .
docker run nyc-finance-pipeline
docker run --gpus all nyc-finance-pipeline
python pipeline.py

📊 MLflow Tracking
mlflow ui


Open: http://localhost:5000

Tracks:

Metrics

Parameters

Model versions

Experiments
