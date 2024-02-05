from django.contrib import admin
from django.urls import path
from it_digi import views
# from parking import views as ca
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('lg/',views.login ,name="loginpage"),
    path('rg/', views.register , name="registrationpage"),
    path('pg/',views.python, name="pythonpage"),
    path('jg/',views.java, name="javapage"),
    path('cg/',views.c, name="cpage"),
    path('ac/',views.ac, name="addcarpage"),
    path('car/', views.car),
    path('fetch/',views.fetch),
    path('sh/',views.show,name="search"),
]