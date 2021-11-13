from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from .managers import UserManager

LEADER_POSITION = 'Ejecutivo Comercial'

class User(PermissionsMixin, AbstractBaseUser):
    
    first_name = models.CharField("Nombres", max_length=50)
    last_name1 = models.CharField("Primer apellido", max_length=50)
    last_name2 = models.CharField("Segundo apellido", max_length=50)
    document_id = models.CharField("Cédula", max_length=255, unique=True)
    birth_date = models.DateField("Fecha de nacimiento", auto_now=False, auto_now_add=False, blank=True, null=True)
    gender = models.CharField("Género", max_length=50)
    admission_date = models.DateField("Fecha de ingreso", auto_now=False, auto_now_add=False, blank=True, null=True)
    department = models.CharField("Departamento", max_length=50)
    sales = models.IntegerField(blank=True, null=True)
    email = models.EmailField("Correo elèctronico", max_length=254, unique=True)
    image = models.URLField("Imagen", max_length=200) 
    phone = models.CharField("Telefono", max_length=15)
    id_employee = models.CharField("Nùmero de empleado", max_length=255, unique=True)
    position = models.CharField("Cargo", max_length=50)
    leader = models.CharField("Jefe", max_length=50)
    zone = models.CharField("Zona", max_length=50)
    city = models.CharField("Municipio", max_length=50)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']
    

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name1} {self.last_name2}'
    
    def region(self) -> str:
        return f'{self.city}, {self.department}'

    def get_sales(self) -> int:
        '''
            Calcula las ventas de un usuario, en caso tal tenga subalternos retorna la suma de las ventas de ellos

            Parametros:
                self: El objeto usuario que será representado por una cadena de caracteres.

            Retorno:
                Integer (int): Valor que representa las ventas del usuario o sus subalternos
        '''
        if self.position == LEADER_POSITION:
            return self.sales
        else:
            sales = 0
            subalternos = User.objects.filter(leader=self.id_employee)
            for subalterno in subalternos:
                sales = sales + subalterno.get_sales()
            return sales
    
    def format_sales(self) -> str:
        '''
            Formatea un numero usando como saparador de miles la ,

            Parametros:
                self: El objeto usuario que será representado por una cadena de caracteres.

            Retorno:
                String (str): Valor que representa las ventas del usuario separados por ,
        '''
        return str('{0:,}'.format(self.get_sales()))
    
    def __str__(self):
        return self.full_name()