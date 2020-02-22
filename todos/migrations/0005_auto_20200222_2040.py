# Generated by Django 3.0.3 on 2020-02-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20200220_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todos.TodoGroup'),
        ),
    ]
