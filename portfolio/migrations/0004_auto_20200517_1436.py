# Generated by Django 3.0.5 on 2020-05-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200516_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='demolink',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='portfolios',
            name='image',
            field=models.ImageField(default='', upload_to='projects/'),
        ),
    ]
