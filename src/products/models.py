from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    tags = models.ManyToManyField(Tag, related_name="product_tags", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
