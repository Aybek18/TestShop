from typing import List

from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name")
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category_name",
            "price",
            "created_at",
            "tags"
        )

    def get_tags(self, obj) -> List[str]:
        return list(tag.name for tag in obj.tags.all())
