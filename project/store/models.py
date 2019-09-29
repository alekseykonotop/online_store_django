from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, verbose_name='Родительская категория')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return f'/store/category/{self.pk}'


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Бренд')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return f'/store/brand/{self.pk}'


def image_forlder(instance, filename):
    filename = f"{instance.slug}.{filename.split('.')[1]}"
    return f'images/products/{instance.slug}/{filename}'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', blank=True)
    model = models.CharField(max_length=100, verbose_name='Модель')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    image = models.ImageField(null=True, blank=True, upload_to=image_forlder, verbose_name='Изображение')
    stock = models.PositiveIntegerField(verbose_name='Остатки')
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['brand', 'model', ]
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolut_url(self):
        return f'/store/products/detail/{self.pk}'


class Article(models.Model):

    title = models.CharField(max_length=350, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Контент')
    published = models.DateField(verbose_name='Дата публикации')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['is_active', '-published', 'title', ]

    def __str__(self):
        return self.title









