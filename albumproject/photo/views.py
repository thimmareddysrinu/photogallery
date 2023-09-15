from django.shortcuts import render
from .models import products


# Create your views here.
def images(request):
 
  product=products.objects.all()
  context={
   'product':product
  }
  return render(request,'home.html',context)