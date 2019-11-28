from django.urls import path
from article import views

urlpatterns = [
    path('ver_post/<int:id>', views.ver_post , name="ver_post"),
]


