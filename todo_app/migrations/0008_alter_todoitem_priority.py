# Generated by Django 4.0.5 on 2022-06-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_alter_todoitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=30),
        ),
    ]