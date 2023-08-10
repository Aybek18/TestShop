from django.db import migrations

categories = [{"name": "sport"}, {"name": "swimming"}, {"name": "hiking"}]
tags = [{"name": "young"}, {"name": "female"}, {"name": "male"}, {"name": "kids"}]
products = [{
    "name": "Example Product 1",
    "description": "This is the first example product.",
    "price": 29.99,
    "category_id": 1,
    "tags": [1, 2, 3]
}, {
    "name": "Example Product 2",
    "description": "This is the second example product.",
    "price": 39.99,
    "category_id": 2,
    "tags": [2, 3, 4]
},
    {
        "name": "Example Product 3",
        "description": "This is the third example product.",
        "price": 49.99,
        "category_id": 3,
        "tags": [3, 4]
    },
]


def import_data(app, _):
    Category = app.get_model("products", "Category")
    Tags = app.get_model("products", "Tag")
    Product = app.get_model("products", "Product")

    for category in categories:
        Category.objects.create(name=category["name"])
    for tag in tags:
        Tags.objects.create(name=tag["name"])
    for product in products:
        instance = Product.objects.create(name=product["name"], description=product["description"],
                                          price=product["price"], category_id=product["category_id"])
        instance.tags.add(*product["tags"])


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_data, migrations.RunPython.noop)]
