
# coding: utf-8

# In[14]:


import csv
import time
import requests
from bs4 import BeautifulSoup
from pattern.en import ngrams

Base_url = "http://www.moneycontrol.com"


companies = {'cadilahealthcare':'CHC','piramalenterprises':'PH05',
             'glenmarkpharma':'GP08','glaxosmithklinepharmaceuticals':'GSK',
             'sunpharmaceuticalindustries':'SPI','lupinlaboratories':'LL',
             'cipla':'C','aurobindopharma':'AP',
             'drreddyslaboratories':'DRL','divislaboratories':'DL03'}
             
# Create a list of the news section urls of the respective companies 
url_list = ['http://www.moneycontrol.com/company-article/{}/news/{}#{}'.format(k,v,v) for k,v in companies.items()]
print(url_list)


# In[16]:


# Create an empty list which will contain the selected news articles 
List_of_links = []   

# Extract the relevant news articles weblinks from the news section of selected companies
for urls in url_list:
    html = requests.get(urls)
    soup = BeautifulSoup(html.text,'html.parser') # Create a BeautifulSoup object 

   # Retrieve a list of all the links and the titles for the respective links
    word1,word2,word3 = "US","USA","USFDA"
 
    sub_links = soup.find_all('a', class_='arial11_summ')
    for links in sub_links:
        sp = BeautifulSoup(str(links),'html.parser')  # first convert into a string
        tag = sp.a
        if word1 in tag['title'] or word2 in tag['title'] or word3 in tag['title']:
            category_links = Base_url + tag["href"]
            List_of_links.append(category_links)
            time.sleep(3)


# In[42]:


# Remove the duplicate news articles based on News Title
import json

unique_links = list(set(List_of_links))
for q in unique_links: 
    print(q)

# Create a dictionary of positive/negative words related to the Pharma Sector
#reader = csv.reader(open('dict.csv', 'r'))
#pharma_dict = dict((rows[0],rows[1]) for rows in reader)

# Creating an empty list which will be filled later with news article links, and Polarity values (pos/neg)
#df =[]
#print(df)


# In[47]:


# Open the choosen news articles and extract the main text  
for selected_links in unique_links:
    results_url = selected_links 
   #print results_url
   
    results = requests.get(results_url)
    results_text = BeautifulSoup(results.text , "lxml")
    #print(results.text)
    #break
    extract_text = results_text.find(class_='arti-flow')
    try:
        data = json.loads(results_text.find('script', type='application/ld+json').text)
    except:
        continue
    #print(data['description'])
    #print(extract_text)
    #print(data)
    #final_text = extract_text.get_text()
    final_text = data['description']
    #print(final_text)
    
    # Pre-processing the extracted text using ngrams function from the pattern package   
    final_text1 = ngrams(final_text, n=1, punctuation=".,;:!?()[]{}`''\"@#$^&*+-|=~_", continuous=False)
    print (final_text1)
    

