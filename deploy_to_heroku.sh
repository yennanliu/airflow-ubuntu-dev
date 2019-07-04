#!/bin/sh

#################################################################
# SHELL SCRIPT DEPLOY AIRFLOW APP TO HEROKU MANUALLY
#################################################################
set -e
heroku create airflow-heroku 
echo 'add postgre and connect to airflow app...'
heroku addons:create heroku-postgresql:dev -a airflow-heroku
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__SQL_ALCHEMY_CONN=$(heroku config -a airflow-heroku | grep DATABASE_URL | sed -e 's/ //g' | cut -d  ':' -f 2-)
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__LOAD_EXAMPLES=False
f_key=$(python -c "from cryptography.fernet import Fernet; print (Fernet.generate_key())") && f_key_fix="${key##b}"
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__FERNET_KEY=$(f_key_fix)
heroku config:set -a airflow-heroku AIRFLOW__WEBSERVER__AUTHENTICATE=True
heroku config:set  -a airflow-heroku AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
echo 'Airflow Config Vars :\n' && heroku config -a airflow-heroku
echo 'add heroku remote git...'
heroku git:remote -a airflow-heroku
echo 'deploy...'
git push heroku master 
echo 'deploy... please check the deploy log via command : heroku logs --tail'
echo 'deploy OK, please visit the app via http://airflow-heroku.herokuapp.com/ or via `heroku open` command '