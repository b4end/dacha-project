from django.db import models
from core.models import Settlement

class News(models.Model):
    """
    Новости и объявления
    """
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    title = models.CharField("Заголовок", max_length=200)
    image = models.ImageField("Картинка новости", upload_to="news/", blank=True, null=True)
    short_description = models.TextField("Краткое описание", max_length=500, blank=True)
    content = models.TextField("Полный текст новости (HTML)")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.settlement.name}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at'] # Сначала свежие

class Document(models.Model):
    """
    Документы (Уставы, правила).
    """
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    title = models.CharField("Название документа", max_length=200)
    file = models.FileField("Файл", upload_to="docs/")
    is_public = models.BooleanField("Виден всем?", default=False, help_text="Если галочка не стоит, видят только авторизованные жители")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

class GalleryImage(models.Model):
    """
    Галерея
    """
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    image = models.ImageField("Фотография", upload_to="gallery/")
    caption = models.CharField("Подпись", max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Галерея"

class StaticPage(models.Model):
    """
    Для текстов 'О поселке', 'Инфраструктура'
    """
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    slug = models.SlugField("URL страницы (about, infrastructure)", help_text="about, infrastructure")
    title = models.CharField("Заголовок страницы", max_length=200)
    content = models.TextField("Контент (HTML)")
    image = models.ImageField("Фото страницы", upload_to="pages/", blank=True, null=True)

    def __str__(self):
        return f"{self.slug} - {self.settlement.name}"

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"
        unique_together = ('settlement', 'slug')