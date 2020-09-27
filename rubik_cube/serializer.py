from rest_framework import serializers
from .models import Cube

class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('solver','size','best_time','worst_time')
        model = Cube
        
