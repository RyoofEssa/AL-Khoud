# Generated by Django 4.2.2 on 2023-06-16 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_coach_club_delete_contact_remove_enroll_club_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='city',
        ),
        migrations.RemoveField(
            model_name='club',
            name='type',
        ),
    ]
