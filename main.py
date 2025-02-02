import re

from bs4 import BeautifulSoup
from selenium import webdriver

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'}
JOB_URL = 'https://www.google.com/search?sca_esv=0dcf27f7239faca2&hl=en&biw=1920&bih=919&sxsrf=AHTn8zpOMIpVN_jzo6Z-Hnwe_mXuUbh_VA:1738527790314&q={0}&udm=8&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBnRhW2_is7MhE2uHZXC2Kp-K878BjLmyCCstxJdBYRc-o0mVzMMruV8STjOF2eC0cseG_bdEktd62NlRqIcKaKVOxbXyt0CpXPFw1UJPPc36IJIiPzBiO5gknJVEIlBU36HtQMSC1aALsyOeuEfz4iZtvccQ&sa=X&ved=2ahUKEwjxxf7a6KWLAxU2RUEAHWkAHd4Qs6gLegQIExAB&jbr=sep:0'

COOKIE = {
    '__Secure-ENID': '25.SE=PEySymhdMwwzdrTzCz8swjB2KPQ3-_1ADdhZErPSc3xdgOxj04wB8-V_3LCRVDCUdzqgSfUpQoZl7YPx7I7yZNCKEpstzYX2lNPKxxOQWJvI6-HSlUshUXtyXcw26E65Mk1rDVSw_pfy8pyEG9anKPUWIkha0ZcB_wgJcb1ZzdlRiTAeBJNwBRdz1urjQeCxGPG96wcG1vsbkM2EvML054_DuBlBHVexCdDPAXOmHfg',
    'AEC': 'AVcja2fcXilyrdvYJbS0c9InN_xRpX106uRPbLY0v-68GR-N-D0m5WWzNg',
    'SOCS': 'CAESHAgCEhJnd3NfMjAyNTAxMjktMF9SQzEaAmVuIAEaBgiA6_q8Bg'
}


def add_cookie(driver):
    for k, v in COOKIE.items():
        driver.add_cookie({'name': f'{k}', 'value': f'{v}'})


def run():
    driver = webdriver.Firefox()
    driver.get(JOB_URL.format("software+engineer"))
    add_cookie(driver)
    driver.refresh()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for result in soup.find_all('a', href=re.compile('.*jobs-detail-viewer')):
        title = result.find('div', class_='tNxQIb')
        print(title.text)
        posted = result.find('span', class_='Yf9oye')
        print(posted.text)
        location = result.find('div', class_='GoEOPd')
        print(location.text)
        print('\n')

    # todo tell selenium to page down to find more results

    driver.close()




if __name__ == '__main__':
    run()
