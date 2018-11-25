# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:14:48 2018

@author: Sangamesh
"""

import pandas as pd
#import pandas.io.data as web   # Package and modules for importing data; this code may change depending on pandas version
import datetime
from pandas_datareader import data, wb 
import numpy as np
# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
#end = datetime.date.today()
end = datetime.datetime(2016,12,31) 

###### Comparing multiple stocks #########
apple = data.DataReader("AAPL", "yahoo", start, end) # Collecting data Yahoo
microsoft = data.DataReader("MSFT", "yahoo", start, end) # Collecting data Microsoft
google = data.DataReader("GOOG", "yahoo", start, end) # Collecting data Google
 
# Below created a DataFrame consisting of the adjusted closing price of these stocks, first by making a list of these objects and using the join method
stocks = pd.DataFrame({"AAPL": apple["Adj Close"],
                      "MSFT": microsoft["Adj Close"],
                      "GOOG": google["Adj Close"]})
 
stocks.head()
## Plotting all stocks; Microsoft and Apple will be on right as there stock price is comparitively lower than google (by default on left)
stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True, title="Stock Prices")
# Calculating returns
# df.apply(arg) will apply the function arg to each column in df, and return a DataFrame with the result
# Recall that lambda x is an anonymous function accepting parameter x; in this case, x will be a pandas Series object
stock_return = stocks.apply(lambda x: x / x[0])
stock_return.head()
stock_return.plot(grid = True, title="Returns").axhline(y = 1, color = "black", lw = 2) # Plotting returns

# Modelling growth of the stock with log differences method
# Let's use NumPy's log function, though math's log function would work just as well
stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
stock_change.head()
stock_change.plot(grid = True, title="Growth of stocks").axhline(y = 0, color = "black", lw = 2) ## Plotting change or growth



