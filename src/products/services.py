from typing import List

from django.http import HttpResponse
from openpyxl.workbook import Workbook

from products.models import Product


class ProductExcelService:
    @classmethod
    def generate_excel_file(cls, products: List[Product], response: HttpResponse) -> None:
        workbook = Workbook()
        worksheet = workbook.active
        headers = [field.name for field in Product._meta.get_fields()]
        worksheet.append(headers)

        for product in products:
            tags = ", ".join([str(value) for value in product.tags.all()])

            row = [product.id, product.created_at, product.name, product.description, product.price,
                   product.category.name, tags]
            worksheet.append(row)
        workbook.save(response)
