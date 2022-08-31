
from rest_framework.serializers import ModelSerializer
from .models import category,Book,Product

class categoryserializer(ModelSerializer):
    class Meta:
        fields=(
            "id",
            "title",
        )
        model=category
class Bookserializer(ModelSerializer):

    class Meta:
        fields=(
          "id",
          "title",
          "category",
          'author',
          "isbn",
          "price",
          "stock",
          "description",
          "imageurl",
          "status",
          "date_created",

        )
        model=Book

class Productserializer(ModelSerializer):
    class Meta:
        fields=(
         "id",
         "product_tag",
         "name",
         "category",
         "price",
         "stock",
         "imageurl",
         "status",
        "date_created",

        )

        model=Product