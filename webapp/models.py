from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=100, null=False, blank=False, verbose_name="Статус", default="New")
    deadline = models.DateField(verbose_name="Дедлайн")

    def __str__(self):
        return f"{self.id}. {self.title}:{self.status}"