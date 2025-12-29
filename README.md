
<h1 style="font-size: 3em; color: #FF0000;">•  PROYECTOS DE APIs </h1> 
<h1 style="font-size: 3em; color: #FF0000;">• PYTHON, JAVASCRIPT Y GO </h1> 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Go](https://img.shields.io/badge/Go-00ADD8?logo=Go&logoColor=white&style=for-the-badge)

![Javascript](https://shields.io/badge/JavaScript-F7DF1E?logo=JavaScript&logoColor=000&style=flat-square)


Luego de descargar git, Los comandos para acceder al repositorio son los siguientes.

```Terminal de comandos
git --version
git init
git clone https://github.com/guevaraStian/APIs.git
cd APIs
git push origin master
```
---------

<h2 style="font-size: 3em; color: #FF0000;">- PYTHON</h2> 


Los pasos para poner en ejecución son los siguientes.
Ir a la pagina web de Python y descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos.

```Pagina web
https://www.python.org/downloads/
```
Luego de tener instalado Python podemos ejecutar los siguientes comandos hasta llegar a la carpeta del proyecto y estando ahí ejecutamos los siguientes codigos.

```Terminal de comandos
cd    
python --version
pip --versión
pip install --upgrade pip
pip install flask fastapi uvicorn
python <Nombre_Proyecto.py>

```
Luego que el proyecto ya se este ejecutando se darán diferentes respuestas en consola o pestañas emergentes.

---------


PYTHON DJANGO API CRUD


Luego de crear la carpeta donde se va a crear la API con django .
procedemos a intalar el framework django.
```Terminal de comandos
pip install django djangorestframework
```
Creamos el proyecto con el siguiente comando.
```Terminal de comandos
django-admin startproject Api_Python_CRUD_Django
```
Luego de entrar a la carpeta, inicializamos la api en el servidor se da el siguiente starapp .
```Terminal de comandos
cd Api_Python_CRUD_Django
python manage.py startapp api
```
El servidor empieza a correr con el siguiente código.
```Terminal de comandos
python manage.py runserver
```
Estos 2 codigos sirven en caso de migracion de informacion a la base de datos.
```Terminal de comandos
python manage.py makemigrations
python manage.py migrate
```


-----------------------------
---------------------------

<h2 style="font-size: 3em; color: #FF0000;">- GO</h2> 





Los pasos para poner en ejecución son los siguientes
Ir a la pagina web de Python y descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de GO en la terminal de comandos

Windows
```Pagina web
https://go.dev/doc/install
```

Luego de tener instalado Python podemos ejecutar los siguientes comandos hasta llegar a la carpeta del proyecto y estando ahí ejecutamos los siguientes codigos

```Terminal de comandos
cd    
go version 
go get github.com/gorilla/mux
go run <Nombre_Proyecto.go>
go build


```
Luego que el proyecto ya se este ejecutando se darán diferentes respuestas en consola o pestañas emergentes


------------------


GO ECHO


Con los siguientes códigos se descargar el framework ECHO de Go

```Terminal de comandos
go mod init main
go get github.com/labstack/echo
```
------------------


GO GIN


Con los siguientes códigos se descargar el framework GIN de GO

```Terminal de comandos
go version
go mod init go-gin-crud
go get -u github.com/gin-gonic/gin
```




-----------------------------
---------------------------
<h2 style="font-size: 3em; color: #FF0000;">- JAVASCRIPT</h2> 







Los pasos para poner en ejecución son los siguientes Ir a la pagina web de JavaScript y descargarlo para tu sistema operativo, escoger la versión LTS y tambien escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos
```Pagina web
https://nodejs.org
```
Luego de descargar el ejecutable, dar click en el .msi y dar click en la opción siguiente

Verifica la instalación:

Abrir la terminal de comandos (Presiona Windows + R, escribe cmd y presiona Enter).
```Terminal de comandos
node -v
npm -v
```

Luego descargamos el repositorio, ingresamos a la carpeta descargada y ejecutamos cualquiera de los siguiente comando
```Terminal de comandos
node main.js
nodemon main.js
npm start
```









