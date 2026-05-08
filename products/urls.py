from django.urls import path
from .views import products, add_success, add_failure

urlpatterns = [
   path("products/", products, name="products"),
   path("products/add-success", add_success, name="add-success"),
   path("products/add-failure", add_failure, name="add-failure"),
]