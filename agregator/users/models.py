# users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    STUDY_DIRECTIONS = [
        ('construction', 'Строительство'),
        ('programming', 'Программирование'),
    ]

    study_direction = models.CharField(
        max_length=20,
        choices=STUDY_DIRECTIONS,
        default='construction',
        verbose_name="Направление учебы"
    )

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def get_study_direction_display_name(self):
        return dict(self.STUDY_DIRECTIONS).get(self.study_direction, 'Не указано')
