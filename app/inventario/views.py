from rest_framework import viewsets,mixins
from .serializers import HardwareSerializer,SoftwareSerializer,AreaSerializer,EmpleadoSerializer
from .models import Hardware,Software,Area,Empleado
from django.shortcuts import render, get_object_or_404
# Create your views here.
def index(request):
    return render(request,'Hardware/CH.html')

def prueba(request):
    return render(request,'Hardware/prueba.html')

def EmpleadoDetail(request, idarea):
    queryset1=Area.objects.all()
    queryset2=Empleado.objects.filter(id_area=idarea)
    return render(request,'Hardware/CH.html',{'query1':queryset1,'query2':queryset2})

def FormHardware(request):
    queryset=Area.objects.all()
    return render(request,'Hardware/CH.html',{'query':queryset})

class HardwareView(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class=HardwareSerializer
    queryset=Hardware.objects.all()
    lookup_field='codigoactivo'

class SoftwareView(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class=SoftwareSerializer
    queryset=Software.objects.all()

class AreaView(viewsets.ModelViewSet):
    serializer_class=AreaSerializer
    queryset=Area.objects.all()






