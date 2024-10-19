# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator



class CarMake(models.Model):
    name = models.CharField(max_length=50 , null=False)
    description = models.CharField(max_length=200 , null=False)

    def __str__(self):
        return self.Name


class CarModel(models.Model):
  name = models.CharField(max_length=50, name=False)
  year = models.IntegerField(default=2023 , validators=[
     MaxValueValidator(2023) ,
     MinValueValidator(2015)
  ])
  car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) 
  CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
  type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

  def __str__(self):
     return self.Name
