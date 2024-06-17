# Generated by Django 3.2.16 on 2024-06-12 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jitterbunk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='jitterbunk.user'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='jitterbunk.user'),
        ),
    ]
