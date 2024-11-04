from django.db import models
from django.utils.html import format_html
from froala_editor.fields import FroalaField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    body = FroalaField(verbose_name='متن')
    image = models.ImageField(upload_to="images/articles", verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.body[:20]}"

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
    show_image.short_description = "تصویر"


    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
