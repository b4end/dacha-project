import os
import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser

# --- ФУНКЦИЯ ГЕНЕРАЦИИ ИМЕНИ ФАЙЛА ---
def avatar_filename(instance, filename):
    """
    Генерирует имя файла вида: avatars/av-000001.jpg
    Где 000001 - это ID пользователя.
    """
    # Получаем расширение файла (например, .jpg или .png)
    ext = filename.split('.')[-1]
    # Формируем имя: av- + ID (с нулями в начале до 6 символов)
    # instance.id - это ID пользователя
    new_filename = f"av-{instance.id:06d}.{ext}"
    return os.path.join('avatars', new_filename)

class Settlement(models.Model):
    name = models.CharField("Название поселка", max_length=100)
    slug = models.SlugField("URL псевдоним", unique=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    address = models.TextField("Адрес", blank=True)
    map_script = models.TextField("Код карты (Яндекс/Google)", blank=True, help_text="Вставьте скрипт карты сюда")

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
    
    phone = models.CharField("Телефон", max_length=20, blank=True, help_text="Для связи с председателем")
    
    # ИЗМЕНЕНИЕ: Добавили upload_to=avatar_filename
    avatar = models.ImageField("Аватарка", upload_to=avatar_filename, blank=True, null=True)

    def get_pastel_color(self):
        """
        Генерирует всегда одинаковый пастельный цвет на основе username.
        Возвращает HEX код без решетки.
        """
        colors = [
            'ffe5d9', 'd8e2dc', 'ffe5f9', 'e0c3fc', 
            'cbb2fe', 'bde0fe', 'a2d2ff', 'eaac8b', 
            'e2ece9', 'fff1e6', 'fde2e4', 'fad2e1',
        ]
        hash_object = hashlib.md5(self.username.encode())
        hash_int = int(hash_object.hexdigest(), 16)
        index = hash_int % len(colors)
        return colors[index]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"