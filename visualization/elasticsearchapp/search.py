from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index
class CompanyIndex(DocType):
    id = Text()
    compnumber = Text()
    ticker = Text()
    longname = Text()
    shortname = Text()
    country = Text()

    class Meta:
        index = 'companies-index'

# Bulk indexing function, run in shell
def bulk_indexing():
    CompanyIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Companies.objects.all().iterator()))

# Simple search function
def search(arg):
    q = Q('match', country=arg)| Q('match', shortname=arg)
    s = Search().query(q)
    # s = Search().query('match', country=arg)| Search().query('match', shortname=arg)
    response = s.execute()

    print(response)
    responseDictarray = []

    for hit in response:
        i = 0
        responseDict = {}
        responseDict['compnumber'] = hit.compnumber
        responseDict['ticker'] = hit.ticker
        responseDict['longname'] = hit.longname
        responseDict['shortname'] = hit.shortname
        responseDict['country'] = hit.country

        responseDictarray.insert(i, responseDict)
        i = i + 1

    return responseDictarray

