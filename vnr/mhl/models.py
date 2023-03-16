from django.db import models
class chd(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    qln = models.CharField(max_length=50)
    mob = models.IntegerField()
    img = models.CharField(max_length=850)

# Create your models here.
