from django.shortcuts import render, redirect
from .forms import ProductAddingForm
from .models import Product
# Create your views here.

def index(request):
   if request.method == "GET":
      form = ProductAddingForm()
   elif request.method == "POST":
      form = ProductAddingForm(request.POST)
      if form.is_valid():
         id = form.cleaned_data["id"]
         name = form.cleaned_data["name"]
         material = form.cleaned_data["material"]
         price = form.cleaned_data["price"]
         quantity = form.cleaned_data["quantity"]
         _, was_created = Product.objects.get_or_create(id=id, name=name, material=material, price=price, quantity=quantity)
         if was_created:
            return redirect("add-success")
         else:
            return redirect("add-failure")

   return render(request, "products/index.html", {
      "form": form
   })

def products(request):
   return render(request, "products/products/products.html")