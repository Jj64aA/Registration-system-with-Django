# Generated by Django 4.1.7 on 2023-08-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=190, null=True)),
                ('u_number', models.CharField(max_length=190, null=True)),
                ('code_hash', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
