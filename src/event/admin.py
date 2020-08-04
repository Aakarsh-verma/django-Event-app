from django.contrib import admin
from event.models import EventPost


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "date_published",
        "date_updated",
        "author",
    )
    search_fields = (
        "title",
        "author",
    )
    readonly_fields = ("date_published", "date_updated")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(EventPost, EventAdmin)
