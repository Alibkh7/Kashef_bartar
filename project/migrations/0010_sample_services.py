# Generated by Django 5.1 on 2024-10-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_sample_options_alter_sampleimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='samples', to='project.service', verbose_name='خدمات'),
        ),
    ]
