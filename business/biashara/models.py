
from tabnanny import verbose
from django.db import models

# Create your models here.

class category(models.Model):
    title=models.CharField(max_length=255)


    class Meta:
          verbose_name_plural='categories'

    def _str_(self):
        return self.title




class Book(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(category,related_name='books',on_delete=models.CASCADE)
    author=models.CharField(max_length=90,default='Raidin')
    isbn=models.CharField(max_length=18)
    pages=models.IntegerField()
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    imageurl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)


    class Meta:
      ordering =('date_created',)

    def _str_(self):
            return self.title

class Product(models.Model):
    product_tag=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    category = models.ForeignKey(category,related_name='products',on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()
    imageurl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
          ordering =('date_created',)

    def _str_(self):
            return "()()".format(self.product_tag, self.name)

    
