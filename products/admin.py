from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):
	
	
	model = ProductImage

class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields if field.name != "id"]

	inlines = [ProductImageInline]
	
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields if field.name != "id"]

	class Meta:
		model = ProductImage

admin.site.register(ProductImage,ProductImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Category._meta.fields if field.name != "id"]

	class Meta:
		model = Category

admin.site.register(Category,CategoryAdmin)

