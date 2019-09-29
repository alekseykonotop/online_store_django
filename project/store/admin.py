from django.contrib import admin
from .models import Category, Brand, Article, Product
from .forms import ArticleAdminForm

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', )
    search_fields = ('name', 'parent', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('is_active', 'published', 'title', 'content', 'get_products', )
    list_display_links = ('title', )
    search_fields = ('is_active', 'title', 'content', 'published', )

    def get_products(self, obj):
        return "\n".join([f'{p.brand} {p.model}' for p in obj.products.all()])

    get_products.short_description = 'Выбранные товары'


admin.site.register(Article, ArticleAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'description', 'price', 'category', 'stock', 'available', )
    list_display_links = ('brand', 'model', 'description', )
    search_fields = ('brand', 'model', 'description', 'price', 'category', )
    prepopulated_fields = {'slug': ('brand', 'model', )}
    list_editable = ('price', 'stock', 'available', )


admin.site.register(Product, ProductAdmin)
