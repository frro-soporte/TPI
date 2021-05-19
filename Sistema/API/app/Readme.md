# API
## Cinear backend api

![Python](https://img.shields.io/badge/Python-v^3.9.5-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v2.0.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)

>Esta guia esta hecha para windows

## Instalación

Cinear requiere [Python 3.9.5](https://www.python.org/) para correr.
Estando en la carpeta Sistema/API Correr 
```sh
python -m venv venv
```
Va a generar una carpeta llamada venv que contenga el ambiente virtual.
Navegar hasta la carpeta Sistema/API/venv/Scripts y ejecutar el siguiente comando
```sh
activate
```
Navegar hasta la carpeta Sistema/API/app y ejecutar.
```sh
python -m pip install -r requirements.txt
```
ese comando va a instalar todas las dependecias necesarias para el proyecto.
## Ejecución
Navegar hasta la carpeta Sistema/API/app y ejecutar.
```sh
python wsgi.py
```
## License
MIT
