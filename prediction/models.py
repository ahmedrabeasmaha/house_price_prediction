from re import T
from django.db import models

class HousingData(models.Model):
    LotArea = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    MasVnrArea = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    BsmtUnfSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    TotalBsmtSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    FstFlrSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    SndFlrSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    GrLivArea = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    GarageArea = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    WoodDeckSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    OpenPorchSF = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)
    SalePrice = models.DecimalField(max_digits = 100, decimal_places = 5,blank=True, null=True)