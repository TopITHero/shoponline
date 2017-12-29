from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):
	model = ProductImage

class ProductAdmin(admin.ModelAdmin):

	inlines = [ProductImageInline]
	
	class Meta:
		model = Product

admin.site.register(Product,ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):

	class Meta:
		model = ProductImage

admin.site.register(ProductImage,ProductImageAdmin)

class CategoryAdmin(admin.ModelAdmin):

	class Meta:
		model = Category

admin.site.register(Category,CategoryAdmin)

