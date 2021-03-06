# Generated by Django 3.0 on 2020-02-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0034_auto_20191125_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='color',
            field=models.CharField(max_length=7, null=True, verbose_name='Цвет в диаграммах'),
        ),
        migrations.AddField(
            model_name='reason',
            name='selectable',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='main_channel',
            field=models.CharField(blank=True, choices=[], max_length=5, null=True, verbose_name='Канал'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='workshop',
            field=models.CharField(choices=[('6', 'цех 6'), ('7', 'цех 7'), ('8', 'цех 8'), ('9', 'цех 9'), ('11', 'цех 11'), ('14', 'цех 14'), ('20', 'цех 20'), ('21', 'цех 21'), ('26', 'цех 26')], max_length=20, verbose_name='Цех'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='xbee_mac',
            field=models.CharField(blank=True, choices=[('00:0c:26:1a:29:83', '00:0c:26:1a:29:83'), ('00:13:A2:00:41:0A:4A:4B', '00:13:A2:00:41:0A:4A:4B'), ('00:13:A2:00:41:0A:4B:02', '00:13:A2:00:41:0A:4B:02'), ('00:13:A2:00:41:0A:4B:11', '00:13:A2:00:41:0A:4B:11'), ('00:13:A2:00:41:0A:4B:17', '00:13:A2:00:41:0A:4B:17'), ('00:13:A2:00:41:0A:55:EB', '00:13:A2:00:41:0A:55:EB'), ('00:13:A2:00:41:6C:D1:4A', '00:13:A2:00:41:6C:D1:4A'), ('00:13:A2:00:41:6C:D6:77', '00:13:A2:00:41:6C:D6:77')], max_length=25, null=True, verbose_name='MAC модема'),
        ),
    ]
