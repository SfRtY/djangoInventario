from django.db import models
# Create your models here.
class Hardware(models.Model):
    codigoactivo = models.CharField(db_column='CodigoActivo', primary_key=True, max_length=12)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=30)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    empleadofinal = models.CharField(max_length=9)
    area = models.CharField(max_length=62)
    numeroserie = models.CharField(max_length=10)
    marca = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'hardware'

class Software(models.Model):
    codigoactivo = models.CharField(db_column='CodigoActivo', primary_key=True, max_length=12)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    version = models.CharField(db_column='version',max_length=8)
    licencia = models.CharField(db_column='licencia',max_length=2)
    tipoequipo = models.CharField(db_column='TipoEquipo', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software'

class Area(models.Model):
    codigoarea = models.CharField(db_column='codigoArea', primary_key=True, max_length=4)  # Field name made lowercase.
    nombrearea = models.CharField(db_column='nombreArea', max_length=62)  # Field name made lowercase.
    abreviatura = models.CharField(db_column='Abreviatura', max_length=19)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'area'

