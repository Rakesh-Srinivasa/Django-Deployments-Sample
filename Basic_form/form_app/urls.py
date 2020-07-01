from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.index, name= 'index'),
    path('', views.formpage, name= 'formpage'),
]
