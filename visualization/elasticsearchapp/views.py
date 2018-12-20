from django.shortcuts import render
from .models import Companies
from .search import search
import pandas as pd
import numpy as np
# Create your views here.
def details(request):
#   post = BlogPost.objects.get(shortname=shortname)
  arg = request.GET.get('arg')
  response = search(arg)
  # responseDummy = response
  # responseDummy = pd.DataFrame(responseDummy)
  # print(responseDummy)
  # countries = responseDummy[responseDummy.columns[1]].values[:]
  # countries = list(countries)
  # countries = responseDummy.ix[:,1]
  # countries = countries.to_json(orient='records')
  # print(countries)
  return render(request, 'details.html',{'company': response})

def searching(request):
  return render(request, 'details.html')
