# Generated by Django 2.2.10 on 2020-05-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200521_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
