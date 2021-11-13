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

Instalar los requerimientos necesarios
```bash
pip install -r SU-Logistics/requirements.txt
```
Creamos la base de datos con el nombre, de acuerdo a la configuracion del archivo [settings.py](./logistics/logistics/settings.py)

Ejecutamos las migraciones

``` bash
python manage.py SU-Logistics/makemigrations
python manage.py SU-Logistics/migrate
```

Para cargar la base de datos desde el archivo CSV

```bash
python SU-Logistics/manage.py shell_plus < SU-Logistics/readcsv.py
```

Para ejecutar el servidor de manera local por el puerto 8000 
```
python SU-Logistics/manage.py runserver 8000
```

