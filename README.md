### Quick start 
```bash
# clone repo, install for local 
$ cd && git clone https://github.com/yennanliu/data_infra_repo.git
$ cd && cd data_infra_repo/superset_infra/posgre_heroku_deploy 
$ pip install -r requirements.txt 
# heroku setting 
$ heroku create airflow-heroku 
$ heroku addons:create heroku-postgresql:dev -a airflow-heroku
# show heroku config 
$ heroku config -a airflow-heroku
# heroku airflow config 
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgres://bmzlfnumagwnfl:81c3f6d09dcc9e3f5a0a36aa83e6fbc432e2c3810d6e349e4cb41ef997501901@ec2-50-19-221-38.compute-1.amazonaws.com:5432/d12rb6i3rphsph 
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__LOAD_EXAMPLES=False
$ heroku config:set  -a airflow-heroku  AIRFLOW__CORE__FERNET_KEY=pndiNQ25jhjnzWr1zanek85Uqr1J38zQcJXUl7H7hNw=
$ heroku config:set -a airflow-heroku AIRFLOW__WEBSERVER__AUTHENTICATE=True
$ heroku config:set  -a airflow-heroku AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
# get AIRFLOW_FERNET_KEY 
$ python -c \"from cryptography.fernet import Fernet; print (Fernet.generate_key())\"
# add remote heroku git 
$ heroku git:remote -a airflow-heroku
$ git push heroku master 
# push to heroku
$ git push heroku master
# track deploy log 
$ heroku logs --tail
```
### Ref 
- Deploy airflow to Heroku
	- https://medium.com/@damesavram/running-airflow-on-heroku-ed1d28f8013d
	- https://github.com/leandroloi/heroku-airflow


	