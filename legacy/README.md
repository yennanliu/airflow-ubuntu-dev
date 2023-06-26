<h1 align="left"><a href="http://airflow-heroku.herokuapp.com/">airflow-heroku-dev</a></h1>

> Demo how to `deploy an Airflow app to Heroku cloud`. The main idea is : start from local airflow server running, python packages installation, DB configuration (connect to Airflow), integrate with Travis CI, make the processes all integrated and automative : testing(dev), docker push (dev), and airflow Heroku deployment (if and only if all checks passed). For more data infra/ETL development ideas, please visit :

* Daas (Data as a service) repo :  [Data infra build](https://github.com/yennanliu/data_infra_repo) -> [ETL build](https://github.com/yennanliu/XJob) -> [DS application demo](https://github.com/yennanliu/analysis)
* Mlflow Heroku demo : [mlflow-heroku-dev](https://github.com/yennanliu/mlflow-heroku-dev)

[![Build Status](https://travis-ci.org/yennanliu/airflow-heroku-dev.svg?branch=master)](https://travis-ci.org/yennanliu/airflow-heroku-dev)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/airflow-heroku-dev/pulls)

### Deploy to Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yennanliu/airflow-heroku-dev)

### DEMO 
[Airflow Heroku demo](http://airflow-heroku.herokuapp.com/)
- userid : `user` |  password : `123`


### File structure 
```bash
# ├── Dockerfile          : file build docker image 
# ├── Procfile            : define the initial operations when Heroku app built and deployed 
# ├── Procfile_dev        : Procfile file for dev 
# ├── README.md
# ├── app.json            : define how to deploy to Heroku as app 
# ├── config              : config file for airflow (airflow.cfg)
# ├── dags                : code define Airflow jobs  
# ├── deploy_to_heroku.sh : shell script deploy app to Heroku
# ├── init_env.sh         : init script for DB (maybe not necessary, need to check)
# ├── requirements.txt    : install needed libraries for airflow 
# └── script              : scripts help the deployment
```

### Quick start 
<details>
<summary>Prerequisites</summary>

```bash
# https://medium.com/@damesavram/running-airflow-on-heroku-ed1d28f8013d

# step 1) set up a Heroku account 
# https://dashboard.heroku.com/
# https://devcenter.heroku.com/articles/getting-started-with-python

# step 2) access the Heroku console page, check the account status 

# step 3) install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli#download-and-install

# step 4) install dev environment for python (e.g. conda)
# https://docs.conda.io/projects/conda/en/latest/user-guide/install/

```
</details>

<details>
<summary>Quick-Start</summary>

```bash
# clone the repo
$ cd && git https://github.com/yennanliu/airflow-heroku-dev.git
$ cd && cd airflow-heroku-dev 
# launch dev python env 
$ source activate <your_dev_env_name>
# install airflow packages and export it the requirements.txt
$ pip install "apache-airflow[postgres, password]" && pip freeze list > requirements.txt
# create heroku project (set airflow-heroku as project name)
$ heroku create airflow-heroku 
# set up postgresql as airflow backend (if not work, can via Heroku console too)
$ heroku addons:create heroku-postgresql:dev -a airflow-heroku
# show heroku config (check if DB url shown as expected)
$ heroku config -a airflow-heroku
# setting up heroku configs 
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__SQL_ALCHEMY_CONN=<replace_with_your_postgre_DB_url>
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__LOAD_EXAMPLES=False
# get the via AIRFLOW_FERNET_KEY 
$ python -c "from cryptography.fernet import Fernet; print (Fernet.generate_key())"
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__FERNET_KEY=<your_FERNET_KEY>
$ heroku config:set -a airflow-heroku AIRFLOW__WEBSERVER__AUTHENTICATE=True
$ heroku config:set  -a airflow-heroku AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
# git update and git push 
$ git add . && git commit -m 'update for heroku deploy' && git push origin 
# set up  remote heroku git 
$ heroku git:remote -a airflow-heroku
# heroku deploy  
$ git push heroku master 
# track deploy log 
$ heroku logs --tail -a airflow-heroku
# access the deployed Heroku app if everything above works fine 
$ heroku open 

# set up airflow user account 
$ heroku run bash
$ python 
# within in python console 
>>> import airflow
>>> from airflow import models, settings
>>> from airflow.contrib.auth.backends.password_auth import PasswordUser
>>> user = PasswordUser(models.User())
>>> user.username = 'user'
>>> user.email  = 'example@airflow.com'
>>> user.password  = '123'
>>> session = settings.Session()
>>> session.add(user)
>>> session.commit()
>>> session.close()
>>> exit()

```
</details>

### Todo 
- dockerize the project 
- unittest/integration test 
- better Backend DB configuration 

### Ref 
- Deploy airflow to Heroku
	- https://medium.com/@damesavram/running-airflow-on-heroku-ed1d28f8013d
	- https://github.com/leandroloi/heroku-airflow
	