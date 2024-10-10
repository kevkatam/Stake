from django.db import models

# Create your models herei.
class Group(models.Model):
    """ model representing group table"""
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    class Meta:
        unique_together = (('name', 'location'))

    def __str__(self):
        """ string representation of the model """
        return f'{self.name} - {self.location}'
