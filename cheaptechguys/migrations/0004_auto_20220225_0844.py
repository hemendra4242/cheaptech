# Generated by Django 3.2.3 on 2022-02-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheaptechguys', '0003_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='After_price',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(max_length=200),
        ),
    ]
