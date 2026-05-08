from django import forms

class ProductAddingForm(forms.Form):
   id = forms.IntegerField(label="Enter product ID:", max_value=100)
   name = forms.CharField(label="Enter product name:", max_length=100)
   material = forms.CharField(label="Enter product material:", max_length=100)
   price = forms.DecimalField(label="Enter product price:", decimal_places=2, max_digits=10)
   quantity = forms.IntegerField(label="Enter product quantity:")