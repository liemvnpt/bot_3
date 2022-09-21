from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import json
import csv

context = ssl._create_unverified_context()
def get_new_feed():
    url = 'https://www.vntrip.vn/cam-nang/kinh-nghiem-du-lich-pleiku-16284'
    # page = urllib.request.urlopen(url, context=context)
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    new_feed = soup.find(class_='journal-content-article')
    print(new_feed)
    return new_feed

def to_soup(html):
    return BeautifulSoup(html, 'html.parser')

def get_hotel():
    url = 'https://www.agoda.com/vi-vn/search?device=c&network=g&adid=579326890755&rand=9408577198103540256&expid=&adpos=&aud=kwd-303931321663&area=57734&site_id=1891453&tag=124bd041-bc20-49ce-bafd-dad790611496&gclid=Cj0KCQjw06OTBhC_ARIsAAU1yOVhg34uqwHpe_S_ylLyCsV2cxUzFd5pQLIotBtx4GwjDMx_dvct89caAlTOEALw_wcB'
    page = requests.get(url, verify=False)
    soup = to_soup(page.text)
    hotel = soup.find_all("div",class_='PropertyCard__HotelName')[:5]

    print(len(hotel))

    dt_arr= []
    cnt_arr = []

    for j in hotel:
        print(j.find("h3").text)
        dt_arr.append(j.find("h3").text)
        print(j.find("p").text)
        cnt_arr.append(j.find("p").text)


    return dt_arr,cnt_arr

def get_hotline(all=False):
    if all:
        url = 'hhttps://moh.gov.vn/danh-ba-uong-day-nong/-/asset_publisher/OYL33cPG6EH4/content/tinh-gia-lai?inheritRedirect=false'
    else:
        url = 'Đường dây nóng: 19009095 / 19003228'
    return url