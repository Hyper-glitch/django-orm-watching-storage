# Bank security console

This inner repo for bank employees 'Shine'. Bank security console it is a website that allows you to connect 
to remote database and controls visits and pass cards employees of our Bank.

### Starting
| Environmental | Description                                               |
|---------------|-----------------------------------------------------------|
| `DB_HOST`     | Database hostname                                         |
| `DB_PORT`     | Database port connection                                  |
| `DB_NAME`     | Database name                                             |
| `DB_USERNAME` | Database username                                         |
| `DB_PASSWORD` | Database password                                         |
| `SECRET_KEY`  | A secret key for a particular Django installation         |
| `DEBUG`       | It provides a detailed traceback with the local variables |

### How to install
1. clone the repository:
```
https://github.com/Hyper-glitch/django-orm-watching-storage
```
2. create **.env** file and set the environmental variables as described above.
3. create venv
```
python3 -m venv venv
```
4. activate venv
```
. venv/bin/activate
```
5. python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip3 install -r requirements.txt
```
6. run django server
```
python3 manage.py runserver
```


### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).