import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

webpage = requests.get(
    'https://www.ambitionbox.com/list-of-companies?page=1',
    headers=headers
).text

Soup = BeautifulSoup(webpage , 'lxml')

Company = Soup.find_all('div' , class_='companyCardWrapper__primaryInformation')

len(Company)

Name = []
Rating = []
Reviews = []
Ctype = []
Hq = []
HR = []
CR = []
for i in Company:
    Name.append(i.find('h2').text.strip())
    Rating.append(i.find('div',class_='rating_text rating_text--md').text.strip())
    Reviews.append(i.find('span',class_='companyCardWrapper__companyRatingCount').text.strip())
    info = i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')
    Ctype.append(info[0].strip())
    Hq.append(info[1].strip())
    ratings = i.find_all('span', class_='companyCardWrapper__ratingValues')
    HR.append(ratings[0].text.strip() if len(ratings) > 0 else None)
    CR.append(ratings[1].text.strip() if len(ratings) > 1 else None)

D = {'Name':Name,'Rating':Rating,'Reviews':Reviews,'Company_Type':Ctype,'Headquaters':Hq,'Highly Rated':HR,'Critically Rated':CR}
df = pd.DataFrame(D)
df

import pandas as pd
import requests
from bs4 import BeautifulSoup

Final = pd.DataFrame()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

for j in range(1, 11):

    url = f'https://www.ambitionbox.com/list-of-companies?page={j}'

    webpage = requests.get(url, headers=headers).text

    Soup = BeautifulSoup(webpage, 'lxml')

    Company = Soup.find_all('div', class_='companyCardWrapper__primaryInformation')

    Name = []
    Rating = []
    Reviews = []
    Ctype = []
    Hq = []
    HR = []
    CR = []

    for i in Company:

        Name.append(i.find('h2').text.strip())

        Rating.append(i.find('div', class_='rating_text rating_text--md').text.strip())

        Reviews.append(i.find('span', class_='companyCardWrapper__companyRatingCount').text.strip())

        info = i.find('span', class_='companyCardWrapper__interLinking').text.strip().split('|')

        Ctype.append(info[0].strip())

        Hq.append(info[1].strip() if len(info) > 1 else None)

        ratings = i.find_all('span', class_='companyCardWrapper__ratingValues')

        HR.append(ratings[0].text.strip() if len(ratings) > 0 else None)

        CR.append(ratings[1].text.strip() if len(ratings) > 1 else None)

    df = pd.DataFrame({
        'Name': Name,
        'Rating': Rating,
        'Rating': Rating,
        'Reviews': Reviews,
        'Company Type': Ctype,
        'Headquarters': Hq,
        'Highly Rated For': HR,
        'Critically Rated For': CR
    })

    Final = pd.concat([Final, df], ignore_index=True)

print(Final.shape)
Final.head(50)

Final.to_csv("ambitionbox_companies.csv", index=False)

