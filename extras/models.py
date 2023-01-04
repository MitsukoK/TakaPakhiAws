import uuid
from django.db import models

# Create your models here.


class OfferModel(models.Model):
    offer_name = models.CharField(max_length=100, null=True)
    offter_img = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.offer_name


class FundModel(models.Model):
    ammount = models.IntegerField()
    fund_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
