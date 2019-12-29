## heroku_command.md

### Check Heroku log 
```bash
$ heroku log 
```
### Connect to Heroku bash 
```bash
$ heroku console log
```

### Connect to Heroku Postgre 
```bash
$ heroku pg:psql postgresql-aerodynamic-<xxx> --app airflow-heroku
```