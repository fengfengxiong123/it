# Generated by Django 2.1.4 on 2019-11-18 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20191118_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dot',
            old_name='labeltwo',
            new_name='backend',
        ),
        migrations.RenameField(
            model_name='dot',
            old_name='labelfour',
            new_name='dev',
        ),
        migrations.RenameField(
            model_name='dot',
            old_name='labelone',
            new_name='font',
        ),
        migrations.RenameField(
            model_name='dot',
            old_name='labelfive',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='dot',
            old_name='labelthree',
            new_name='server',
        ),
    ]
