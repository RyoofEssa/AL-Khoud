# Generated by Django 4.2.2 on 2023-06-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
    ]
