import requests

from bs4 import BeautifulSoup

resp = requests.get('https://www.coronavirus2020.kz/')

html_data = BeautifulSoup(resp.text, "html.parser", )

quotes = html_data.find_all('td')

# t = [i.find('a href=').get_text() for i in quotes]
print(quotes)

# quotes1 = html_data.find_all(class_="badge badge-danger")
# print(quotes1)

# t1 = [i.find(class_="badge badge-danger") for i in quotes1]

# t2 = []
# for i in t1:
#     if i != None:
#         t2.append(i)

# t3 = [i for i in t1]
#
# for i in range(len(t3)):
#     # print(t[i], t3[i])
#     print(t3[i])



