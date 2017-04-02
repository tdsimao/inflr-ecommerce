from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sold_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases', null=True, default=None)

    def for_sale(self):
        return self.sold_to is None
