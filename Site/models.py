from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    material = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
