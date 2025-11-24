from django.db import models
from core.models import Settlement

class Plot(models.Model):
    STATUS_CHOICES = (
        ('free', 'Свободен'),
        ('reserved', 'Забронирован'),
        ('sold', 'Продан'),
    )
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name="Поселок")
    number = models.CharField("Номер участка", max_length=20)
    area = models.DecimalField("Площадь (сотки)", max_digits=5, decimal_places=2)
    price = models.DecimalField("Цена (руб)", max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='free')
    
    def __str__(self):
        return f"Участок {self.number} ({self.settlement.name})"

    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"