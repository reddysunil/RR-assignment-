from django.db import models


# Create your models here.

class Users(models.Model):
    userid = models.IntegerField()
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

