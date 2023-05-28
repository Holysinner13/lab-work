from django.db import models
from django.contrib.auth.models import User
from items.models import Items


class Chat(models.Model):
    item = models.ForeignKey(Items, related_name='chat', on_delete=models.CASCADE, verbose_name='Чат')
    members = models.ManyToManyField(User, related_name='chat', verbose_name='Участники')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE, verbose_name='Чат')
    content = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
