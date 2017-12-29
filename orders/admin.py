from django.contrib import admin
from .models import *
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
	model = ProductInOrder

class ProductInOrderAdmin(admin.ModelAdmin):

	class Meta:
		model = ProductInOrder

admin.site.register(ProductInOrder,ProductInOrderAdmin)

class StatusAdmin(admin.ModelAdmin):

	class Meta:
		model = Status

admin.site.register(Status,StatusAdmin)

class OrderAdmin(admin.ModelAdmin):

	inlines = [ProductInOrderInline]
	class Meta:
		model = Order

admin.site.register(Order,OrderAdmin)		



class ProductInBacketAdmin(admin.ModelAdmin):

	class Meta:
		model = ProductInBacket

admin.site.register(ProductInBacket,ProductInBacketAdmin)