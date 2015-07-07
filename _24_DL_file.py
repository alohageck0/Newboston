__author__ = 'royalfiish'
from urllib import request
goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=6&e=6&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def dwnl_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_path = r'goog.csv'
    fw = open(dest_path, 'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()

dwnl_stock_data(goog_url)