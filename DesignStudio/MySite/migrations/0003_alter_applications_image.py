# Generated by Django 4.2.7 on 2023-11-02 12:51

import MySite.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_remove_applications_status_delete_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='image',
            field=models.ImageField(help_text='Разрешается формата файла только jpg, jpeg, png, bmp', upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), MySite.models.Applications.validate_image], verbose_name='Фотография'),
        ),
    ]
