from django.db import models

# Create your models here.
class GameSales(models.Model):
    Rank = models.IntegerField(null=False, blank=False, unique=True)
    Name = models.CharField(max_length=512, null=False, blank=False)
    Platform = models.CharField(max_length=64, null=False, blank=False)
    Year = models.CharField(max_length=64 ,null=False, blank=False)
    Genre = models.CharField(max_length=128, null=False, blank=False)
    Publisher = models.CharField(max_length=128, null=False, blank=False)
    NA_Sales = models.FloatField(null=False, blank=False)
    EU_Sales = models.FloatField(null=False, blank=False)
    JP_Sales = models.FloatField(null=False, blank=False)
    Other_Sales = models.FloatField(null=False, blank=False)
    Global_Sales = models.FloatField(null=False, blank=False)
    
    def __str__(self) -> str:
        return f"Name: {self.Name}"