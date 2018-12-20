from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import CompanyIndex

# Create your models here.

# Companies to be indexed into ElasticSearch


class Companies(models.Model):
    id = models.IntegerField(default=0)
    compnumber = models.CharField(max_length=100, primary_key=True)
    ticker = models.CharField(max_length=200)
    longname = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    # Method for indexing the model
    def indexing(self):
        obj = CompanyIndex(
            meta={'id': self.compnumber},
            id = self.compnumber,
            compnumber=self.compnumber,
            ticker=self.ticker,
            longname=self.longname,
            shortname=self.shortname,
            country=self.country
        )
        obj.save()
        return obj.to_dict(include_meta=True)
