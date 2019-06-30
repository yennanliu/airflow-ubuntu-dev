# airflow-heroku-dev 
> Demo how to deploy Airflow to Heroku cloud, for more data infra and ETL development information, please visit 
[Data infra delopment](https://github.com/yennanliu/data_infra_repo)
[XJob (Airflow ETL delopment)](https://github.com/yennanliu/XJob)

[![Build Status](https://travis-ci.org/yennanliu/Xjob.svg?branch=master)](https://travis-ci.org/yennanliu/airflow-heroku-dev)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/airflow-heroku-dev/pulls)

### Deploy to Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yennanliu/airflow-heroku-dev)

### DEMO 
[Airflow Heroku demo](http://airflow-heroku.herokuapp.com/)
- userid : `user` |  password : `123`


### File structure 
```bash
# ├── Procfile        : define the initial operations when Heroku app built and deployed 
# ├── Procfile_dev
# ├── README.md
# ├── app.json         : define how to deploy to Heroku as app 
# ├── dags             : Dags define how does airflow run process  
# ├── init_env.sh      : init script for DB (maybe not necessary, need to check)
# └── requirements.txt : install needed libraries for airflow 
```

### Quick start 
<details>
<summary>Quick-Start</summary>

```bash
# clone the repo
$ cd && git https://github.com/yennanliu/airflow-heroku-dev.git
$ cd && cd airflow-heroku-dev 
# create heroku project  
$ heroku create airflow-heroku 
# set up postgresql as airflow backend 
$ heroku addons:create heroku-postgresql:dev -a airflow-heroku
# show heroku config 
$ heroku config -a airflow-heroku
# heroku airflow config 
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__SQL_ALCHEMY_CONN=<replace_with_your_postgre_DB_url>
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__LOAD_EXAMPLES=False
# get the via AIRFLOW_FERNET_KEY 
$ python -c \"from cryptography.fernet import Fernet; print (Fernet.generate_key())\"
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__FERNET_KEY=<your_FERNET_KEY>
$ heroku config:set -a airflow-heroku AIRFLOW__WEBSERVER__AUTHENTICATE=True
$ heroku config:set  -a airflow-heroku AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
# update to git
$ git add . && git commit -m 'code update for heroku deployment'
# add remote heroku git 
$ heroku git:remote -a airflow-heroku
# deploy to heroku 
$ git push heroku master 
# track deploy log 
$ heroku logs --tail -a airflow-heroku
# if everything works fine, should be able to access your app via command below
$ heroku open 
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
	