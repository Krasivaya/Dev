# Generated by Django 2.2.6 on 2019-11-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0021_auto_20191107_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]