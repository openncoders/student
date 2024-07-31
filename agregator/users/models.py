
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

    def get_study_direction_display_name(self):
        return dict(self.STUDY_DIRECTIONS).get(self.study_direction, 'Не указано')


class Teacher(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Легко'),
        ('medium', 'Средне'),
        ('hard', 'Тяжело'),
        ('very_hard', 'Очень тяжело'),
    ]
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    rating = models.BigIntegerField()
    characteristic = models.TextField()
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='easy'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'