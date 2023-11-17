from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"Category: {self.name}"


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Product:{self.title}"

