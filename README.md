# SU Logistics

---
## Construido con
+ [Django 3.2.9](https://www.djangoproject.com/)
+ [PostgreSQL 14.1](https://www.postgresql.org/)

---
## Instalacion

Descargar el repositorio con mediante la linea de comandos 
```bash
git clone https://github.com/AndresDFX/SU-Logistics.git
```

Ingresamos a la carpeta del proyecto 
```bash
cd SU-Logistics/logistics
```

Instalar los requerimientos necesarios
```bash
pip install -r requirements.txt
```
Creamos la base de datos con el nombre, de acuerdo a la configuracion del archivo [settings.py](./logistics/logistics/settings.py)

Ejecutamos las migraciones

``` bash
python manage.py makemigrations
python manage.py migrate
```

Para cargar la base de datos desde el archivo CSV

```bash
python manage.py shell < readcsv.py
```

Para ejecutar el servidor de manera local por el puerto 8000 
```
python manage.py runserver 8000
```

