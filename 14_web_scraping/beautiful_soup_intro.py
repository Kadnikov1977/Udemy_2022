from bs4 import BeautifulSoup

h_str = """
                            <tr class='table-row' onclick="yaCounter57348121.reachGoal('click_table_regions_row'); return true;" data-href='/countries/ru/77/'>

                    <td class="pl-3 text-left p-2">
                        <a
                                class='link-table'
                                href='/countries/ru/77/'
                                title='Коронавирус в Москве'
                        >
                            <span class="h6"><strong><u>Москва</u></strong></span>
                        </a>
                    </td>


                    <td>
                        <span class="badge badge-info"><span class="h6">2 194 045</span></span>
                        <br /><span class="badge badge-light mb-1">+19 509</span>                    </td>

                    <td>
                        <span class="badge badge-danger"><span class="h6">38 439</span></span>
                        <br /><span class="badge badge-light mb-1">+71</span>                    </td>
                    <td>
                        <span class="badge badge-success"><span class="h6">1 927 017</span></span>
                        <br /><span class="badge badge-light mb-1">+3 231</span>                    </td>
                    <td>
                        <span class="badge badge-secondary"><span class="h6">1.75%</span></span>
                    </td>

                </tr>

                            <tr class='table-row' onclick="yaCounter57348121.reachGoal('click_table_regions_row'); return true;" data-href='/countries/ru/78/'>

                    <td class="pl-3 text-left p-2">
                        <a
                                class='link-table'
                                href='/countries/ru/78/'
                                title='Коронавирус в Санкт-Петербурге'
                        >
                            <span class="h6"><strong><u>Санкт-Петербург</u></strong></span>
                        </a>
                    </td>


                    <td>
                        <span class="badge badge-info"><span class="h6">930 172</span></span>
                        <br /><span class="badge badge-light mb-1">+8 413</span>                    </td>

                    <td>
                        <span class="badge badge-danger"><span class="h6">29 479</span></span>
                        <br /><span class="badge badge-light mb-1">+63</span>                    </td>
                    <td>
                        <span class="badge badge-success"><span class="h6">838 112</span></span>
                        <br /><span class="badge badge-light mb-1">+645</span>                    </td>
                    <td>
                        <span class="badge badge-secondary"><span class="h6">3.17%</span></span>
                    </td>

                </tr>

                            <tr class='table-row' onclick="yaCounter57348121.reachGoal('click_table_regions_row'); return true;" data-href='/countries/ru/50/'>

                    <td class="pl-3 text-left p-2">
                        <a
                                class='link-table'
                                href='/countries/ru/50/'
                                title='Коронавирус в Московской области'
                        >
                            <span class="h6"><strong><u>Московская область</u></strong></span>
                        </a>
                    </td>


                    <td>
                        <span class="badge badge-info"><span class="h6">699 014</span></span>
                        <br /><span class="badge badge-light mb-1">+5 980</span>                    </td>

                    <td>
                        <span class="badge badge-danger"><span class="h6">13 078</span></span>
                        <br /><span class="badge badge-light mb-1">+39</span>                    </td>
                    <td>
                        <span class="badge badge-success"><span class="h6">616 966</span></span>
                        <br /><span class="badge badge-light mb-1">+926</span>                    </td>
                    <td>
                        <span class="badge badge-secondary"><span class="h6">1.87%</span></span>
                    </td>

                </tr>
"""



pars_h = BeautifulSoup(h_str, "html.parser")

print(pars_h.find_all(class_='h6').find_next_siblind('strong'))




#y = pars_h.select(".h6")
# for i in y:
#     print(i.attrs['class'])
#     print(i)
#
#
#       # .find('strong').find('u').get_text())
# print('======================================================')
# print(pars_h.select('td'))
# print('======================================================')











#
# t = pars_h.find_all(class_='pl-3 text-left p-2')
#
# for i in t:
#     print(i.text)

# print(pars_h.find_all('td'))
# print(pars_h.find_all(class_='h6'))




# # print(pars_h.body.ol.li)
#
# # print(pars_h.body.ol.find_all('li')[1])
#
# # print(pars_h.body.find(class_='green'))
#
# print(pars_h.body.select('.green')[1])
#
# print(pars_h.body.select('#css-li'))

