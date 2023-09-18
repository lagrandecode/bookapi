from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=250)
    number_pages = models.IntegerField()
    quantity = models.PositiveIntegerField()
    publish_date = models.DateField()

    def __str__(self):
        return self.name
     ///////////



