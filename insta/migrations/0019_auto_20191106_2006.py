# Generated by Django 2.2.6 on 2019-11-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0018_profile_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
    ]
