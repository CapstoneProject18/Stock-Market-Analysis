from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=244)
    description = models.TextField()
 
    def __unicode__(self):
        return self.name

    def __str__(self):
    	return self.name