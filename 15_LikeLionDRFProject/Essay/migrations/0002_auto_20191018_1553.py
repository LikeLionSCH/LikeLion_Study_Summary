# Generated by Django 2.1.8 on 2019-10-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Essay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
