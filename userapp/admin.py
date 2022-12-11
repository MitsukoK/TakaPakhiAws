from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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

fields = list(UserAdmin.fieldsets)
fields[1] = (  # type: ignore
    "Personal info",
    {
        "fields": (
            "first_name",
            "last_name",
            "email",
            # "age",
            # "nickname",
            "phone_number",
            "user_pin",
            "current_balance",
            # "types",
            # "client_identity_id",
            #! mobile_banking, mobile_recharge, bank, gift_card
            "mobile_banking",
            "mobile_recharge",
            "bank",
            "gift_card",
            "isReseller",
        )
    },
)
UserAdmin.fieldsets = tuple(fields)


admin.site.register(NewUser, UserAdmin)
