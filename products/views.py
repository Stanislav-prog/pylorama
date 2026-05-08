from django.shortcuts import render, redirect
from .forms import ProductAddingForm
from .models import Product
# Create your views here.

def index(request):
   try:
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
            Product.objects.get_or_create(id=id, name=name, material=material, price=price, quantity=quantity)
            return redirect("add-success")
         
   except Exception as exc:
      return redirect("add-failure")

   return render(request, "products/index.html", {
      "form": form
   })

def products(request):
   products = Product.objects.all()
   field_names = [f.name for f in Product._meta.get_fields()]

   return render(request, "products/products/products.html", {
      "table_headers": field_names,
      "products": products
   })

def add_success(request):
   return render(request, "products/add-results/add-success.html")

def add_failure(request):
   return render(request, "products/add-results/add-failure.html")