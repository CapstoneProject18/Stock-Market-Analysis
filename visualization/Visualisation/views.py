from django.shortcuts import render
from django import forms
import quandl

class NameForm(forms.Form):
	company = forms.CharField(label='company_name', max_length=100)
	start_date = forms.CharField(label='start_date', max_length=100)
	end_date = forms.CharField(label='end_date', max_length=100)




def fetch(request):
    # return render(request, 'visualisation/chart.html')
	
	if request.method == 'POST':
		company = 'AAPL'
		start_date = '2015-12-31'
		end_date = '2016-12-31'
		form = NameForm(request.POST)
		print(request.POST.get('start_date'))
		quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
		company = request.POST.get('company_name')
		# start_date = request.POST.get('start_date')
		# end_date = request.POST.get('end_date')
		data = quandl.get_table('WIKI/PRICES', ticker = company,
			qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
			date = { 'gte': start_date, 'lte': end_date }, 
			paginate=True)
		data = data.set_index('ticker')
		print(type(data))
		date_col = data.ix[:,0]
		date_json = date_col.to_json(orient='records')
		close_col = data.ix[:,1]
		print(date_col)
		close_json = close_col.to_json(orient='records')
		print(date_json)
		print(close_json)
		return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company})

        # check whether it's valid:
        
    # if a GET (or any other method) we'll create a blank form
	else:

		quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
		company = 'AAPL'
		data = quandl.get_table('WIKI/PRICES', ticker = company,
			qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
			date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
			paginate=True)
		data = data.set_index('ticker')
		print(type(data))
		date_col = data.ix[:,0]
		date_json = date_col.to_json(orient='records')
		close_col = data.ix[:,1]
		print(date_col)
		close_json = close_col.to_json(orient='records')
		print(date_json)
		print(close_json)
		return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company})#, 'close' : close_col })



def chart(request):
    return render(request, 'visualisation/chart.html')

def company(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		print(form)
		return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company})


# Create your views here.


