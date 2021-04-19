from rest_framework import serializers
from .models import namaModel

class namaSerial(serializers.ModelSerializer):
    class Meta:
        model = namaModel
        fields = ['id','nama']
