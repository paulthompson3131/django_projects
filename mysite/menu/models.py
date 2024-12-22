from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=128)
    heading = models.CharField(max_length=128)
    parent = models.CharField(max_length=128)

class MenuContent(models.Model):
    name = models.ForeignKey(Menu, on_delete=models.CASCADE) 
    url_to_call = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
