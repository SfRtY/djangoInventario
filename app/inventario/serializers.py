from rest_framework import serializers
from .models import Hardware,Software,Area,Empleado

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hardware
        fields=('codigoactivo','descripcion','modelo','estado','empleadofinal','area','numeroserie','marca')

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Software
        fields=('codigoactivo','nombre','version','licencia','tipoequipo')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields=('codigoarea','nombrearea','abreviatura')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=('dni','id_area','nombre_empleado')
