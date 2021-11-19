import pandas as pd
import urllib
import bs4 as bs
from bs4 import SoupStrainer

df = pd.read_csv('10K Links.csv')
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

import pandas as pd
df = pd.read_csv('Dropped_Companies.csv')
company_names = list(df['Name of Stock'])

search_urls = []
for name in company_names:
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company='+ name.replace(" ", "+") + '&type=10-K&dateb=&owner=exclude&count=100'
    search_urls.append(url)


links = []
dates = []
companies = []
for url in search_urls:
    print(url)
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        table =soup.find_all('table')
        tr = table[2].find_all('tr')

        for i in range(len(tr)-1):

            d = tr[i+1].find_all('td')
            year=int(d[3].getText()[:4])

            if year >= 2019:

                a = tr[i+1].find_all('a')[0]
                index_beg=str(a).find('"')+1
                index_end = str(a)[index_beg:].find('"')
                link = 'https://www.sec.gov'+str(a)[index_beg:index_end+index_beg]


                date = d[3].getText()
                html1=urllib.request.urlopen(link).read()
                sp=BeautifulSoup(html1, "html.parser")
                table1 = sp.find_all('table')
                td = table1[0].find_all('td')
                a = td[2].find_all('a', href= True)
                index_beg=str(a).find('"')+1
                index_end = str(a)[index_beg:].find('">')
                link1 = 'https://www.sec.gov'+str(a)[index_beg:index_end+index_beg]
                index_comp_beg=url.find('ny=')+3
                index_comp_end=url.find('&type')
                company = url[index_comp_beg:index_comp_end].replace('+',' ')
                # print(year)
                # print(link1)
                # print(company)
                # print(date)
                links.append(link1)
                dates.append(date)
                companies.append(company)
    except:
        pass

outputdf = pd.DataFrame({'company name': companies,
                        'filing date': dates,
                        'doc link': links})


outputdf.to_csv('10KLinksBS.csv')