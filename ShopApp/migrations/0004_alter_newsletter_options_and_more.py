# Generated by Django 4.0.1 on 2022-01-27 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_alter_newsletter_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ('client_email',), 'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='client_email',
        ),
    ]