from django.contrib import admin

from extras.models import FundModel, OfferModel


@admin.register(OfferModel)
class OfferAdmin(admin.ModelAdmin):
    list_display = [
        "offer_name",
        "offer_link",
        "offer_created_at",
    ]
    list_filter = ["offer_created_at"]
    search_fields = ["offer_name", "offer_description", "offer_link"]


@admin.register(FundModel)
class FundAdmin(admin.ModelAdmin):
    list_display = ["user", "fund_amount", "fund_id"]
    list_filter = ["fund_created_at"]
    search_fields = ["user", "fund_id"]
