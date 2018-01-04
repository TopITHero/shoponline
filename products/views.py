from django.shortcuts import render 
from .models import ProductImage,Category,Product
# Create your views here.

def products(request):
	category = Category.objects.all()
	products = ProductImage.objects.filter(is_active = True, is_main = True)
	main = ProductImage.objects.filter(is_active = True, is_main = True)[:3]
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	print(request.session.session_key)
	return render(request, 'products.html', {'products':products,'category':category, 'main':main})


def detail(request,pk):	
	category = Category.objects.all()
	product = Product.objects.get(pk = pk)

	return render(request, 'product_detail.html',{ 'product': product,'category':category,})

def category_filter(request,c_id):
	category = Category.objects.all()
	products = ProductImage.objects.filter(is_active = True, is_main = True, category_id = c_id)
	main = ProductImage.objects.filter(is_active = True, is_main = True,category_id = c_id)[:3]
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	print(request.session.session_key)
	return render(request, 'products.html', {'products':products,'category':category, 'main':main})

