# Generated by Django 2.1.4 on 2019-11-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dot',
            name='labelfive',
            field=models.BooleanField(default=True, verbose_name='标签五'),
        ),
        migrations.AlterField(
            model_name='dot',
            name='labelfour',
            field=models.BooleanField(default=True, verbose_name='标签四'),
        ),
        migrations.AlterField(
            model_name='dot',
            name='labelone',
            field=models.BooleanField(default=True, verbose_name='标签一'),
        ),
        migrations.AlterField(
            model_name='dot',
            name='labelthree',
            field=models.BooleanField(default=True, verbose_name='标签三'),
        ),
        migrations.AlterField(
            model_name='dot',
            name='labeltwo',
            field=models.BooleanField(default=True, verbose_name='标签二'),
        ),
    ]
