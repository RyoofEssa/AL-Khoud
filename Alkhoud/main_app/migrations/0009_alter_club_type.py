# Generated by Django 4.2.2 on 2023-06-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_club_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='type',
            field=models.CharField(choices=[('Gym', 'Gym'), ('Self_defense ', 'Self Defense '), ('Equestrian', 'Equestrian')], default='Equestrian', max_length=64),
        ),
    ]
