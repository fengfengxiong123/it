# Generated by Django 2.1.4 on 2019-11-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='中文名'),
        ),
    ]
