from django.contrib import admin
from .models import RequestMobileBankModel, RequestMobileRechargeModel, BankingModel

# Register your models here.

admin.site.register(RequestMobileBankModel)
admin.site.register(RequestMobileRechargeModel)
admin.site.register(BankingModel)
