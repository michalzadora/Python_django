# Generated by Django 2.0.5 on 2018-06-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pension', '0003_auto_20180612_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='AAA', max_length=200),
        ),
        migrations.AddField(
            model_name='reservation',
            name='surname',
            field=models.CharField(default='AAA', max_length=200),
        ),
    ]
