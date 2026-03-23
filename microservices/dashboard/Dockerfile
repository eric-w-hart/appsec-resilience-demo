FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir Flask==3.1.3
COPY app.py .
COPY anomaly_demo.py .
CMD ["python", "app.py"]