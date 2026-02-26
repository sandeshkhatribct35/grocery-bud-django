from django.urls import path
from .views import home, delete_item

urlpatterns = [
    path("", home, name="home"),
    path("delete/<int:id>/", delete_item, name="delete"),
]