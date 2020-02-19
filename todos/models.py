from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class TodoGroup(models.Model):
    class Meta:
        verbose_name = "Todo Group"
        verbose_name_plural = "Todo Groups"

    # Creator of todo group (Django built-in user model)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo_groups")

    title = models.CharField(verbose_name="Group title", max_length=150)

    def __str__(self):
        return self.title


class Todo(models.Model):
    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ['position']

    # Title of a todo
    content = models.CharField(verbose_name="Content", max_length=1000)

    # Todo group
    group = models.ForeignKey(
        TodoGroup, on_delete=models.CASCADE, related_name="todos")

    # Created at (datetime field)
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True)

    # Remind at (datetime field)
    remind_at = models.DateTimeField(verbose_name="Remind at", null=True)

    # Ordering position
    position = models.PositiveIntegerField(default=0, blank=False, null=True)

    def __str__(self):
        return self.content
