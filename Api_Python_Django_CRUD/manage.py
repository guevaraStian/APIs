# Api_Python_CRUD_Django
# Luego de crear la carpeta donde se va a crear la API con django 
# procedemos a intalar el framework django
# pip install django djangorestframework
# Creamos el proyecto con el siguiente comando
# django-admin startproject Api_Python_CRUD_Django
# Luego de entrar a la carpeta, inicializamos la api en el servidor se da el siguiente starapp 
# cd Api_Python_CRUD_Django
# python manage.py startapp api
# El servidor empieza a correr con el siguiente codigo
# python manage.py runserver
# Estos 2 codigos sirven en caso de migracion de informacion a la base de datos
# python manage.py makemigrations
# python manage.py migrate

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Api_Python_CRUD_Django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Aparentemente no esta instalado django "
            "Depronto no estan los paths en PYTHONPATH"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
