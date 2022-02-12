from django.contrib import admin

from applications.store.models import Store, Visit


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "worker",
    )
    search_fields = ("title",)


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
    search_fields = ("store__title", "store_worker__name",)
