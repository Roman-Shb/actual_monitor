# Generated by Django 3.0 on 2020-08-29 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0047_repairer'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_rawdata',
            name='repairer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.Repairer', verbose_name='Ремонтник'),
        ),
    ]
