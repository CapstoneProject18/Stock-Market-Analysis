from django.shortcuts import render
from django import forms
import quandl
import pandas as pd
# from sklearn.externals import joblib
# import numpy as np
# from keras.models import load_model


class NameForm(forms.Form):
	company = forms.CharField(label='company_name', max_length=100)
	start_date = forms.CharField(label='start_date', max_length=100)
	end_date = forms.CharField(label='end_date', max_length=100)



def home(request):
	
	quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
	company = 'AIG'
	data = quandl.get_table('WIKI/PRICES', ticker = company,
		qopts = { 'columns': ['ticker', 'date', 'adj_close' , 'volume'] },
		date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
		paginate=True)
	data = data.set_index('ticker')
	print(type(data))
	date_col = data.ix[:,0]
	date_json = date_col.to_json(orient='records')
	close_col = data.ix[:,1]
	volume = data.ix[:,2]
	print(date_col)
	close_json = close_col.to_json(orient='records')
	print(date_json)
	print(close_json)


	data = quandl.get_table('MER/F1', reportdate='2013-03-31', compnumber='372',paginate=True)

	company_details = {}
	company_details_values = {} 

	data_headers = list(data)
	company_details['company_number'] = data_headers[0]
	company_details['report_date'] = data_headers[4]
	company_details['report_type'] = data_headers[5]
	company_details['currency'] = data_headers[7]	
	company_details['long_name'] = data_headers[9]	
	company_details['short_name'] = data_headers[10]	
	company_details['status'] = data_headers[11]	
	company_details['country_code'] = data_headers[12]
	company_details['region'] = data_headers[13]
	company_details['ticker'] = data_headers[16]
	company_details['exchange'] = data_headers[17]
	company_details['address1'] = data_headers[18]
	company_details['address2'] = data_headers[19]
	company_details['address3'] = data_headers[20]
	company_details['address4'] = data_headers[21]
	company_details['city'] = data_headers[22]
	company_details['country'] = data_headers[24]
	company_details['phone_number'] = data_headers[26]
	company_details['website'] = data_headers[28]





	company_details_values['company_number'] = data['compnumber'][0]
	company_details_values['report_date'] = data['reportdate'][0]
	company_details_values['report_type'] = data['reporttype'][0]
	company_details_values['currency'] = data['currency'][0]	
	company_details_values['long_name'] = data['longname'][0]	
	company_details_values['short_name'] = data['shortname'][0]	
	company_details_values['status'] = data['status'][0]	
	company_details_values['country_code'] = data['countrycode'][0]
	company_details_values['region'] = data['region'][0]

	company_details_values['ticker'] = data['ticker'][0]
	company_details_values['exchange'] = data['exchange'][0]
	company_details_values['address1'] = data['address1'][0]
	company_details_values['address2'] = data['address2'][0]
	company_details_values['address3'] = data['address3'][0]
	company_details_values['address4'] = data['address4'][0]
	company_details_values['city'] = data['city'][0]
	company_details_values['country'] = data['country'][0]
	company_details_values['phone_number'] = data['phonenumber'][0]
	company_details_values['website'] = data['website'][0]
	pred = ''
	return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company , 'company_details' : company_details,'company_details_values' : company_details_values , 'pred' : pred})
	# return render(request, 'visualisation/company.html')




