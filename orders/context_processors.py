from .models import BuyingProduct

def korzina_info(request):
	session_key = request.session.session_key
	buying_products =  BuyingProduct.objects.filter(session_key = session_key, is_active = True)
	product_total_numb = buying_products.count()
	return locals()