# Generated by Django 4.1 on 2022-08-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useremail_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremail',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
