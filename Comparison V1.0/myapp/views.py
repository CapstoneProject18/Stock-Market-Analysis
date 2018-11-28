from django.shortcuts import render
from django import forms
import quandl
import pandas as pd

class NameForm(forms.Form):
    company = forms.CharField(label='company_name', max_length=100)
    start_date = forms.CharField(label='start_date', max_length=100)
    end_date = forms.CharField(label='end_date', max_length=100)


def fetch(request):
    if request.method == 'POST':
        company = []
        company1 = ''
        company2 = ''
        company3 = ''
        start_date = '2015-12-31'
        end_date = '2016-12-31'
        form = NameForm(request.POST)
        
        quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
        company1 = request.POST.get('company_name1')
        company2 = request.POST.get('company_name2')
        company3 = request.POST.get('company_name3')
        if company1 != '':
            company.append(company1)
        if company2 != '':
            company.append(company2)
        if company3 != '':
            company.append(company3)
        
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        dataRAW = quandl.get_table('WIKI/PRICES', ticker=company,
                         qopts={'columns': ['ticker', 'date', 'adj_close']},
                         date={'gte': start_date, 'lte': end_date},
                         paginate=True)
        new = dataRAW.set_index('date')
        data = new.pivot(columns='ticker')
        
        if len(data.columns) == 3:
            close1 = list(data[data.columns[0]].values[:])
            close2 = list(data[data.columns[1]].values[:])
            close3 = list(data[data.columns[2]].values[:])
        if len(data.columns == 2):
            close1 = list(data[data.columns[0]].values[:])
            close2 = list(data[data.columns[1]].values[:])
            close3 = []
        print(type(close1))
        
        dateData = dataRAW.set_index('ticker')
        date_col = dateData.ix[:,0]
        date_json = date_col.to_json(orient='records')
        
        return render(request, 'myapp/Comparison_Form.html', {'date': date_json, 'price1': close1, 'price2': close2, 'price3': close3 , 'company1': company1, 'company2': company2, 'company3': company3})

        # check whether it's valid:

    # if a GET (or any other method) we'll create a blank form
    else:
        quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
        company = 'AAPL'
        data = quandl.get_table('WIKI/PRICES', ticker=company,
                          qopts={'columns': ['ticker', 'date', 'adj_close']},
                          date={'gte': '2015-12-31', 'lte': '2016-12-31'},
                          paginate=True)
        data = data.set_index('ticker')
        date_col = data.ix[:, 0]
        date_json = date_col.to_json(orient='records')
        close_col = data.ix[:, 1]
        close_json = close_col.to_json(orient='records')
        
        return render(request, 'myapp/Comparison_Form.html', {'date': date_json, 'price': close_json, 'company': company})


def chart(request):
    return render(request, 'myapp/Comparison_Form.html')


def company(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		print(form)
		return render(request, 'myapp/Comparison_Form.html', {'date': date_json, 'price': close_json, 'company': company})