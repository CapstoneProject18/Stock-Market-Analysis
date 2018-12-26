# Stock-Market-Analysis

## Objectives
* Creating a  model to predict next 3 day stock prices using historical data.
* Sentiment analysis on the news/twitter related to a particular stock.
* Comparing two or more companies based on their industry.
* Search engine to make use of information retrieval techniques for searching.
* Making a web application to produce comprehensive reports and compile the findings. 

## Work Done
* Prediction Module
    * The model takes closing price and volume traded of all four currencies for 60 time periods and suggests if we should buy or sell LITECOIN, 3 time periods into the future.
    * Final model which will take in 5 years of stock data and twitter sentiments as input giving future prices/suggestions on buying or selling for the stock.
* Sentiment Analysis Module
    * First step was to build a model to check for polarity of  a single tweet   
    * Using the twitter feed of the stock as  input
    * The feed is the processed by a classifier (glob) and its polarity is decided
    * The the  percentage of positive negative or neutral tweets is plotted in the form of a bar graph.
    * Integrating news 
    * Detailed quantitative sentiment analysis (Eg - Innovation for Tech)
* Visualisation Module
    * Create a portal for the investors where they can find analytics, news, about the company. 
    * Display a chart showing the time series plot of  close price of the company.
    * Show parameters like Market Cap, Book value, sales growth and other detail specific to  company. 
     * Display fundamental analysis of the company which includes Balance Sheets, P&L balances, Cash Flows of the company.
    * Show recent news / Announcement made by the company
* Comparison Module
    * comparison between two or more stocks based on stock price - visualisation done
    * comparison between two or more stocks based on returns and growth rate
    * Comparison  based on capital asset pricing model
    * Comparison dependent on visualisation module
* Search Engine Module
    * The prototype takes query from user and gives it to the IR system.
    * The IR system evaluates the query and output the top results from the database.
    * The key point to note here is that this is not a simple query-result case of RDBMS system but here we have unstructured data and based on the evaluation results of IR system we get the results.
    * Autocomplete using Edit Distance
    * Wildcard queries

*Our main project resides in visualization module of the master branch.*

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

What things you need to install the software

```
git
Python3
pip3
virtualenv [If no anaconda present]
Good internet connection : For retrieving data from APIs
```
Installing Anaconda will be better as most of the dependencies will be taken care of.

### Installing and running

A step by step series of examples that tell you how to get a development env running

Clonning the repository on your machine
```
git clone https://github.com/CapstoneProject18/Stock-Market-Analysis.git
```
Building a virtual environment and starting the environment (If no anaconda installed)
```
virtualenv env

For windows : env\Scripts\activate.bat
For linux   : source env/bin/activate 
```
Installing requirements
```
cd visualization
pip3 install -r requirements.txt
```
Running the project
```
python3 manage.py runserver
```
Open browser window and in new tab go to link http://127.0.0.1:8000
    
## [Contributors](https://github.com/CapstoneProject18/Stock-Market-Analysis/graphs/contributors)
* **Ayush Dosajh** - *Sentiment Module*
* **Ganesh Singh** - *Prediction Module*
* **Gulshan Singh** - *Search Engine Module*
* **Mayank Singh** - *Visualization Module*
* **Sangamesh Kotalwar** - *Comparison Module*

## Acknowledgement
We are highly indebted to Mr. Manish Hurkat and Mr. Bhavesh Sangwan for their guidance and constant supervision as well as for providing necessary information regarding the project & also for their support in completing the project.
We acknowledge that any work that I submit for assessment at NIIT University:
* Must be all my own work, unless this requirement is specifically excluded when part of a designated group assignment.  
* Must not have been prepared with the assistance of any other person, except those permitted within University guidelines or the specific assessment guidelines for the piece of work.
* Has not previously been submitted for assessment at this University or elsewhere.
