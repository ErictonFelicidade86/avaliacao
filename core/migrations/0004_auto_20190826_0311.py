# Generated by Django 2.2.4 on 2019-08-26 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190826_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='regiao',
            new_name='regioes',
        ),
    ]