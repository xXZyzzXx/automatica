from django.contrib import admin

from applications.store.models import Store, Visit


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "worker",
    )


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "visit_datetime",
        "store",
        "latitude",
        "longitude",
    )
    list_filter = ("visit_datetime",)
