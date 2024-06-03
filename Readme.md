Django is web framework
------------------------
### uv installation :-
uv package

pip install uv

#### for creating virtual environment:-
uv venv

for activation   :- .venv\Scripts\activate
for deactivation :- deactivate

### Installing Django:
uv pip install Django

### Creating Project:
django-admin startproject Project-name

cd Project-name

### To run project:-
python manage.py runserver port-number

- we get db.sqlite3 file

manage.py - starting point file and gets invoke first

db.sqlite - its default database used in django

multiple modules therefore [pycache] folder is built.

settings.py -- configuration of Django
Middlewares , auth , templates

urls.py - routing files
admin is by default.

views.py - business logic

------------------------------------------------------------
Django architecture

User --req--> web --req--> Django --url resolver --req--> urls.py --req--> views.py -->Model.py --> database      ^                                                 |
                              |                                                 |
                              |______________________________________________response


Templating engine

----------------------------
uv pip install django-tailwind
uv pip install 'django-tailwind[reload]'

if it gives error then 
python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install 'django-tailwind[reload]'

python manage.py tailwind init 
after running this command in app directory, you will get theme folder formed in pwd.


