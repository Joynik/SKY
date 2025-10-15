from django.contrib import admin

from .models import Category, Color, Product, ProductColor, ProductImage, ProductSize, Size


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ["category"]
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline, ProductSizeInline, ProductColorInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ColorAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
