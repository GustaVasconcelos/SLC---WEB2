# Generated by Django 4.1.7 on 2023-04-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.TextField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
            ],
        ),
    ]