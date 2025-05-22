from models import *
from rest_framework import serializers

class CondominiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominium
        fields = '__all__'
        
        
class BlocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloc
        fields = '__all__'
        
        
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        
        
class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = '__all__'
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'