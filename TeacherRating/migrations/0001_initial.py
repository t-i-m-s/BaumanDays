# Generated by Django 3.1.2 on 2020-10-09 21:25

import TeacherRating.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('surname', models.CharField(max_length=50, verbose_name='surname')),
                ('patronymic', models.CharField(max_length=50, verbose_name='patronymic')),
                ('discipline', models.CharField(max_length=50, verbose_name='discipline')),
                ('knowledge_level', models.IntegerField(verbose_name='knowledge level')),
                ('character_level', models.IntegerField(verbose_name='character level')),
                ('photo_path', models.FilePathField(path=TeacherRating.models.images_path, verbose_name='photo path')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='author name')),
                ('comment_text', models.CharField(max_length=500, verbose_name='comment text')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherRating.teacherrating')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]