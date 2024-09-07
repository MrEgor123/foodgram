from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models import UniqueConstraint

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True,
    )

    # Переопределите поля groups и user_permissions, чтобы избежать конфликтов
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Уникальное имя для обратной связи
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Уникальное имя для обратной связи
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name="Подписчик",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='subscribing',
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            UniqueConstraint(fields=['user', 'author'], name='unique_subscription')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'