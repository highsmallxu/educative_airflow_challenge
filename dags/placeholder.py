# implement your DAG here
import os
import json
from airflow.decorators import dag
import pendulum

# make sure you add the following code to your DAG
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth.json"
os.environ["AIRFLOW_CONN_FRANKFURTER_API"] = "http://https://api.frankfurter.app/"
PROJECT_ID = json.load(open("auth.json","rb"))["quota_project_id"]


@dag(
    schedule="* * * * 1-5",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"],
    template_searchpath=["/usercode/sql"]
)
def pipeline():
    pass