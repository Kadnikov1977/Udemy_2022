import requests

from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


URL = 'https://www.coronavirus2020.kz/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'accept': '*/*'}
response = requests.request("GET", URL, headers=HEADERS, verify=False)
if response.status_code == 200:
    html_data = BeautifulSoup(response.text, 'html.parser')
    quotes = html_data.find_all(class_='city_cov')
    new_list = [t.text for t in quotes]
    text_for_print = u'Всего зарегистрированных случаев заражения \n'
    text_for_print += new_list[0]
    print(text_for_print)