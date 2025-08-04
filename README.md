# Android API Violation Data Engineering Pipeline

## Project Overview
This project automates the generation, streaming, analysis, and cloud storage of Android API usage logs and violations. It demonstrates data engineering and automation using Python, Kafka, Airflow, Docker, and AWS S3.

---

## Key Components

### 1. Input Generation Scripts
Python scripts that generate sample Java applications to test API usage and edge cases.
- All Java files are auto-generated and not included here (see /sample_data for a demo).

### 2. Data Analysis and Visualization
- Jupyter notebooks for detailed data analysis.
- `cs.py` script consolidates outputs and creates visualizations.

### 3. Streaming and Orchestration (Data Engineering)
- **Kafka streaming:** Real-time data streaming (see `log_producer.py`, `log_consumer.py`).
- **Airflow DAG:** Automates pipeline steps (see `airflow_dag.py`).
- **Docker & docker-compose:** For containerized, reproducible deployment.

### 4. Cloud Integration
- **cloud_upload.py**: Upload analysis outputs to AWS S3.
- Set credentials in `.env` (never commit real keys!)

---

## How to Run

### 1. Batch Workflow (Local)
- Run input generator scripts in `src/input_generators/`
- Analyze data with Jupyter notebooks in `/notebooks`
- Visualize using `cs.py`

### 2. Streaming Workflow (Kafka)
- Run `docker-compose up` in `/src` to start Kafka
- Run `log_producer.py` to stream logs
- Run `log_consumer.py` to process streaming data

### 3. Orchestration (Airflow)
- Add `airflow_dag.py` to your Airflow DAGs folder and run the DAG

### 4. Cloud Storage
- Set your AWS credentials (`.env` file)
- Run `cloud_upload.py` to upload outputs to S3

---

## File Structure

```
src/
  input_generators/
  log_producer.py
  log_consumer.py
  cloud_upload.py
  airflow_dag.py
  Dockerfile
  docker-compose.yml
notebooks/
data/
sample_data/
results/
docs/
README.md
requirements.txt
.gitignore
.env.example
```

---

## Notes