def fetch(request):
    # return render(request, 'visualisation/chart.html')
	
	# if request.method == 'POST':
		
	# 	company = request.POST.get('company_name') if request.POST.get('company_name') != '' else 'AAPL'
	# 	start_date = request.POST.get('start_date') if request.POST.get('start_date') != '' else '2015-12-31'
	# 	end_date = request.POST.get('end_date') if request.POST.get('end_date') != '' else '2016-12-31'
		
	# 	print(company)
	# 	print(start_date)
	# 	print(end_date)

	# 	# if(start_date == ''):
	# 	# start_date = '2015-12-31'
	# 	# end_date = '2016-12-31'
	# 	# form = NameForm(request.POST)
	# 	print(request.POST.get('start_date'))
	# 	quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
	# 	# company = request.POST.get('company_name')
	# 	# start_date = request.POST.get('start_date')
	# 	# end_date = request.POST.get('end_date')
	# 	data = quandl.get_table('WIKI/PRICES', ticker = company,
	# 		qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
	# 		date = { 'gte': start_date, 'lte': end_date }, 
	# 		paginate=True)
	# 	data = data.set_index('ticker')
	# 	print(type(data))
	# 	date_col = data.ix[:,0]
	# 	date_json = date_col.to_json(orient='records')
	# 	close_col = data.ix[:,1]
	# 	print(date_col)
	# 	close_json = close_col.to_json(orient='records')
	# 	print(date_json)
	# 	print(close_json)
		
	# 	company_excel = pd.read_excel("CompanyData.xlsx")
	# 	compn = company_excel[company_excel.ticker == company]['compnumber']
	# 	print(compn)
	# 	data = quandl.get_table('MER/F1', reportdate='2013-03-31', compnumber=compn ,paginate=True)

	# 	if(not data.empty and not compn.empty):
	# 		company_details = {}
	# 		company_details_values = {} 

	# 		data_headers = list(data)
	# 		company_details['company_number'] = data_headers[0]
	# 		company_details['report_date'] = data_headers[4]
	# 		company_details['report_type'] = data_headers[5]
	# 		company_details['currency'] = data_headers[7]	
	# 		company_details['long_name'] = data_headers[9]	
	# 		company_details['short_name'] = data_headers[10]	
	# 		company_details['status'] = data_headers[11]	
	# 		company_details['country_code'] = data_headers[12]
	# 		company_details['region'] = data_headers[13]
	# 		company_details['ticker'] = data_headers[16]
	# 		company_details['exchange'] = data_headers[17]
	# 		company_details['address1'] = data_headers[18]
	# 		company_details['address2'] = data_headers[19]
	# 		company_details['address3'] = data_headers[20]
	# 		company_details['address4'] = data_headers[21]
	# 		company_details['city'] = data_headers[22]
	# 		company_details['country'] = data_headers[24]
	# 		company_details['phone_number'] = data_headers[26]
	# 		company_details['website'] = data_headers[28]
		

	# 		company_details_values['company_number'] = data['compnumber'][0]
	# 		company_details_values['report_date'] = data['reportdate'][0]
	# 		company_details_values['report_type'] = data['reporttype'][0]
	# 		company_details_values['currency'] = data['currency'][0]	
	# 		company_details_values['long_name'] = data['longname'][0]	
	# 		company_details_values['short_name'] = data['shortname'][0]	
	# 		company_details_values['status'] = data['status'][0]	
	# 		company_details_values['country_code'] = data['countrycode'][0]
	# 		company_details_values['region'] = data['region'][0]
		
	# 		company_details_values['ticker'] = data['ticker'][0]
	# 		company_details_values['exchange'] = data['exchange'][0]
	# 		company_details_values['address1'] = data['address1'][0]
	# 		company_details_values['address2'] = data['address2'][0]
	# 		company_details_values['address3'] = data['address3'][0]
	# 		company_details_values['address4'] = data['address4'][0]
	# 		company_details_values['city'] = data['city'][0]
	# 		company_details_values['country'] = data['country'][0]
	# 		company_details_values['phone_number'] = data['phonenumber'][0]
	# 		company_details_values['website'] = data['website'][0]
	# 	else:
	# 		company_details = {}
	# 		company_details_values = {}
	# 		company_details['company_number'] = "compnumber"
	# 		company_details['report_date'] = "reportdate"
	# 		company_details['report_type'] = "reporttype"
	# 		company_details['currency'] = "currency"	
	# 		company_details['long_name'] = "longname"	
	# 		company_details['short_name'] = "shortname"	
	# 		company_details['status'] = "status"	
	# 		company_details['country_code'] = "countrycode"
	# 		company_details['region'] = "region"
	# 		company_details['ticker'] = "ticker"
	# 		company_details['exchange'] = "exchange"
	# 		company_details['address1'] = "address1"
	# 		company_details['address2'] = "address2"
	# 		company_details['address3'] = "address3"
	# 		company_details['address4'] = "address4"
	# 		company_details['city'] = "city"
	# 		company_details['country'] = "country"
	# 		company_details['phone_number'] = "phonenumber"
	# 		company_details['website'] ="website"
		

	# 		company_details_values['company_number'] = 'NA'
	# 		company_details_values['report_date'] = 'NA'
	# 		company_details_values['report_type'] = 'NA'
	# 		company_details_values['currency'] = 'NA'	
	# 		company_details_values['long_name'] = 'NA'	
	# 		company_details_values['short_name'] = 'NA'	
	# 		company_details_values['status'] = 'NA'	
	# 		company_details_values['country_code'] = 'NA'
	# 		company_details_values['region'] = 'NA'
		
	# 		company_details_values['ticker'] = 'NA'
	# 		company_details_values['exchange'] = 'NA'
	# 		company_details_values['address1'] = 'NA'
	# 		company_details_values['address2'] = ''
	# 		company_details_values['address3'] = 'NA'
	# 		company_details_values['address4'] = ''
	# 		company_details_values['city'] = ''
	# 		company_details_values['country'] = 'NA'
	# 		company_details_values['phone_number'] = 'NA'
	# 		company_details_values['website'] = 'NA'



	# 	return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company,'company_details' : company_details,'company_details_values' : company_details_values})

       
	# else:
	pred = {}
	


	arg = request.GET.get('company_name')
	quandl.ApiConfig.api_key = "23KLyzjn5UvKQog-DZyM"
	company = arg
	data = quandl.get_table('WIKI/PRICES', ticker = company,
		qopts = { 'columns': ['ticker', 'date', 'adj_close' , 'volume'] },
		date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
		paginate=True)
	data = data.set_index('ticker')
	print(type(data))
	date_col = data.ix[:,0]
	date_json = date_col.to_json(orient='records')
	close_col = data.ix[:,1]
	volume = data.ix[:,2]
	print(date_col)
	close_json = close_col.to_json(orient='records')
	print(date_json)
	print(close_json)

	company_excel = pd.read_excel("CompanyData.xlsx")
	compn = company_excel[company_excel.ticker == company]['compnumber']
	
	data = quandl.get_table('MER/F1', reportdate='2013-03-31', compnumber=compn ,paginate=True)

	
	if(not data.empty and not compn.empty):
		company_details = {}
		company_details_values = {} 

		data_headers = list(data)
		company_details['company_number'] = data_headers[0]
		company_details['report_date'] = data_headers[4]
		company_details['report_type'] = data_headers[5]
		company_details['currency'] = data_headers[7]	
		company_details['long_name'] = data_headers[9]	
		company_details['short_name'] = data_headers[10]	
		company_details['status'] = data_headers[11]	
		company_details['country_code'] = data_headers[12]
		company_details['region'] = data_headers[13]
		company_details['ticker'] = data_headers[16]
		company_details['exchange'] = data_headers[17]
		company_details['address1'] = data_headers[18]
		company_details['address2'] = data_headers[19]
		company_details['address3'] = data_headers[20]
		company_details['address4'] = data_headers[21]
		company_details['city'] = data_headers[22]
		company_details['country'] = data_headers[24]
		company_details['phone_number'] = data_headers[26]
		company_details['website'] = data_headers[28]
	

		company_details_values['company_number'] = data['compnumber'][0]
		company_details_values['report_date'] = data['reportdate'][0]
		company_details_values['report_type'] = data['reporttype'][0]
		company_details_values['currency'] = data['currency'][0]	
		company_details_values['long_name'] = data['longname'][0]	
		company_details_values['short_name'] = data['shortname'][0]	
		company_details_values['status'] = data['status'][0]	
		company_details_values['country_code'] = data['countrycode'][0]
		company_details_values['region'] = data['region'][0]
	
		company_details_values['ticker'] = data['ticker'][0]
		company_details_values['exchange'] = data['exchange'][0]
		company_details_values['address1'] = data['address1'][0]
		company_details_values['address2'] = data['address2'][0]
		company_details_values['address3'] = data['address3'][0]
		company_details_values['address4'] = data['address4'][0]
		company_details_values['city'] = data['city'][0]
		company_details_values['country'] = data['country'][0]
		company_details_values['phone_number'] = data['phonenumber'][0]
		company_details_values['website'] = data['website'][0]
	else:
		company_details = {}
		company_details_values = {}
		company_details['company_number'] = "compnumber"
		company_details['report_date'] = "reportdate"
		company_details['report_type'] = "reporttype"
		company_details['currency'] = "currency"	
		company_details['long_name'] = "longname"	
		company_details['short_name'] = "shortname"	
		company_details['status'] = "status"	
		company_details['country_code'] = "countrycode"
		company_details['region'] = "region"
		company_details['ticker'] = "ticker"
		company_details['exchange'] = "exchange"
		company_details['address1'] = "address1"
		company_details['address2'] = "address2"
		company_details['address3'] = "address3"
		company_details['address4'] = "address4"
		company_details['city'] = "city"
		company_details['country'] = "country"
		company_details['phone_number'] = "phonenumber"
		company_details['website'] ="website"
	

		company_details_values['company_number'] = 'NA'
		company_details_values['report_date'] = 'NA'
		company_details_values['report_type'] = 'NA'
		company_details_values['currency'] = 'NA'	
		company_details_values['long_name'] = 'NA'	
		company_details_values['short_name'] = 'NA'	
		company_details_values['status'] = 'NA'	
		company_details_values['country_code'] = 'NA'
		company_details_values['region'] = 'NA'
	
		company_details_values['ticker'] = 'NA'
		company_details_values['exchange'] = 'NA'
		company_details_values['address1'] = 'NA'
		company_details_values['address2'] = ''
		company_details_values['address3'] = 'NA'
		company_details_values['address4'] = ''
		company_details_values['city'] = ''
		company_details_values['country'] = 'NA'
		company_details_values['phone_number'] = 'NA'
		company_details_values['website'] = 'NA'

	pred['AAPL'] = "99.633"
	pred['MSFT'] = "53.044"
	pred['AIG'] = "59.322"
	pred['GOOGL'] = "778.834"

	if( not (company == 'AAPL' or company == 'AIG' or company =='GOOGL' or company == 'MSFT')):
		pred[company] = ''


	# c=close_col.tail(10)  #[56.5,56.23,55.28,55.17,55.4,54.62,55.32,54.09,52.31,51.86]
	# v=volume.tail(10) #[3177925,4343055,4262349,2964323,4455977,3743641,2497070,4785030,4820379,3843474]
	# i=[6750.54,6811.04,6881,6913,6929,6966,7101,7131,7046,7040,7030]
	# pred = (take_input(c,v,i,"AAL"))


	return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company , 'company_details' : company_details,'company_details_values' : company_details_values , 'pred' : pred[company]})



def take_input(c,v,i,comp):
    c=np.array(c)
    scaler0 = joblib.load("AAPL_close.save") 
    c=scaler0.transform(c.reshape(-1,1)).reshape(len(c),)
    v=np.array(v)
    scaler = joblib.load("AAPL_volume.save") 
    v=scaler.transform(v.reshape(-1,1)).reshape(len(v),)
    i=np.array(i)
    scaler = joblib.load("AAPL_index.save") 
    i=scaler.transform(i.reshape(-1,1)).reshape(len(i),)
    inp=np.array([])
    for j in range(0,10):
        temp=[]
        temp.append(c[j])
        temp.append(v[j])
        temp.append(i[j])
        temp=np.array(temp)
        inp=np.concatenate((inp,temp))
        
      
    
    inp=inp.reshape(1,10,3)  
    print(inp.shape)
    model=load_model("AAPL.h5")
    ans=scaler0.inverse_transform(model.predict(inp))
    #print(inp)
    return ans



def chart(request):
    return render(request, 'visualisation/chart.html')

def company(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		# print(form)
		return render(request, 'visualisation/company.html', { 'date' : date_json  , 'price' : close_json , 'company' : company})


# Create your views here.


