import re
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

page_data = []

for i in range(1,6542,100):
    print(i)
    url = f'https://www.the-numbers.com/movie/budgets/all/{i}'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    html_content = BS(requests.get(url, headers=agent).content)
    html_content = str(html_content).split("\n")
    line_data = []
    in_lineData = False
    for line in html_content:
        if "<tr>" in line:
            in_lineData = True
            indx = re.search(">([\\d,]+)<", line)
            if indx == None:
                in_lineData = False
                continue
            line_data.append(int(indx.group(1).replace(',','')))
        elif "</tr>" in line:
            in_lineData = False
            page_data.append(line_data)
            line_data = []
        elif in_lineData == True:
            data = re.search(">\\s\\$[\\d,]+<|>[a-zA-Z][a-zA-Z][a-zA-Z]\\s\\d+,\\s\\d+<", line)
            if data == None:
                data = re.search(">[^=|#|>]+<", line)
            try:
                data = data.group(0).replace('>', '').replace('<', '').replace("\xa0", '')
                data = int(data.replace('$','').replace(',','')) if re.search('\\$[\\d,]+', data) != None else data
                line_data.append(data)

            except:
                print(line)
        else:
            continue
    


        
page_data = pd.DataFrame(page_data)
page_data.set_index(0, inplace=True)
page_data.rename(columns={1:"release_date", 2:"title", 3:"budget", 4:"domestic_revenue", 5:"global_revenue"}, inplace=True)

page_data.to_csv("./data_gathering/theNumbers_finance.csv")