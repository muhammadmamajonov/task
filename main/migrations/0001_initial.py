# Generated by Django 4.0.6 on 2022-07-28 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apparat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apparat_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_count', models.IntegerField()),
                ('counted_at', models.DateTimeField()),
                ('apparat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.apparat')),
            ],
        ),
    ]
