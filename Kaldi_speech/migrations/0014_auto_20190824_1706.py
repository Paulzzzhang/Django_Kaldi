# Generated by Django 2.2.4 on 2019-08-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0013_auto_20190824_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everydaymotto',
            name='poster',
            field=models.ImageField(default='motto/poster/default.png', upload_to='motto/poster', verbose_name='poster'),
        ),
    ]
