# Generated by Django 3.1.7 on 2021-09-24 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_cbvs', '0003_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='django_cbvs.info'),
        ),
    ]
