# Generated by Django 2.2.4 on 2019-08-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0004_auto_20190824_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]