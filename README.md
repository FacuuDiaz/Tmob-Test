# Tmob-Test

Sistema de evaluacion de la empresa T-mob


#### Version de python usada
> `python 3.10.2`

#### Creacion y Activacion del entorno virtual
Para crear ejecutamos el siguiente comando en la terminal:
`virtualenv env`
En caso de no tener virtualenv instalado en el sistema se instala con el siguiente comando: 
- `pip install virtualenv`

Una vez creado el ambiente se autogenera una carpeta con el nombre asignado (en este caso env).
Para activarlo ejecutamos el siguiente comando:
- `source env/bin/activate`

#### Instalación de requerimientos
> `pip install -r requirements.txt`

#### Creación de superusuario
Dentro de la carpeta de `Tmob` ejecutar el siguiente comando 
> `python manage.py createsuperuser`

Estas credenciales van a ser las mismas para entrar en el `<url>/admin` para la administracion del sistema.

Para ejecutar el sistema:
> `python manage.py runserver`

previamente se tiene que crear un archivo `.env` dentro de la carpeta main del proyecto (`Tmob/Tmob`) con las credenciales de la base de datos. Hay un ejemplo de los datos posibles que puede tener llamado `env.example`, en caso de querer usar el mismo archivo, directamente saque la extencion __`.example`__ del mismo y cree una base de datos con las mismas caracteristicas delladas en el archivo

#### Database
> version: `10.5.13-MariaDB`

#### Django
 > version: `2.2.28`
