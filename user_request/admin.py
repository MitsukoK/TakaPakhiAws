from django.contrib import admin
from django.utils.html import format_html

from .models import (BankingModel, RequestMobileBankModel,
                     RequestMobileRechargeModel)


# custom admin for mobile banking
@admin.register(RequestMobileBankModel)
class RequestMobileBankModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "amount",
        "phone_number",
        "bank_name",
        "choice",
        "is_term",
        "created_at",
        "colored_status",
    )
    list_filter = (
        "user",
        "amount",
        # "phone_number",
        "bank_name",
        "choice",
        # "is_term",
        "created_at",
        "status",
    )
    search_fields = (
        "user",
        "amount",
        "phone_number",
        "bank_name",
        "choice",
        "is_term",
        # "created_at",
        "status",
    )
    list_per_page = 10
    editable_fields = ("status",)

    ordering = ("-created_at",)

    def colored_status(self, obj):
        if obj.status == "Pending":
            color_code = "blue"
        elif obj.status == "Approved":
            color_code = "green"
        elif obj.status == "Declined":
            color_code = "red"
        else:
            color_code = "black"
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            obj.status,
        )

    @admin.action(description="Approve selected")
    def approve(self, request, queryset):
        queryset.update(status="Approved")
        self.message_user(request, "Selected requests approved")

    @admin.action(description="Decline selected")
    def decline(self, request, queryset):
        queryset.update(status="Declined")
        self.message_user(request, "Selected requests declined")

    actions = ["approve", "decline"]


# custom admin for mobile recharge
@admin.register(RequestMobileRechargeModel)
class RequestMobileRechargeModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "amount",
        "phone_number",
        "choice",
        "is_term",
        "created_at",
        "colored_status",
    )
    list_filter = (
        "user",
        "amount",
        "is_term",
        "created_at",
        "status",
    )
    search_fields = (
        "user",
        "amount",
        "phone_number",
        "choice",
        "status",
    )
    list_per_page = 10
    editable_fields = ("status",)

    ordering = ("-created_at",)

    def colored_status(self, obj):
        if obj.status == "Pending":
            color_code = "blue"
        elif obj.status == "Approved":
            color_code = "green"
        elif obj.status == "Declined":
            color_code = "red"
        else:
            color_code = "black"
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            obj.status,
        )

    @admin.action(description="Approve selected")
    def approve(self, request, queryset):
        queryset.update(status="Approved")
        self.message_user(request, "Selected requests approved")

    @admin.action(description="Decline selected")
    def decline(self, request, queryset):
        queryset.update(status="Declined")
        self.message_user(request, "Selected requests declined")

    actions = ["approve", "decline"]


# custom admin for banking
@admin.register(BankingModel)
class BankingModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "amount_c",
        "bank_name",
        # "account_number",
        "bank_account_number",
        "is_term",
        "created_at",
        "colored_status",
    )
    list_filter = (
        "user",
        "amount",
        "bank_name",
        "is_term",
        "created_at",
        "status",
    )
    search_fields = (
        "user",
        "amount",
        "bank_name",
        "status",
    )
    list_per_page = 10
    editable_fields = ("status",)
    ordering = ("-created_at",)

    def amount_c(self, obj):
        return f"{obj.amount} tk"

    def colored_status(self, obj):
        if obj.status == "Pending":
            color_code = "blue"
        elif obj.status == "Approved":
            color_code = "green"
        elif obj.status == "Declined":
            color_code = "red"
        else:
            color_code = "black"
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            obj.status,
        )

    @admin.action(description="Approve selected")
    def approve(self, request, queryset):
        queryset.update(status="Approved")
        self.message_user(request, "Selected requests approved")

    @admin.action(description="Decline selected")
    def decline(self, request, queryset):
        queryset.update(status="Declined")
        self.message_user(request, "Selected requests declined")

    actions = ["approve", "decline"]


# admin.site.register(RequestMobileBankModel)
# admin.site.register(RequestMobileRechargeModel)
# admin.site.register(BankingModel)
