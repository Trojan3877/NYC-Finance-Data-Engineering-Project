# 🚦 SafeSight AI — Production-Ready AI Safety Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![CUDA](https://img.shields.io/badge/NVIDIA-CUDA--Ready-brightgreen)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blueviolet)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI](https://img.shields.io/github/actions/workflow/status/Trojan3877/SafeSight-AI/ci.yml)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/Trojan3877/SafeSight-AI)
![Repo Size](https://img.shields.io/github/repo-size/Trojan3877/SafeSight-AI)
![Stars](https://img.shields.io/github/stars/Trojan3877/SafeSight-AI?style=social)
![Repo Stats](https://github-readme-stats.vercel.app/api/pin/?username=Trojan3877&repo=NYC-Finance-Data-Engineering-Project&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Trojan3877&layout=compact&theme=radical)

---

## 🧠 Overview

**SafeSight AI** is an end-to-end, production-ready AI system designed to demonstrate **real-world ML engineering**, **system design**, and **deployment readiness**.

This project showcases:
- Scalable ML pipelines
- GPU-accelerated inference (NVIDIA CUDA)
- RESTful APIs (FastAPI)
- Live dashboards (Streamlit)
- Experiment tracking (MLflow)
- CI/CD automation
- Cloud-deployable architecture (Render, Docker)

Built with **Big Tech engineering standards** in mind.

---

## 🧩 System Architecture

![System Architecture](docs/system_architecture.png)

### Logical Flow
Data Sources
↓
ETL / Feature Engineering
↓
Model Training (GPU / CUDA)
↓
MLflow Experiment Tracking
↓
FastAPI Inference Service
↓
Streamlit Live Dashboard
↓
Docker + CI/CD + Cloud Deployment

---

## ⚙️ Tech Stack

**Core**
- Python 3.10+
- NumPy, Pandas
- Scikit-learn

**ML & Ops**
- MLflow
- NVIDIA CUDA
- Joblib

**Backend**
- FastAPI
- Uvicorn

**Frontend**
- Streamlit

**DevOps**
- Docker
- GitHub Actions (CI/CD)
- Render (Cloud Deployment)
- n8n (Automation)

---

## 📊 Metrics Snapshot

| Category | Value |
|------|------|
| Accuracy | 0.89 |
| F1 Score | 0.86 |
| ROC-AUC | 0.91 |
| Avg Inference Latency | 38ms |
| Throughput | ~1,200 req/min |
| GPU Support | ✅ |

(Full details in `metrics.md`)

---

## 🚀 Quick Start

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Trojan3877/SafeSight-AI.git
cd SafeSight-AI
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run API
uvicorn api.main:app --reload


➡ API Docs: http://localhost:8000/docs

4️⃣ Run Dashboard
streamlit run dashboard/app.py


➡ Dashboard: http://localhost:8501

🧪 Testing
pytest tests/


Tests are executed automatically via GitHub Actions CI on every push and PR.

🐳 Docker (GPU-Ready)
docker build -t safesight-ai .
docker run -p 8000:8000 safesight-ai


CUDA-enabled base image supports NVIDIA GPUs.

☁️ Cloud Deployment

Render

Web Service

Docker enabled

Start Command:

uvicorn api.main:app --host 0.0.0.0 --port 10000

🤖 Automation

n8n workflows automate retraining & pipeline execution

Designed for scalable production workflows
SafeSight-AI/
├── api/
├── dashboard/
├── models/
├── tests/
├── docs/
├── n8n/
├── metrics.md
├── dailylog.md
├── CONTRIBUTING.md
├── Dockerfile
├── docker-compose.yml
└── README.md



