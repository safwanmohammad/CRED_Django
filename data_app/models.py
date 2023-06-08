from django.db import models

# Create your models here.

class datas(models.Model):
    SL_NO = models.IntegerField()
    ITEM_NAME = models.CharField(max_length=200)
    DESCRIPTION = models.TextField(max_length=300)

    def __str__(self):
        return self.ITEM_NAME

