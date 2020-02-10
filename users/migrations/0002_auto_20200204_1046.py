# Generated by Django 3.0.2 on 2020-02-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='cap',
            new_name='passenger_num',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='driver',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='ride',
            name='isComplete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]