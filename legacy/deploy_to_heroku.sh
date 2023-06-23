#!/bin/sh

#################################################################
# SHELL SCRIPT DEPLOY AIRFLOW APP TO HEROKU MANUALLY
#################################################################
set -e

# Install custom python package if requirements.txt is present
if [ -e "requirements.txt" ]; then
    echo 'install custom python package...'  && $(which pip) install --user -r requirements.txt
fi

# Build heroku project 
heroku create airflow-heroku 
echo 'add postgre and connect to airflow app...'
heroku addons:create heroku-postgresql:dev -a airflow-heroku
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__SQL_ALCHEMY_CONN=$(heroku config -a airflow-heroku | grep DATABASE_URL | sed -e 's/ //g' | cut -d  ':' -f 2-)
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__LOAD_EXAMPLES=False
heroku config:set  -a airflow-heroku  AIRFLOW__CORE__FERNET_KEY=${FERNET_KEY:=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")}
heroku config:set  -a airflow-heroku  AIRFLOW__WEBSERVER__AUTHENTICATE=True
heroku config:set  -a airflow-heroku  AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
echo 'Airflow Config Vars :\n' &&  heroku config -a airflow-heroku
echo 'add heroku remote git...' && heroku git:remote -a airflow-heroku
echo 'deploy...' && git push heroku master 
echo 'deploy... please check the deploy log via command : heroku logs --tail \n' && echo 'deploy OK, please visit the app via http://airflow-heroku.herokuapp.com/ or via `heroku open` command '

# Set up airflow user account
# $ heroku run bash
# $ python 
# import airflow
# from airflow import models, settings
# from airflow.contrib.auth.backends.password_auth import PasswordUser
# user = PasswordUser(models.User())
# user.username = 'user'
# user.email  = 'example@airflow.com'
# user.password  = '123'
# session = settings.Session()
# session.add(user)
# session.commit()
# session.close()
# exit()