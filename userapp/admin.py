from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from banking.models import BankingMethod

from .models import NewUser

# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             "Additional Info",
#             {
#                 "fields": (
#                     "age",
#                     "nickname",
#                 ),
#             },
#         ),  # type: ignore
#     )

# fields = list(UserAdmin.fieldsets)
# fields[1] = (  # type: ignore
#     "Personal info",
#     {
#         "fields": (
#             "first_name",
#             "last_name",
#             "email",
#             # "age",
#             # "nickname",
#             "phone_number",
#             "user_pin",
#             "current_balance",
#             # "types",
#             # "client_identity_id",
#             #! mobile_banking, mobile_recharge, bank, gift_card
#             "mobile_banking",
#             "mobile_recharge",
#             "bank",
#             "gift_card",
#             "isReseller",
#         )
#     },
# )


# UserAdmin.fieldsets = tuple(fields)


# admin.site.register(NewUser, UserAdmin)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional Info",
            {
                "fields": (
                    "phone_number",
                    "user_pin",
                    "current_balance",
                    "mobile_banking",
                    "mobile_recharge",
                    "bank",
                    "gift_card",
                    "isReseller",
                ),
            },
        ),  # type: ignore
    )

    # set each mobile_banking, mobile_recharge, bank, gift_card in action
    def mobile_banking(self, obj):
        return obj.mobile_banking

    mobile_banking.short_description = "Mobile Banking"  # type: ignore
    mobile_banking.admin_order_field = "mobile_banking"  # type: ignore

    def mobile_recharge(self, obj):
        return obj.mobile_recharge

    mobile_recharge.short_description = "Mobile Recharge"  # type: ignore
    mobile_recharge.admin_order_field = "mobile_recharge"  # type: ignore

    def bank(self, obj):
        return obj.bank

    bank.short_description = "Bank"  # type: ignore
    bank.admin_order_field = "bank"  # type: ignore

    def gift_card(self, obj):
        return obj.gift_card

    gift_card.short_description = "Gift Card"  # type: ignore
    gift_card.admin_order_field = "gift_card"  # type: ignore

    def isReseller(self, obj):
        return obj.isReseller

    isReseller.short_description = "Reseller"  # type: ignore
    isReseller.admin_order_field = "isReseller"  # type: ignore

    list_display = (
        "client_identity_id",
        "username",
        "email",
        "phone_number",
        "user_pin",
        "current_balance",
        "mobile_banking",
        "mobile_recharge",
        "bank",
        "gift_card",
        "isReseller",
    )

    list_filter = (
        "username",
        "email",
        "phone_number",
        "user_pin",
        "current_balance",
        "mobile_banking",
        "mobile_recharge",
        "bank",
        "gift_card",
        "isReseller",
    )

    search_fields = (
        "username",
        "email",
        "phone_number",
        "user_pin",
        "current_balance",
        "mobile_banking",
        "mobile_recharge",
        "bank",
        "gift_card",
        "isReseller",
    )

    ordering = (
        "username",
        "email",
        "phone_number",
        "user_pin",
        "current_balance",
        "mobile_banking",
        "mobile_recharge",
        "bank",
        "gift_card",
        "isReseller",
    )

    filter_horizontal = ()

    list_per_page = 25

    actions = [
        "mobile_banking",
        "mobile_recharge",
        "bank",
        "gift_card",
        "isReseller",
    ]


admin.site.register(NewUser, CustomUserAdmin)
