FROM apache/airflow:2.8.2
COPY requirements.txt .
RUN pip install -r requirements.txt
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         nano \
	 iputils-ping \
	 git
COPY ./.dbt /home/airflow/.dbt
USER airflow