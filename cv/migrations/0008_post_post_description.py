# Generated by Django 4.0.6 on 2022-07-16 05:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
