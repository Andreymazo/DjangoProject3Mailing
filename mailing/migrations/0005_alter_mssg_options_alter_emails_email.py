# Generated by Django 4.1.6 on 2023-02-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_emails_options_rename_topic_mssg_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mssg',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='emails',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Емэйл'),
        ),
    ]
