from django.db import models

# Create your models here.
class namaModel(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama