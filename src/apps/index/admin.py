from django.contrib import admin

from .models import Category, Product
# Register your models here.

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
    verbose_name_plural = "Add products"


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)