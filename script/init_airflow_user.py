import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

def main():
    print (">>>> create airflow user...")
    user = PasswordUser(models.User())
    user.username = 'user'
    user.email  = 'example@airflow.com'
    user.password  = '123'
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()
    print (">>>> create airflow user OK : user_id : user,  password : 123")

if __name__ == '__main__':
    main()
