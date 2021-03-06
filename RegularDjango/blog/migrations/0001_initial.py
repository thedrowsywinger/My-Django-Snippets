# Generated by Django 3.1.7 on 2021-04-08 06:38

import blog.models
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUploaderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('abstract', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('header_image', models.ImageField(upload_to=blog.models.blog_images_path)),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('keywords', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
