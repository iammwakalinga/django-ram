from unicodedata import name
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[

    path('',views.index,name="index"),

    path('signup',views.signup,name="signup"),
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),
    path('activate/<uid64>/<token>',views.activate,name="activate"),
    
    
]


urlpatterns += staticfiles_urlpatterns()

