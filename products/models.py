from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added = models.DateTimeField(auto_created=True)
    desc= models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.title