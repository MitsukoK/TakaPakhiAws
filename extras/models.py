import uuid

from django.db import models

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


class FundModel(models.Model):

    # user
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # fund amount
    fund_amount = models.IntegerField()
    # fund created at
    fund_created_at = models.DateTimeField(auto_now_add=True)
    # auto generate random and unique fund id
    fund_id = models.CharField(
        max_length=100,
        unique=True,
        default=uuid.uuid4().hex[:10].upper(),
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.fund_amount}"

    def save_model(self, request, obj, form, change):
        # add money to user ammount when fund is created
        if not change:
            obj.user.user_amount += obj.fund_amount
            obj.user.save()
        super().save_model(request, obj, form, change)

    class Meta:
        verbose_name = "Fund"
        verbose_name_plural = "Funds"
