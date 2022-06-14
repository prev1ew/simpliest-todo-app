# Generated by Django 4.0.5 on 2022-06-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_alter_todoitem_options_alter_todoitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('2', 'High'), ('1', 'Medium'), ('0', 'Low')], default='1', max_length=30),
        ),
    ]
