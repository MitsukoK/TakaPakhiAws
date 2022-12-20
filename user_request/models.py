from django.db import models
from userapp.models import NewUser


# STATUS
STATUS_CHOICE = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Declined", "Declined"),
]
#! MOBILE BANKING MODEL
class RequestMobileBankModel(models.Model):
    # mobile banking choices
    MOBILE_BANKING_CHOICE = [
        ("Personal", "Personal"),
        ("Agent", "Agent"),
    ]

    # see which user is requesting
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # amount
    amount = models.IntegerField()
    # phone number
    phone_number = models.CharField(max_length=100)
    # bank name
    bank_name = models.CharField(max_length=100)
    # logo goes here
    add_logo = models.CharField(max_length=100, null=True)
    # choice field (personal, agent)
    choice = models.CharField(
        choices=MOBILE_BANKING_CHOICE,
        max_length=10,
        # default="Personal",
    )
    is_term = models.BooleanField()
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def __str__(self) -> str:
        return f"{self.user} - {self.amount}"


#! MOBILE RECHARGE MODEL
class RequestMobileRechargeModel(models.Model):
    # mobile banking choices
    MOBILE_RECHARGING_CHOICE = [
        ("Prepaid", "Prepaid"),
        ("Postpaid", "Postpaid"),
    ]
    # see which user is requesting
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # amount
    amount = models.IntegerField()
    # logo goes here
    add_logo = models.CharField(max_length=100, null=True)
    # phone number
    phone_number = models.CharField(max_length=100)
    # choice field (personal, agent)
    choice = models.CharField(
        choices=MOBILE_RECHARGING_CHOICE,
        max_length=10,
        # default="Personal",
    )
    is_term = models.BooleanField()
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def __str__(self) -> str:
        return f"{self.user} - {self.amount}"


#! BANKING MODEL
class BankingModel(models.Model):
    # see which user is requesting
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # amount
    amount = models.IntegerField()
    # logo goes here
    add_logo = models.CharField(max_length=100, null=True)
    # bank name
    bank_name = models.CharField(max_length=100)
    # bank account number
    bank_account_number = models.CharField(max_length=100)
    # bank account name
    bank_account_name = models.CharField(max_length=100)
    # branch name
    branch_name = models.CharField(max_length=100)
    # is terms and conditions checked
    is_term = models.BooleanField()
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def __str__(self) -> str:
        return (
            f"{self.user} - {self.amount} - {self.bank_name} - {self.bank_account_name}"
        )


#! Notification Model
class NotificationModel(models.Model):
    VIEWSTATUS = [
        ("read", "Read"),
        ("unread", "Unread"),
    ]
    # id = models.AutoField()
    status = models.CharField(max_length=20, choices=VIEWSTATUS)
    recharge = models.ForeignKey(
        RequestMobileRechargeModel,
        on_delete=models.CASCADE,
        null=True,
    )
    bank = models.ForeignKey(
        BankingModel,
        on_delete=models.CASCADE,
        null=True,
    )
    mobile_bank = models.ForeignKey(
        RequestMobileBankModel, on_delete=models.CASCADE, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
