# Generated by Django 4.2.2 on 2023-07-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdts', '0004_tbl_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_products',
            name='photo',
            field=models.URLField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_user1',
            name='photo',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
