# Generated by Django 4.0.6 on 2022-07-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/uploads/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='transcription',
            field=models.FileField(null=True, upload_to='media/uploads/'),
        ),
    ]
