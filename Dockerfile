FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api
COPY models ./models

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
