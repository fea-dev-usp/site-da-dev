# Generated by Django 5.0.6 on 2024-09-29 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feadev', '0003_alter_user_data_nascimento_alter_user_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_entrada',
            field=models.DateField(blank=True, null=True),
        ),
    ]