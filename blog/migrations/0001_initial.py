# Generated by Django 5.1 on 2024-11-01 12:15

import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='عنوان')),
                ('body', froala_editor.fields.FroalaField(verbose_name='متن')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='تصویر')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ('-created',),
            },
        ),
    ]
