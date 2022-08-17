# Generated by Django 4.1 on 2022-08-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useremail_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useremail',
            name='token',
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_token', to='accounts.useremail')),
            ],
        ),
    ]
