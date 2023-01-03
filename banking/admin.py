from django.contrib import admin

from .models import BankingMethod


# custom admin
@admin.register(BankingMethod)
class BankingMethodAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo",
        "types",
    )
    list_filter = (
        "name",
        "types",
    )
    search_fields = (
        "name",
        "types",
    )
    list_per_page = 10
    editable_fields = ("types",)


# admin.site.register(BankingMethod)
