import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from userapp.models import NewUser

# Create your models here.


class OfferModel(models.Model):
    # offer name
    offer_name = models.CharField(max_length=100)
    # offer description
    offer_description = models.TextField()
    # offer image
    offer_image = models.ImageField(upload_to="offer_images")
    # offer link
    offer_link = models.URLField()
    # offer created at
    offer_created_at = models.DateTimeField(auto_now_add=True)
    # offer updated at
    offer_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.offer_name

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


# generate random and unique fund id
def generate_fund_id():
    fund_id = uuid.uuid4().hex[:10].upper()
    if FundModel.objects.filter(fund_id=fund_id).exists():
        return generate_fund_id()
    return fund_id


class FundModel(models.Model):

    # user
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # fund amount
    fund_amount = models.IntegerField()
    # fund created at
    fund_created_at = models.DateTimeField(auto_now_add=True)
    # auto generate random and unique fund id
    fund_id = models.CharField(
        max_length=10, default=generate_fund_id, editable=False, unique=True
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.fund_amount}"

    def save_model(self, request, obj, form, change):
        # add money to user amount when fund is created
        print("saving method called")
        if not change:
            print("this is new fund -> ", obj.fund_amount)
            print("this is user current balance -> ", obj.user.current_balance)

            obj.user.current_balance += obj.fund_amount
            print("this is user current balance after -> ", obj.user.current_balance)

            obj.user.save()
        super().save_model(request, obj, form, change)

    class Meta:
        verbose_name = "Fund"
        verbose_name_plural = "Funds"


@receiver(post_save, sender=FundModel)
def fund_created(sender, instance, created, **kwargs):
    if created:
        print("fund created")
        print("this is new fund -> ", instance.fund_amount)
        print("this is user current balance -> ", instance.user.current_balance)

        instance.user.current_balance += instance.fund_amount
        print("this is user current balance after -> ", instance.user.current_balance)

        instance.user.save()
    else:
        print("fund updated")
