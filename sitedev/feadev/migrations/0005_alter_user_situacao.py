# Generated by Django 5.0.6 on 2024-09-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feadev', '0004_alter_user_data_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='situacao',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
