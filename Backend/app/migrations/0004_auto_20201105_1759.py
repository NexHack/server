# Generated by Django 3.1.3 on 2020-11-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_skills_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='app.Skills'),
        ),
    ]
