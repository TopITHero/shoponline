from django.shortcuts import render 
from .models import ProductImage,Category,Product
# Create your views here.

def products(request):
	category = Category.objects.all()
	products = ProductImage.objects.filter(is_active = True, is_main = True)
	main = ProductImage.objects.filter(is_active = True, is_main = True)[:3]
	print("works")
	return render(request, 'products.html', {'products':products,'category':category, 'main':main})


def detail(request,pk):	
	category = Category.objects.all()
	product = Product.objects.get(pk = pk)
	print("works")
	return render(request, 'product_detail.html',{ 'product': product,'category':category,})

