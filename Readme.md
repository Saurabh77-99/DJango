Django is web framework
------------------------
### uv installation :-
uv package

pip install uv

#### for creating virtual environment:-
uv venv

for activation   :- .venv\Scripts\activate
for deactivation :- deactivate

### Installing Django:-
uv pip install Django

### Creating Project:-
django-admin startproject Project-name

cd Project-name

There will be subfolder of the same project-name in it  

manage.py -> Its root file

### To run project:-
python manage.py runserver port-number

After running the command listed we get db.sqlite3 file

manage.py - starting point file,sets up environment and gets invoke first

db.sqlite - its default database used in django

multiple modules therefore [pycache] folder is built.

### configuration of Django:-
settings.py 
Middlewares , auth , templates

urls.py - routing files

admin is by default.

views.py - business logic

------------------------------------------------------------
### Django architecture

User --> req--> web -->req--> Django --> url resolver --? req--> urls.py --req--> views.py -->Model.py --> database       ^                                                    |
                               |                                                    |
                               |_________________________________________________response

views.py in(Jango/Jango) -> logic and response

Basic Code in views.py for request , response 

urls.py edited in url patterns and routing:-
```
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
```

After this run the command and watch directory too if it's correct:-
``` 
python manage.py runserver 
```
### Templating engine   
----------------------------
uv pip install django-tailwind
uv pip install 'django-tailwind[reload]'

if it gives error then 
python -m ensurepip --upgrade
python -m pip install --upgrade pip
pip install 'django-tailwind[reload]'

python manage.py tailwind init 
after running this command in app directory, you will get theme folder formed in pwd.


