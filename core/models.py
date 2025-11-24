from django.db import models
from django.contrib.auth.models import AbstractUser

class Settlement(models.Model):
    name = models.CharField("Название поселка", max_length=100)
    slug = models.SlugField("URL псевдоним", unique=True, help_text="Например: zapovednoe")
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поселок"
        verbose_name_plural = "Поселки"

class User(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('chairman', 'Председатель'),
        ('resident', 'Житель'),
        ('guest', 'Гость'),
    )
    role = models.CharField("Роль", max_length=20, choices=ROLES, default='guest')
    settlement = models.ForeignKey(Settlement, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Поселок")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"