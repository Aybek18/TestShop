from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from products.models import Product
from products.serializers import ProductSerializer


@receiver(post_save, sender=Product)
def update_cached_products(sender, instance, created, **kwargs) -> None:
    # Signal for updating cached product list
    cached_products = cache.get("cached_products")
    if cached_products:
        cached_products = [product for product in cached_products if product['id'] != instance.id]
        if created:
            cached_products.insert(0, ProductSerializer(instance).data)
        cached_products.insert(instance.id + 1, ProductSerializer(instance).data)
        cache.set("cached_products", cached_products, timeout=settings.CACHE_EXPIRATION_SECONDS)
