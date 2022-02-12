from django.contrib import admin

from applications.workers.models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
    )
    search_fields = ("name",)
