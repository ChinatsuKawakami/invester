
# install pandas for analyzing data
import pandas_datareader.data as web
import datetime


def main():
    # set start date for reading stock data
    start = datetime.datetime(2017,12,27)
    # set end date for reading stock data
    end = datetime.datetime(2018,1,2)
    # set whose stock will be read and assigned to result
    result = web.DataReader('JPY=X','yahoo',start,end)
    print(result)

if __name__ == '__main__':
    main()