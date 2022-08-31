from unicodedata import name
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[

  path('drinks/', views.drink_list),
]  
    
    



urlpatterns += staticfiles_urlpatterns()
