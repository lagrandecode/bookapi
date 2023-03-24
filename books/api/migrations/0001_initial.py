# Generated by Django 4.1.7 on 2023-03-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number_pages', models.IntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
