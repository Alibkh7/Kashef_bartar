from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    body1 = models.TextField(verbose_name='متن')
    body2 = models.TextField(verbose_name='متن اضافه', null=True, blank=True)
    image = models.ImageField(upload_to='images/services/main', verbose_name='تصویر اصلی')
    image1 = models.ImageField(upload_to='images/services/1', null=True, blank=True, verbose_name='تصویر متن 1', default='images/services/1/1-default.png')
    image2 = models.ImageField(upload_to='images/services/2', null=True, blank=True, verbose_name='تصویر متن 2', default='images/services/2/2-default.png')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'


    def __str__(self):
        return self.title


class Sample(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.CharField(max_length=200, verbose_name='معرفی مختصر')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='images/samples', verbose_name='تصویر')
    customer = models.CharField(max_length=100, verbose_name='مشتری')
    services = models.ManyToManyField(Service, related_name='samples', verbose_name='خدمات', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انجام پروژه')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'

    def __str__(self):
        return self.title


class SampleImage(models.Model):
    sample = models.ForeignKey(Sample, related_name='images', on_delete=models.CASCADE, verbose_name='نمونه کار')
    image = models.ImageField(upload_to='images/samples', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر متن نمونه کار'
        verbose_name_plural = 'تصاویر متن نمونه کار'
    def __str__(self):
        return f"تصویر برای {self.sample.title}"

