# Generated by Django 2.2.7 on 2020-06-04 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20200604_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]