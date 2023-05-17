from django.db import models
from django.urls import reverse


class Users(models.Model):
    username = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def __str__(self):
        return f'{self.id} Username: {self.username}, age: {self.age}'

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['id']


class Profile(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
