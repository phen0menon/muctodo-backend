# Generated by Django 3.0.3 on 2020-02-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_remind_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['position'], 'verbose_name': 'Todo', 'verbose_name_plural': 'Todos'},
        ),
        migrations.AddField(
            model_name='todo',
            name='position',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
