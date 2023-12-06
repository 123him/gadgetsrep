# Generated by Django 4.2.2 on 2023-07-24 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdts', '0003_remove_tbl_user1_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('warranty', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_products',
            },
        ),
    ]
