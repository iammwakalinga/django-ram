from django.contrib import admin
from .models import Soda

admin.site.register(Soda)

def _str_(self):
    return self.name + '' + self.description