# Generated by Django 2.2.2 on 2019-10-03 06:55

import Kaldi_speech.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0027_user_curr_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=90, verbose_name='得分')),
                ('audio', models.FileField(default='default/default.wav', upload_to=Kaldi_speech.models.useraudio_directory_path, verbose_name='用户音频')),
            ],
        ),
        migrations.AddField(
            model_name='userverb',
            name='audio',
            field=models.FileField(default='default/default.wav', upload_to=Kaldi_speech.models.useraudio_directory_path, verbose_name='用户音频'),
        ),
        migrations.AddField(
            model_name='userverb',
            name='score',
            field=models.IntegerField(default=0, verbose_name='得分'),
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_img',
            field=models.ImageField(default='default/default.png', upload_to=Kaldi_speech.models.course_directory_path, verbose_name='课程封面'),
        ),
        migrations.AlterField(
            model_name='course',
            name='intro',
            field=models.CharField(default='写点介绍吧...', max_length=200, verbose_name='课程介绍'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='课程名称'),
        ),
        migrations.AlterField(
            model_name='course',
            name='num_learners',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AlterField(
            model_name='course',
            name='num_sections',
            field=models.IntegerField(default=0, verbose_name='课程章节'),
        ),
        migrations.AlterField(
            model_name='everydaymotto',
            name='audio',
            field=models.FileField(default='default/default.wav', upload_to='motto/audio', verbose_name='音频'),
        ),
        migrations.AlterField(
            model_name='everydaymotto',
            name='author',
            field=models.CharField(default='Rie fu', max_length=50, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='everydaymotto',
            name='motto',
            field=models.CharField(default='Life is like a boat', max_length=100, verbose_name='格言'),
        ),
        migrations.AlterField(
            model_name='everydaymotto',
            name='poster',
            field=models.ImageField(default='default/default.png', upload_to='motto/poster', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='section',
            name='num_sentences',
            field=models.IntegerField(default=0, verbose_name='章节例句数'),
        ),
        migrations.AlterField(
            model_name='section',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='章节副标题'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=100, verbose_name='章节标题'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='sentence_ch',
            field=models.CharField(max_length=200, verbose_name='中文释义'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='sentence_en',
            field=models.CharField(max_length=200, verbose_name='英文例句'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='sentence_src',
            field=models.FileField(default='default/default.wav', upload_to=Kaldi_speech.models.section_directory_path, verbose_name='例句音频'),
        ),
        migrations.AlterField(
            model_name='user',
            name='add_time',
            field=models.DateField(auto_now_add=True, verbose_name='添加事件'),
        ),
        migrations.AlterField(
            model_name='user',
            name='curr_course',
            field=models.IntegerField(default=-1, verbose_name='当前学习课程'),
        ),
        migrations.AlterField(
            model_name='user',
            name='open_id',
            field=models.CharField(max_length=100, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='curr_section',
            field=models.IntegerField(default=-1, verbose_name='当前章节'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='curr_sentence',
            field=models.IntegerField(default=-1, verbose_name='当前例句'),
        ),
        migrations.AlterField(
            model_name='verb',
            name='uk_phonetic',
            field=models.CharField(max_length=100, verbose_name='英式英标'),
        ),
        migrations.AlterField(
            model_name='verb',
            name='uk_speech',
            field=models.FileField(default='default/default.wav', upload_to='verb/', verbose_name='英式发音'),
        ),
        migrations.AlterField(
            model_name='verb',
            name='us_phonetic',
            field=models.CharField(max_length=100, verbose_name='美式英标'),
        ),
        migrations.AlterField(
            model_name='verb',
            name='us_speech',
            field=models.FileField(default='default/default.wav', upload_to='verb/', verbose_name='没事发音'),
        ),
        migrations.AlterField(
            model_name='verb',
            name='verb',
            field=models.CharField(max_length=50, verbose_name='词汇'),
        ),
        migrations.AlterField(
            model_name='verbexplain',
            name='explain',
            field=models.CharField(max_length=200, verbose_name='释义'),
        ),
        migrations.AlterField(
            model_name='verbexplain',
            name='pos',
            field=models.CharField(max_length=20, verbose_name='词性'),
        ),
        migrations.DeleteModel(
            name='UserAudio',
        ),
        migrations.AddField(
            model_name='usersentence',
            name='sentence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kaldi_speech.Sentence'),
        ),
        migrations.AddField(
            model_name='usersentence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kaldi_speech.User'),
        ),
    ]