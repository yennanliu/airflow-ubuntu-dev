# README

## Commands
```bash
docker exec -it --user airflow airflow-scheduler bash -c "airflow dags list"
docker exec -it --user airflow airflow-scheduler bash -c "airflow dags list-import-errors"
```