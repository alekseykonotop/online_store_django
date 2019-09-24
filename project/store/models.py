from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name', ]

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return f'/store/category/{self.pk}'


class Product(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    model = models.CharField(max_length=50, verbose_name='Модель')
    # title = models.CharField(max_length=150, verbose_name='Название продукта')
    disc = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-brand', '-model', ]

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolut_url(self):
        return f'/store/products/{self.pk}'


class Article(models.Model):

    title = models.CharField(max_length=350, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Контент')
    published = models.DateField(verbose_name='Дата публикации')
    # category = models.OneToOneField(Category, on_delete=models.CASCADE, verbose_name='Категория')
    products = models.ManyToManyField(Product, verbose_name='Товары')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published', ]

    def __str__(self):
        return self.title









