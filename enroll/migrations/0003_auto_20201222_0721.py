# Generated by Django 3.0.9 on 2020-12-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='image',
            field=models.ImageField(default='', upload_to='enroll/images'),
        ),
    ]
