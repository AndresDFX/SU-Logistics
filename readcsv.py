import csv
import datetime

from users.models import User

with open('BD prueba.csv') as csvdata:
    reader = csv.DictReader(csvdata)
    for row in reader:
        if row['Ventas 2019'].strip():
            a = row['Ventas 2019'][1:]
            sale = a.replace('.','') 
        else:
            sale = '0'
        
        User.objects.create_user(
            row['Email'], 
            row['Contraseña'],
            first_name = row['Nombres'],
            last_name1 = row['Apellido 1'],
            last_name2 = row['Apellido 2'],
            document_id = row['Cédula'],
            birth_date = datetime.datetime.strptime(row['Fecha de Nacimiento'], "%d/%m/%Y").strftime("%Y-%m-%d"), 
            gender = row['Género'],
            admission_date = datetime.datetime.strptime(row['Fecha de Ingreso'], "%d/%m/%Y").strftime("%Y-%m-%d"),
            id_employee = row['Número de empleado'],
            position = row['Cargo'],
            leader = row['Jefe'],
            zone = row['Zona'],
            image = row['Imágen'],
            phone = row['Celular'],
            city = row['Municipio'],
            department = row['Departamento'],
            sales = int(sale),
        )