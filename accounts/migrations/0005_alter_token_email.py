# Generated by Django 4.1 on 2022-08-17 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_useremail_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email_token', to='accounts.useremail'),
        ),
    ]
