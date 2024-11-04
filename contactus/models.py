from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    meli_code = models.CharField(max_length=10, verbose_name='کد ملی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    message = models.TextField(verbose_name='شرح درخواست')

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'مخاطب'
        verbose_name_plural = 'مخاطبان'


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    career = models.CharField(max_length=100, verbose_name='عنوان شغلی')
    image = models.ImageField(upload_to="images/teamprof", verbose_name='تصویر')
    text = models.CharField(max_length=200, verbose_name='توضیحات')

    def __str__(self):
        return f"{self.name} - {self.career}"

    class Meta:
        verbose_name = 'تیم'
        verbose_name_plural = 'اعضای تیم'