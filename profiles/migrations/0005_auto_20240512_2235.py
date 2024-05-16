from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20240511_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(
                blank_label='Country',
                null=True,
                blank=True
            ),
        ),
    ]
