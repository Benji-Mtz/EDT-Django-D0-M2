# Proyecto Blog Django

## Creando un proyecto nuevo de Django

```sh
python3 -m venv .env
source .env/bin/activate
(.env) pip3 install django==3.2
(.env) pip3 freeze > requirements.txt
(.env) pip3 install -r requirements.txt
(.env) django-admin startproject startapp . #crea la carpeta startapp/ y el archivo manage.py
```
Como se ha creado un archivo `manage.py` es posible utilizarlo en lugar de usar el `django-admin`, por ejemplo:

```sh
(./.env)
(./.env) python manage.py startapp cursos
(./.env) python manage.py startapp profesores
(./.env) python manage.py startapp blog
(./.env) python manage.py runserver
  
  http://127.0.0.1:8000/

```
La estructura final de nuestro proyecto deberá de ser algo similar a esto:

```sh
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── templates
│   │   └── index.html
│   ├── tests.py
│   └── views.py
├── cursos
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── docker-compose.yaml
├── edteam
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── profesores
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py 
│   ├── tests.py
│   └── views.py
└── README.md

```

## Agregar las nuevas apps en `./edteam/settings.py`

```python

INSTALLED_APPS = [
    'cursos',
    'profesores',
    'blog',
    'django.contrib.admin',
    ...
]

```

## Primer vista `./blog/views.py`

Para esta vista se utilizara un template que renderice cierta informacion, por lo tanto dentro de nuestra carpeta de aplicación debera encontrarse la carpeta con el nombre exacto que es `tamplates` la cual contendra todos los archivos html.

```python

from django.shortcuts import render

def index(request):
    # Mock de datos
    lista_articulos = [
        {
            "titulo":"",
            "imagen":"",
            "autor":"",
        },
        {
            "titulo":"",
            "imagen":"",
            "autor":"",
        },
        {
            "titulo":"",
            "imagen":"",
            "autor":"",
        },
    ]
    
    context = {
        "articulos": lista_articulos
    }
    return render(request, 'index.html', context)

```
Así mismo para hacer el render de la vista iremos a la carpeta del proyecto principal archivo urls `./edteam/urls.py` y agregaremos la siguiente ruta:

```python
from blog.views import index

urlpatterns = [
    path('blog/', index),
    path('admin/', admin.site.urls),
]

```
## Creando modelos para la DB 

Un modelo es una clase por lo que en cada aplicación tendremos el archivo `models.py` en este caso en `./blog/models.py`

```python
from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    autor = models.CharField(max_length=150)
```
Para hacer la migracion debemos hacer un makemigration pero para la app especifica `blog` sino se hace en todas las apps
```sh
(./.env) python manage.py makemigrations blog
(./.env) python manage.py sqlmigrate blog 0001_initial #Show SQL
(./.env) python manage.py migrate blog
```
Esto creara la tabla blog_articulo

## Shell de Django

Podemos abrir el shell de django con `python manage.py shell`

```sh
>>> from blog.models import Articulo
>>> articulo1 = Articulo()
>>> articulo1.titulo = 'mi primer articulo'
>>> articulo1.imagen = 'articulo1.jpg'
>>> articulo1.autor = 'Benji Martinez'
>>> articulo1.save()
>>> articulo2 = Articulo.objects.create(titulo='Segundo articulo', imagen='articulo2.jpg', autor='Mich MA')
>>> Articulo.objects.all()
>>> articulo = Articulo.objects.get(pk=2)
>>> articulo.imagen
'articulo2.jpg'
>>> quit()
```

## Migrate para la autorizacion de usuarios

```sh
(./.env) python manage.py migrate
(./.env) python manage.py createsuperuser #admin:admin
```