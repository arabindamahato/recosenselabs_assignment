# Generated by Django 2.2.7 on 2020-06-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200603_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
