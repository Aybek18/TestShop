from django.urls import path

from products.views import ProductListAPIView, ProductExcelAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="products"),
    path("export/", ProductExcelAPIView.as_view(), name="product_excel")
]
