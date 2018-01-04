from django.shortcuts import render,redirect ,get_object_or_404, render_to_response
from django.http import JsonResponse
# Create your views here.

from .models import BuyingProduct

def buying(request):
	return_dict = dict()
	session_key = request.session.session_key
	data = request.POST
	product_id = data.get("product_id")
	numb = data.get("numb")
	delete_p = data.get("delete")

	if delete_p == True:
		pass
	else:
		
		new_product, created = BuyingProduct.objects.get_or_create(session_key = session_key, 
			product_id = product_id, defaults = {"numb": numb})
	

		if not created:
			new_product.numb += int(numb)
			print(new_product.numb)
			new_product.save(force_update = True)

		buying_products =  BuyingProduct.objects.filter(session_key = session_key, is_active = True)
		product_total_numb = buying_products.count()


	return render_to_response("korzina_list.html", {'buying_products':buying_products, 'product_total_numb':product_total_numb})

def delete_product(request,pk):
	p = get_object_or_404(BuyingProduct, pk = pk)
	p.delete()
	session_key = request.session.session_key
	buying_products =  BuyingProduct.objects.filter(session_key = session_key, is_active = True)
	product_total_numb = buying_products.count()
	return render_to_response('korzina_list.html', {'buying_products':buying_products,
													'product_total_numb':product_total_numb})

