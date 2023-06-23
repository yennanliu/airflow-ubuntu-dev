## heroku_command.md

### 1) Check Heroku log 
```bash
$ heroku logs --tail
```
### 2) Connect to Heroku bash 
```bash
$ heroku run bash
```

### 3) Connect to Heroku Postgre 
```bash
$ heroku pg:psql postgresql-aerodynamic-<xxx> --app airflow-heroku
```