# Generated by Django 3.1.2 on 2020-11-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherRating', '0007_auto_20201015_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherrating',
            name='discipline_photo_path',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='teacherrating',
            name='photo_path',
            field=models.ImageField(upload_to=''),
        ),
    ]
