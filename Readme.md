Django is web framework
------------------------
### uv installation :-
uv package

    pip install uv

### for creating virtual environment:-
    uv venv

for activation:-

    .venv\Scripts\activate 

for deactivation :- 

    deactivate

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

    from . import views
    urlpatterns = [
        path("admin/", admin.site.urls),
        path('',views.home,name='home'),
        path('about/',views.about,name='about'),
        path('contact/',views.contact,name='contact'),
    ]

After this run the command and watch directory too if it's correct:-
 
        python manage.py runserver 

### Template  
Creating two folder static and templates inside Jango not Jango/Jango
index.html inside Templates , watchout code in views.py(render,return)

If template doesn't loads then get into settings.py

There will be a section of TEMPLATES in it and include templates in DIRS.

    "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,

After do this: Jango/templates/website/index.html, it will give error in rendering therefore path must be mentioned in views.py 
    
Before templates/website it was templates/index.html:

    def home(request):
        return render(request,'index.html')

After templates/website:

    def home(request):
        return render(request,'website/index.html')

Creating Jango/static/style.css:-

this won't work
    
    <link rel="stylesheet" href="../../static/style.css> 

### templating engine

This will work injecting css, static refers to loading static asset

    <link rel="stylesheet" href="{% static 'style.css' %}">
    
This won't still render, you need to include {% load static %}

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="{% static 'style.css' %}">
    </head>
    <body>
        <h1>Djangoo</h1>
    </body>
    </html>

settings.py(modified for rendering css):-

    STATIC_URL = "static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]    

Now you can finally inject css in it


    uv pip install django-tailwind
    uv pip install 'django-tailwind[reload]'

if it gives error then 

    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
    pip install 'django-tailwind[reload]'
    python manage.py tailwind init 

after running this command in app directory, you will get theme folder formed in pwd.


