# Generated by Django 3.2.21 on 2023-09-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230917_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Unspecified', max_length=200),
        ),
    ]