# Generated by Django 3.1 on 2020-08-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_user', '0010_auto_20200804_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insta_user_data',
            options={'ordering': ['number_followers']},
        ),
    ]