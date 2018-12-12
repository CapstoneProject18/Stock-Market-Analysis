from django.shortcuts import render
from django import forms


import requests
import glob
from bs4 import BeautifulSoup
import pandas as pd
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class NameForm(forms.Form):
    company = forms.CharField(label='company', max_length=100)


def fetch(request):
    #labels = ['neutral_tweet' , 'Negative_tweet' , 'Positive_tweet' ]
    values = [33 , 33 , 34]

    if request.method == 'POST':
        company = ''
        form = NameForm(request.POST)

        company = request.POST.get('company')




        class TwitterClient(object):

            def __init__(self):

                # keys and tokens from the Twitter Dev Console
                consumer_key = 'D6MkertW4Sj8rBSYoOsbvdhJl'
                consumer_secret = 'EldSKoYJlcXgHb2mbYqv7FZd98nOhmdex8sSmiTdarEjK5iGUM'
                access_token = '983592056445534210-vbGACTti0KK8fxa7fVks7qnlnHDFgxM'
                access_token_secret = '2IA4ordLzeGu48T9MgdzCQ62n2hiINrjnyzAMK9y84gau'

                # attempt authentication
                try:
                    # create OAuthHandler object
                    self.auth = OAuthHandler(consumer_key, consumer_secret)
                    # set access token and secret
                    self.auth.set_access_token(access_token, access_token_secret)
                    # create tweepy API object to fetch tweets
                    self.api = tweepy.API(self.auth)
                except:
                    print("Error: Authentication Failed")

            def clean_tweet(self, tweet):

                return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)" , " ", tweet).split())

            def get_tweet_sentiment(self, tweet):

                # create TextBlob object of passed tweet text
                analysis = TextBlob(self.clean_tweet(tweet))
                # set sentiment
                if analysis.sentiment.polarity > 0:
                    return 'positive'
                elif analysis.sentiment.polarity == 0:
                    return 'neutral'
                else:
                    return 'negative'

            def get_tweets(self, query, count = 10):

                # empty list to store parsed tweets
                tweets = []

                try:
                    # call twitter api to fetch tweets
                    fetched_tweets = self.api.search(q = query, count = count)

                    # parsing tweets one by one
                    for tweet in fetched_tweets:
                        # empty dictionary to store required params of a tweet
                        parsed_tweet = {}

                        # saving text of tweet
                        parsed_tweet['text'] = tweet.text
                        # saving sentiment of tweet
                        parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                        # appending parsed tweet to tweets list
                        if tweet.retweet_count > 0:
                            # if tweet has retweets, ensure that it is appended only once
                            if parsed_tweet not in tweets:
                                tweets.append(parsed_tweet)
                        else:
                            tweets.append(parsed_tweet)

                    # return parsed tweets
                    return tweets

                except tweepy.TweepError as e:
                    # print error (if any)
                    print("Error : " + str(e))


        # creating object of TwitterClient Class
        api = TwitterClient()
        # calling function to get tweets
        tweets = api.get_tweets(query = company, count = 200)

        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        # percentage of positive tweets
        #return("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        # percentage of negative tweets
        #print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
        # percentage of neutral tweets
        #return(" \t Neutral tweets percentage: {} %  ".format(100*(len(tweets) -len( ntweets) - len(ptweets))/len(tweets)) + " \n \t Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)) + " \n \t Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))  )
        #dict = {'values': {u'neutral_tweet':(100*(len(tweets) -len( ntweets) - len(ptweets))/len(tweets)) , u'positive':(100*len(ptweets)/len(tweets))  , u'negative':(100*len(ntweets)/len(tweets))}}
        #labels = [('neutral_tweet') , ('Negative_tweet') , ('Positive_tweet') ]
        values = [(100*(len(tweets) -len( ntweets) - len(ptweets))/len(tweets)) , (100*len(ntweets)/len(tweets))  , (100*len(ptweets)/len(tweets))]
        return render(request, 'myapp/company.html', { 'company': company , 'values' : values })

        # check whether it's valid:
    else:
        company = 'cipla'
        return render(request, 'myapp/company.html', { 'company': company ,  'values' : values })


    # if a GET (or any other method) we'll create a blank form


def chart(request):
    return render(request, 'myapp/chart.html')


def company(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		print(form)
		return render(request, 'myapp/company.html', {'company': company ,  'values' : values})
