# Generated by Django 2.2.4 on 2019-08-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_consulta_regioes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='regioes',
            new_name='regiao',
        ),
    ]