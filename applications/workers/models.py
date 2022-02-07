from django.db import models

from applications.utils.models import UUIDModel


class Worker(UUIDModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return self.name

