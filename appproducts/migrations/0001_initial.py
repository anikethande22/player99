# Generated by Django 4.2.7 on 2023-12-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='static/photos/')),
                ('description', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('title', models.CharField(max_length=100)),
                ('copies', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=56)),
            ],
        ),
    ]
