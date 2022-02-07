from django.db import models

from applications.workers.models import Worker
from applications.utils.models import UUIDModel


class Store(UUIDModel):
    title = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="stores")

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.title


class Visit(UUIDModel):
    visit_datetime = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="visits")
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"

    @property
    def title(self):
        return f"Visit ({self.id})"

    def __str__(self):
        return self.title
