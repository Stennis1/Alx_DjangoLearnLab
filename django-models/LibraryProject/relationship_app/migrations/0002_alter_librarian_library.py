# Generated by Django 4.2.11 on 2025-02-19 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relationship_app.library'),
        ),
    ]
