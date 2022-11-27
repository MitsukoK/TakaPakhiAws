from django.db import models


class BankingMethod(models.Model):
    """Banking Method for all systems

    Foregin Keys:
        * Mobile Banking
        * Bank
        * Mobile Rechanre
        * Gift Card

    Fields:
        * id
        * name (foregin Key)
        * logo (img)
        * type
    """

    auto_increment_id = models.AutoField(primary_key=True)  # type: ignore
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="logo")
    # type field with choices are Mobile Banking, Bank, Mobile Recharge, Gift Card
    types = models.CharField(
        max_length=20,
        choices=[
            ("Mobile Banking", "Mobile Banking"),
            ("Bank", "Bank"),
            ("Mobile Recharge", "Mobile Recharge"),
            ("Gift Card", "Gift Card"),
        ],
    )

    def __str__(self) -> str:
        return self.name  # + self.types.name  # type: ignore
