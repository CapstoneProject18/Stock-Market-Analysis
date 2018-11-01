
# coding: utf-8

# In[2]:


import datetime
import requests
import os
from os.path  import basename
import glob
from bs4 import BeautifulSoup
import pandas as pd
import pprint
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

from flask import Flask , render_template , request , redirect , url_for , jsonify


# In[20]:


#Flask

#from flask import Flask
app = Flask(__name__)

_code = ""

@app.route("/", methods=["GET","POST"])
#def hello_world():
#    return 'Hello, World!'
def main():
    if(request.method == "POST"):
        _code = request.form['code']


        return redirect(url_for('getcode' , code = _code  ))
        # return render_template('index.html')
    else:

        return render_template('index.html' , var = "")



@app.route("/search")
def getcode():
    _code = request.args['code']
    news=""
    new=""
    news = _code.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", _code).split())
    new = _code

    analysis = TextBlob(new)
    # set sentiment
    pos = "Positive"
    neg = "Negative"
    #print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity > 0:
        return render_template('pos.html' , var = "")
    elif analysis.sentiment.polarity == 0:
        return render_template('neg.html' , var = "")
    else:
        return render_template('neg.html' , var = "")







if __name__ == "__main__":
    #app.run(host='127.0.0.1', debug=True, port=5000)
    app.run(debug=True)
