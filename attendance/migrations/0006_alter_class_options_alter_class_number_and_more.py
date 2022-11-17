# Generated by Django 4.1.3 on 2022-11-15 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_course_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='class',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('course', 'semester')},
        ),
    ]