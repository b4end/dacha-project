from django.db import models
from core.models import Settlement

class StaticPage(models.Model):
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    slug = models.SlugField("URL страницы") # home, about
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Контент (HTML)")

    def __str__(self):
        return f"{self.slug} - {self.settlement.name}"

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"