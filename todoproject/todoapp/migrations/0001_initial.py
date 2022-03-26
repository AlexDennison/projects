# Generated by Django 3.2.9 on 2021-11-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=250)),
                ('priority', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
