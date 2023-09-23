from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    expiration_date = models.DateField()
    # Add more fields as needed

class Donor(models.Model):
    name = models.CharField(max_length=255)
    # Add more fields as needed

class CollectionEvent(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    food_items = models.ManyToManyField(FoodItem)
    collection_date = models.DateTimeField()
    # Add more fields as needed