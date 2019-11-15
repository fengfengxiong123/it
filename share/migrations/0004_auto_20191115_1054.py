# Generated by Django 2.1.4 on 2019-11-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20191114_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='dot',
            name='labelfive',
            field=models.CharField(choices=[('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署')], max_length=10, null=True, verbose_name='标签五'),
        ),
        migrations.AddField(
            model_name='dot',
            name='labelfour',
            field=models.CharField(choices=[('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署')], max_length=10, null=True, verbose_name='标签四'),
        ),
        migrations.AddField(
            model_name='dot',
            name='labelone',
            field=models.CharField(choices=[('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署')], max_length=10, null=True, verbose_name='标签一'),
        ),
        migrations.AddField(
            model_name='dot',
            name='labelthree',
            field=models.CharField(choices=[('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署')], max_length=10, null=True, verbose_name='标签三'),
        ),
        migrations.AddField(
            model_name='dot',
            name='labeltwo',
            field=models.CharField(choices=[('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署')], max_length=10, null=True, verbose_name='标签二'),
        ),
    ]