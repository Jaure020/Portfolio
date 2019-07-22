from django.db import models

# Create your models here.

class LinkedIn(models.Model):
    title= models.CharField(max_length=255)
    pub_date= models.DateTimeField()
    body= models.TextField()
    image= models.ImageField(upload_to='images/')