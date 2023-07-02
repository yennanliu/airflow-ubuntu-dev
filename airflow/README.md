# README

## Commands

```bash
git clone https://github.com/yennanliu/airflow-heroku-dev.git
cd airflow-heroku-dev
cd airflow
docker-compose up
```

```bash
docker exec -it --user airflow airflow-scheduler bash -c "airflow dags list"
docker exec -it --user airflow airflow-scheduler bash -c "airflow dags list-import-errors"


# docker ps -a 
#docker exec -it 4c1a10e004d4f3cf59071cc3773277cec7fcd4f6506ef3c47fea39331c9e114a /bin/sh
#sudo docker exec -it 971ea5970dc1 bash
sudo pip install aws_requests_auth
sudo pip install 'apache-airflow[amazon]'
sudo pip install boto3
```

```bash
# 8) STOP --------------------------
# Stop all running containers
# https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481
docker stop -f $(docker ps -aq)
#docker stop $(docker ps -a -q)


# 9) REMOVE --------------------------
# Remove all containers
sudo docker rm -f $(sudo docker ps -a)
# Remove all images
docker rmi -f $(docker images -q)
# remove all containers in docker
docker rm -f $(docker ps -a -q)
# remove all images in docker
docker rmi -f $(docker images -q -a)
# clean docker cache : https://stackoverflow.com/questions/65405562/is-there-a-way-to-clean-docker-build-cache
docker builder prune
```

## Ref
- https://github.com/DataEngDev/airflow_in_docker_compose/blob/master/docs/quick_start_airflow.md
- ssh conn it setup for airflow
	- https://cloud.ibm.com/docs/ssh-keys?topic=ssh-keys-generating-and-using-ssh-keys-for-remote-host-authentication
	- https://github.com/yennanliu/til/blob/master/README.md#20210319
