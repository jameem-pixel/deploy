# Generated by Django 3.2.6 on 2021-10-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20211018_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='profile_img',
        ),
    ]
