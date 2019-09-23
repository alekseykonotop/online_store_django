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
    list_display = ('title', 'content', 'published', 'category', )
    list_display_links = ('title', )
    search_fields = ('title', 'content', 'category',)


admin.site.register(Article, ArticleAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'disc', 'price', 'category', 'article', )
    list_display_links = ('brand', 'model', 'disc', 'price', 'category', 'article', )
    search_fields = ('brand', 'model', 'disc', 'price', 'category', 'article', )


admin.site.register(Product, ProductAdmin)
