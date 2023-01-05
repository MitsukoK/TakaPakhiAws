import uuid

from django.db import models

from userapp.models import NewUser

# STATUS
STATUS_CHOICE = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Declined", "Declined"),
]


# def generate_mobile_bank_id():
#     _id = uuid.uuid4().hex[:5].upper()
#     if RequestMobileBankModel.objects.filter(transaction_id=_id).exists():
#         return generate_mobile_bank_id()
#     return _id


# def generate_mobile_recharge_id():
#     _id = uuid.uuid4().hex[:5].upper()
#     if RequestMobileRechargeModel.objects.filter(transaction_id=_id).exists():
#         return generate_mobile_recharge_id()
#     return _id


# def generate_bank_id():
#     _id = uuid.uuid4().hex[:5].upper()
#     if BankingModel.objects.filter(transaction_id=_id).exists():
#         return generate_bank_id()
#     return _id


#! MOBILE BANKING MODEL
class RequestMobileBankModel(models.Model):
    # mobile banking choices
    MOBILE_BANKING_CHOICE = [
        ("Personal", "Personal"),
        ("Agent", "Agent"),
    ]

    # generate random and unique transaction id
    # transaction_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False
    # )
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
    ip_address = models.GenericIPAddressField(null=True)
    # choice field (personal, agent)
    choice = models.CharField(
        choices=MOBILE_BANKING_CHOICE,
        max_length=10,
        # default="Personal",
    )
    is_term = models.BooleanField()
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated at value is auto updated when the model is updated
    updated_at = models.DateTimeField(auto_now=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def save(self, *args, **kwargs):
        # check if the status has changed
        if (
            self.pk is not None
            and self.status != RequestMobileRechargeModel.objects.get(pk=self.pk).status
        ):
            # create a new instance with similar field values except for the status
            new_request = RequestMobileRechargeModel(
                user=self.user,
                bank_name=self.bank_name,
                amount=self.amount,
                phone_number=self.phone_number,
                choice=self.choice,
                is_term=self.is_term,
                status=self.status,
            )
            new_request.save()
        # call the original save method
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user} - {self.amount}"

    class Meta:
        verbose_name = "Mobile Banking"
        verbose_name_plural = "Mobile Banking"


#! MOBILE RECHARGE MODEL
class RequestMobileRechargeModel(models.Model):
    # mobile banking choices
    MOBILE_RECHARGING_CHOICE = [
        ("Prepaid", "Prepaid"),
        ("Postpaid", "Postpaid"),
    ]

    # generate random and unique transaction id
    # transaction_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False
    # )  # see which user is requesting
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100, null=True)

    # amount
    amount = models.IntegerField()
    # logo goes here
    add_logo = models.CharField(max_length=100, null=True)
    ip_address = models.GenericIPAddressField(null=True)

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
    # updated at value is auto updated when the model is updated
    updated_at = models.DateTimeField(auto_now=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def save(self, *args, **kwargs):
        # check if the status has changed
        if (
            self.pk is not None
            and self.status != RequestMobileRechargeModel.objects.get(pk=self.pk).status
        ):
            # create a new instance with similar field values except for the status
            new_request = RequestMobileRechargeModel(
                user=self.user,
                bank_name=self.bank_name,
                amount=self.amount,
                phone_number=self.phone_number,
                choice=self.choice,
                is_term=self.is_term,
                status=self.status,
            )
            new_request.save()
        # call the original save method
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name_plural = "Mobile Recharge"


#! BANKING MODEL
class BankingModel(models.Model):

    # generate random and unique transaction id
    # transaction_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False
    # )
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
    ip_address = models.GenericIPAddressField(null=True)

    # bank account name
    bank_account_name = models.CharField(max_length=100)
    # branch name
    branch_name = models.CharField(max_length=100)
    # is terms and conditions checked
    is_term = models.BooleanField()
    # created at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated at value is auto updated when the model is updated
    updated_at = models.DateTimeField(auto_now=True)
    # status
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="Pending")

    def save(self, *args, **kwargs):
        print("thisis primary key -> ", self.pk)
        print("this is self status -> ", self.status)
        print(BankingModel.objects.filter(pk=self.pk))
        print("checking their status -> ", end="")
        print(
            self.status != BankingModel.objects.filter(pk=self.pk).values()[0]["status"]
        )
        # check if the status has changed
        if (
            self.pk is not None
            and self.status
            != BankingModel.objects.filter(pk=self.pk).values()[0]["status"]
        ):
            # create a new instance with similar field values except for the status
            new_request = BankingModel(
                user=self.user,
                bank_name=self.bank_name,
                amount=self.amount,
                add_log=self.add_logo,
                bank_account_number=self.bank_account_number,
                ip_address=self.ip_address,
                choice=self.choice,
                is_term=self.is_term,
                status=self.status,
            )
            new_request.save()
        # call the original save method
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return (
            f"{self.user} - {self.amount} - {self.bank_name} - {self.bank_account_name}"
        )

    class Meta:
        verbose_name_plural = "Banking"
