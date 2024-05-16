# Generated by Django 3.2.25 on 2024-05-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20240510_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('title', models.CharField(max_length=200)),
                ('name_1', models.CharField(max_length=200)),
                ('url_1', models.URLField(
                    blank=True,
                    max_length=1024,
                    null=True
                )),
                ('name_2', models.CharField(max_length=200)),
                ('url_2', models.URLField(
                    blank=True,
                    max_length=1024,
                    null=True
                )),
            ],
        ),
    ]
