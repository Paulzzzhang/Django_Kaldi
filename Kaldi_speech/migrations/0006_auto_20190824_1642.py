# Generated by Django 2.2.4 on 2019-08-24 08:42

import Kaldi_speech.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0005_auto_20190824_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='sentence_src',
            field=models.FileField(default='../media/course/default.wav', upload_to=Kaldi_speech.models.section_directory_path, verbose_name='audio'),
        ),
    ]