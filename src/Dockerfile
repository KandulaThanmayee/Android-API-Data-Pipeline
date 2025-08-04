FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir kafka-python boto3 pandas numpy matplotlib seaborn
CMD ["python3", "log_consumer.py"]
