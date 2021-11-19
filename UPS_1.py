import bs4 as bs
from bs4 import SoupStrainer
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

weblink = []
filing_type = []
company_name = []
date = []


urls_company_names = []
url = 'https://www.sec.gov/edgar/search/#/dateRange=1y&filter_forms=10-K&page='
for page in range(1,76):
    page_url = url+str(page)
    urls_company_names.append(page_url)


urls_company_names[1:4]
df = pd.read_csv('Dropped_Companies.csv')
c_names=df['Name of Stock']

search_urls = []
for name in c_names:
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company='+ name.replace(" ", "+") + '&type=10-K&dateb=&owner=exclude&count=100'
    search_urls.append(url)


k10_links = []
k10_dates = []
k10_cnames=[]
for url in search_urls:
    print(url)

    html =urllib.request.urlopen(url).read().decode('utf-8')

    index = html.find('tbody')
    html = html[index:]
    index = html.find('<tr')
    html = html[index:]



    ind_beg = url.find('company=')
    ind_end = url.find('&ty')
    cname = url[ind_beg+8:ind_end].replace('+',' ')

    if not html.find('<tr>')!= -1:
        index = html.find('<tr')
        html = html[index:]
        index = html.find('<a href')
        html = html[index:]
        index = html.find('"')
        html = html[index+1:]
        index = html.find('"')
        k10_links.append('https://www.sec.gov'+html[0:index])
        index = html.find('<td>')
        html = html[index+4:]
        index=html.find('<')
        k10_dates.append(html[:index])
        k10_cnames.append(cname)

k10_links_htm = []
    #url = 'https://www.sec.gov/Archives/edgar/data/37785/000119312510036348/0001193125-10-036348-index.htm'
for url in k10_links:
    html =urllib.request.urlopen(url).read().decode('utf-8')

    index = html.find('<table class')
    html = html[index:]
    index = html.find('<td scope')
    html = html[index:]
    index = html.find('<a href')
    html = html[index:]
    index = html.find('"')
    html = html[index+1:]
    index = html.find('">')
    k10_links_htm.append('https://www.sec.gov'+html[0:index])

for i in range(len(k10_dates)):
    date = k10_dates[i]
    if date[0] == '1' or date[0] == '2':
        pass
    else:
        k10_cnames.pop(i)
        k10_links.pop(i)
        k10_dates.pop(i)
        k10_links_htm.pop(i)
k10_types=[]
for i in range(len(k10_dates)):
    k10_types.append('10 K')

outputdf.to_csv('.csv')



import csv
final_list=[]
for i in range(len(k10_dates)):
    final_list.append([k10_cnames[i],k10_dates[i],k10_types[i],k10_links_htm[i]])
with open("10K Links.csv", "w", encoding="utf-8",newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([('Company Name','Filing Date','Filing Type', 'Link')])
    writer.writerows(final_list)