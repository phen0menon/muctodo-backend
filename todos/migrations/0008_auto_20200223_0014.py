# Generated by Django 3.0.3 on 2020-02-22 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_merge_20200222_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todos.TodoGroup'),
            preserve_default=False,
        ),
    ]
