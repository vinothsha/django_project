# Generated by Django 3.2.7 on 2021-10-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('indoor', 'indoor'), ('outdoor', 'outdoor')], max_length=100, null=True),
        ),
    ]
