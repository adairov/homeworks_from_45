from django.db import models

# Create your models here.

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class ToDoList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус", default=STATUS_CHOICES[0][0])
    deadline = models.DateField(null=True, blank=True, verbose_name="Дедлайн")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.id}. {self.title}:{self.status}"