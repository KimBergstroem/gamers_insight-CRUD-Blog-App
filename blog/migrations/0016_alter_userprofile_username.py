# Generated by Django 3.2.21 on 2023-09-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20230930_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='User', max_length=15),
        ),
    ]