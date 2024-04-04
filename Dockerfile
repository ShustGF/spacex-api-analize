FROM apache/airflow:2.8.2
COPY requirements.txt .
RUN pip install -r requirements.txt