# Generated by Django 4.1.3 on 2022-11-13 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_collegeday_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['year', 'semester']},
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together={('year', 'semester')},
        ),
    ]
