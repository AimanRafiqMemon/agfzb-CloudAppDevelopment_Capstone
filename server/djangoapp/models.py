from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model 
class CarMake(models.Model):
 Name = models.CharField(max_length=30)
 Description = models.CharField(max_length=300)
# - Any other fields you would like to include in car make model
 def __str__(self):
    return self.Name


# <HINT> Create a Car Model model 
class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
 Car_Make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
 Name = models.CharField(max_length=30)
 Dealer_id = models.IntegerField()
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
 Type = models.CharField(max_length=30, choices=(('SUV', 'SUV'),('Sedan', 'Sedan'),('Wagon', 'Wagon')), default='Sedan')
# - Year (DateField)
 Year = models.DateField()
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
 def __str__(self):
        return self.Name



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

