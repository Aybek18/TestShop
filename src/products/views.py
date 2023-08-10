from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from products.services import ProductExcelService


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().select_related("category").prefetch_related("tags")
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        cached_products = cache.get("cached_products")
        if cached_products is not None:
            return Response(cached_products, status=status.HTTP_200_OK)

        serializer = ProductSerializer(self.get_queryset(), many=True)
        cache.set("cached_products", serializer.data, timeout=settings.CACHE_EXPIRATION_SECONDS)
        return Response(serializer.data)


class ProductExcelAPIView(RetrieveAPIView):
    queryset = Product.objects.all().select_related("category").prefetch_related("tags")

    def retrieve(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
        ProductExcelService.generate_excel_file(queryset, response)
        return response
