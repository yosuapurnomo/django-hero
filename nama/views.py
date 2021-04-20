from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import namaSerial
from .models import namaModel

# Create your views here.
class namaView(ListCreateAPIView,):
    queryset = namaModel.objects.all()
    serializer_class = namaSerial

    def get_success_headers(self, data):
    	try:
    		return {
			'success':data
			}
    	except (TypeError, KeyError):
    		return {
			'failed':"Create failed"
			}