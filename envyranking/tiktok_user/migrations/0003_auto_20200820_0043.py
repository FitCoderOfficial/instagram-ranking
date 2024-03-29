# Generated by Django 3.1 on 2020-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok_user', '0002_auto_20200820_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiktok_user_data',
            name='number_followers',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tiktok_user_data',
            name='number_follows',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tiktok_user_data',
            name='number_heart',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tiktok_user_data',
            name='number_videos',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
