import requests

from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = 'https://coronavirus-monitor.info/country/russia/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'accept': '*/*'}
response = requests.request("GET", URL, headers=HEADERS, verify=False)
if response.status_code == 200:
    html_data = BeautifulSoup(response.text, 'html.parser')
    quotes_region_country = html_data.find_all(class_='flex-table')
    quotes_new_count = html_data.find_all(class_='flex-row flex-row')
    list_region = []
    list_region_new_count = []
    list_country = []
    list_country_new_count = []
    # separ_region = 0
    # for i in quotes_all_data:
    #     if i.find(class_='flex-row first').get_text() == 'Регион':
    #         continue
    #     if i.find(class_='flex-row first').get_text() == 'Страна':
    #         separ_region = 1
    #         continue
    #     if separ_region == 0:
    #         list_region.append(i.find(class_='flex-row first').get_text())
    #         # list_region_new_count.append(i.find(class_='visible-sm visible-xs').get_text())
    #     else:
    #         list_country.append(i.find(class_='flex-row first').get_text())
    #         # list_country_new_count.append(i.find(class_='visible-sm visible-xs').get_text())



    separ_region = 0
    for i in quotes_region_country:
        if i.find(class_='flex-row first').get_text() == 'Регион':
            continue
        if i.find(class_='flex-row first').get_text() == 'Страна':
            separ_region = 1
            continue
        if separ_region == 0:
            list_region.append(i.find(class_='flex-row first').get_text())
            # if str(type(i.find(class_='visible-sm visible-xs'))) == '<class \'NoneType\'>':
            #     list_region_new_count.append('0')
            # else:
            #     list_region_new_count.append(i.find(class_='visible-sm visible-xs').text)
        else:
            list_country.append(i.find(class_='flex-row first').get_text())
            # if str(type(i.find(class_='visible-sm visible-xs'))) == '<class \'NoneType\'>':
            #     list_country_new_count.append('0')
            # else:
            #     list_country_new_count.append(i.find(class_='visible-sm visible-xs')['content'])

    for i in list_region:
        print(i, end='\n')

    for i in list_country:
        print(i, end='\n')

    separ_region = 0
    for i in quotes_new_count:
        print(i.find(class_='visible-sm visible-xs'))
        # i.find(class_='flex-row first').get_text() == 'Регион':
        #     continue
        # if i.find(class_='flex-row first').get_text() == 'Страна':
        #     separ_region = 1
        #     continue
        # if separ_region == 0:
        #     list_region.append(i.find(class_='flex-row first').get_text())
        #     # if str(type(i.find(class_='visible-sm visible-xs'))) == '<class \'NoneType\'>':
        #     #     list_region_new_count.append('0')
        #     # else:
        #     #     list_region_new_count.append(i.find(class_='visible-sm visible-xs').text)
        # else:
        #     list_country.append(i.find(class_='flex-row first').get_text())



    # for i in list_region_new_count:
    #     print(i, end='\n')
    #
    # for i in list_country_new_count:
    #     print(i, end='\n')
        # if str(type(i)) != '<class \'NoneType\'>':
        #     print(i, end='\n')
        # else:
        #     print('0')






        #     if str(i.find(class_='visible-sm visible-xs')) != 'None':
        #         list_region_new_count.append(i.find(class_='visible-sm visible-xs').get_text())
        #     else:
        #         list_region_new_count.append('0')
        #
        # else:
        #     if i.find(class_='flex-row first') != 'None':
        #         list_country.append(i.find(class_='flex-row first').get_text())
        #     else:
        #         list_country.append('0')
        #
        #     if str(i.find(class_='visible-sm visible-xs')) != 'None':
        #         list_country_new_count.append(i.find(class_='visible-sm visible-xs').get_text())
        #     else:
        #         list_country_new_count.append('0')



            # if i.find(class_='visible-sm visible-xs') != 'None':
            #     list_region_new_count.append(i.find(class_='visible-sm visible-xs').get_text())
            # # list_country.append(i.find(class_='flex-row first').get_text())
            # list_country_new_count.append(i.find(class_='visible-sm visible-xs'))


    # for i in range(0, len(list_region)):
    #     print(str(list_region[i]) + ' ' + str(list_region_new_count[i]))
    # for i in range(0, len(list_country)):
    #     print(str(list_country[i]) + ' ' + str(list_country_new_count[i]))

    # print(list_region)
    # print(list_country)


    #
    # quotes_name_of_region_and_country = 0
    # quotes_new_count = html_data.find_all(class_='visible-sm visible-xs')
    # # quotes3 = html_data.find_all(class_='badge badge-light mb-1')





    # list_region = []
    # list_country = []
    # separ_region = 0
    # for i in quotes_name_of_region_and_country:
    #     if i.get_text() == 'Регион':
    #         continue
    #     if i.get_text() == 'Страна':
    #         separ_region = 1
    #         continue
    #     if separ_region == 0:
    #         # print('регион ' + i.get_text())
    #         list_region.append(i.get_text())
    #     else:
    #         # print('страна ' + i.get_text())
    #         list_country.append(i.get_text())
    # print(list_region)
    # print(list_country)



    # new_list2 = [t.text for t in quotes1]
    # # new_list3 = [t.text for t in quotes2]
    # new_list3 = []
    # for t in quotes2:
    #     if t.text != '':
    #         new_list3.append(t.text)
    #     else:
    #         new_list3.append('+0')
    # print(new_list3)
    # new_list_3 = []
    # for i in range(0, len(new_list3)):
    #     if i % 3 == 0:
    #         new_list_3.append(new_list3[i])
    # for i in new_list_3:
    #     print(i, end='\n')
    # new_list_1 = []
    # for i in new_list1:
    #     s = str(i).strip("\n")
    #     new_list_1.append(s)
    # new_list_2 = []
    # for i in new_list2:
    #     s = str(i).strip("\n")
    #     new_list_2.append(i)
    # # new_list2 = [t.text for t in quotes2]
    # text_for_print = u'Всего зарегистрированных случаев заражения' + '\n' + '\n'
    # # print(new_list_1)
    # # print(new_list_2)
    #
    # for i in range(0, len(new_list_1)):
    #     text_for_print += new_list_1[i] + ' - ' + new_list_2[i] + '\n'
    # print(text_for_print)