from django.contrib import admin
from .models import Category, Article, Product
from .forms import ArticleAdminForm

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'content', 'published', 'get_products', )
    list_display_links = ('title', )
    search_fields = ('title', 'content', )

    def get_products(self, obj):
        return "\n".join([f'{p.brand} {p.model}' for p in obj.products.all()])

    get_products.short_description = 'Выбранные товары'


admin.site.register(Article, ArticleAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'disc', 'price', 'category', )
    list_display_links = ('brand', 'model', 'disc', 'price', 'category', )
    search_fields = ('brand', 'model', 'disc', 'price', 'category', )


admin.site.register(Product, ProductAdmin)
