# Generated by Django 3.2.10 on 2023-12-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('passengers', models.IntegerField()),
            ],
        ),
    ]
