from django.shortcuts import render
from serializers import *
from models import *
from rest_framework import viewsets, status

class CondominiumViewSet(viewsets.ModelViewSet):
    queryset = Condominium.objects.all()
    serializer_class = CondominiumSerializer
    

class BlocViewSet(viewsets.ModelViewSet):
    queryset = Bloc.objects.all()
    serializer_class = BlocSerializer
    

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    
class WarningViewSet(viewsets.ModelViewSet):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer
    
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
