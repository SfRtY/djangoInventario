from rest_framework import viewsets
from .serializers import HardwareSerializer,SoftwareSerializer,AreaSerializer
from .models import Hardware,Software,Area
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'Hardware/CH.html')

def FormHardware(request):
    queryset=Area.objects.all()
    return render(request,'Hardware/CH.html',{'query':queryset})

class HardwareView(viewsets.ModelViewSet):
    serializer_class=HardwareSerializer
    queryset=Hardware.objects.all()

class SoftwareView(viewsets.ModelViewSet):
    serializer_class=SoftwareSerializer
    queryset=Software.objects.all()

class AreaView(viewsets.ModelViewSet):
    serializer_class=AreaSerializer
    queryset=Area.objects.all()
