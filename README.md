# Stock-Market-Analysis
To predict the stock prices of next 5 days for the given stock if its stock price of last 5 years is given to you. Also many other visualisations to help user to understand more about the stock

## Objectives
* Creating a  model to predict next 3 day stock prices using historical data.
* Sentiment analysis on the news/twitter related to a particular stock.
* Comparing two or more companies based on their industry.
* Search engine to make use of information retrieval techniques for searching.
* Making a web application to produce comprehensive reports and compile the findings. 

## Work Done
* Prediction Module
    * The model takes closing price and volume traded of all four currencies for 60 time periods and suggests if we should buy or sell LITECOIN, 3 time periods into the future.
* Sentiment Analysis Module
    * First step was to build a model to check for polarity of  a single tweet   
    * Using the twitter feed of the stock as  input
    * The feed is the processed by a classifier (glob) and its polarity is decided
    * The the  percentage of positive negative or neutral tweets is plotted in the form of a bar graph.
* Visualisation Module
    * Create a portal for the investors where they can find analytics, news, about the company. 
    * Display a chart showing the time series plot of  close price of the company.
    * Show parameters like Market Cap, Book value, sales growth and other detail specific to  company. 
* Comparison Module
    * comparison between two or more stocks based on stock price - visualisation done
    * comparison between two or more stocks based on returns and growth rate
* Search Engine Module
    * The prototype takes query from user and gives it to the IR system.
    * The IR system evaluates the query and output the top results from the database.
    * The key point to note here is that this is not a simple query-result case of RDBMS system but here we have unstructured data and based on the evaluation results of IR system we get the results. 

## Work to be done
* Prediction module
    * Final model which will take in 5 years of stock data and twitter sentiments as input giving future prices/suggestions on buying or selling for the stock.
* Sentiment module
    * Integrating news 
    * Detailed quantitative sentiment analysis (Eg - Innovation for Tech)
* Visualisation module
    * Display fundamental analysis of the company which includes Balance Sheets, P&L balances, Cash Flows of the company.
    * Show recent news / Announcement made by the company
* Comparison module
    * Comparison  based on capital asset pricing model
    * Comparison dependent on visualisation module
* Search module
    * Autocomplete using Edit Distance
    * Wildcard queries
