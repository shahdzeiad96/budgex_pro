# Generated by Django 5.1.6 on 2025-03-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgex_app', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='budgex_user_set', to='auth.group'),
        ),
    ]
