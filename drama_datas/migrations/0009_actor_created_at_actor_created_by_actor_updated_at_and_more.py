# Generated by Django 4.0.4 on 2023-01-07 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drama_datas', '0008_dramadata_patern_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='投稿日'),
        ),
        migrations.AddField(
            model_name='actor',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AddField(
            model_name='actor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日'),
        ),
        migrations.AddField(
            model_name='cast',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='投稿日'),
        ),
        migrations.AddField(
            model_name='cast',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AddField(
            model_name='cast',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='dramadata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='投稿日'),
        ),
        migrations.AlterField(
            model_name='dramadata',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
        migrations.AlterField(
            model_name='dramadata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日'),
        ),
    ]
