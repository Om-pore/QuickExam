# Generated by Django 5.1.2 on 2024-10-31 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='finalexam',
            options={'verbose_name_plural': 'FinalExams'},
        ),
    ]
