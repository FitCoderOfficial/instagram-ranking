# Generated by Django 3.1 on 2020-08-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tiktok_user_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.BigIntegerField(blank=True, null=True)),
                ('id_number', models.BigIntegerField(blank=True)),
                ('secUid_number', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('biograghy', models.CharField(blank=True, max_length=500, null=True)),
                ('profilepic_url', models.URLField(blank=True, max_length=500)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('number_videos', models.BigIntegerField(blank=True)),
                ('number_heart', models.BigIntegerField(blank=True)),
                ('number_followers', models.BigIntegerField(blank=True)),
                ('number_follows', models.BigIntegerField(blank=True)),
                ('is_private', models.BooleanField(blank=True)),
                ('is_verified', models.BooleanField(blank=True)),
                ('is_favorite', models.BooleanField(blank=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='tiktok_user_data',
            index=models.Index(fields=['number_followers'], name='tiktok_user_number__bc0c01_idx'),
        ),
    ]