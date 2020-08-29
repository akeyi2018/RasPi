# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import ephem
import json

class sun_info:

    def __init__(self, code):
        self.postal_code = code
        #日の出入り時間の前後３０分にカーテン開閉を行う
        self.adjust_time = timedelta(minutes=30)
        #緯度経度書き込み用Jsonファイル名
        self.location_json_file = 'location.json'

    #jsonファイルから緯度経度を取得する
    def get_latlon_from_json(self):
        with open(self.location_json_file, 'r') as json_file:
            return json.load(json_file)
    
    #jsonに緯度経度を書き込む
    def write_latlon_to_json(self):
 
        res = self.get_latlon()
        if res is None: return res
 
        json_data = {'lat': res[0], 'lon': res[1]}
 
        with open(self.location_json_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    #郵便番号より経度、緯度を取得する（geocoding.jp)   
    def get_latlon(self):
        try:
            url = F'https://www.geocoding.jp/?q={self.postal_code}'
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'lxml')
            elems = soup.find('div', {'id': 'address'}).find_all("span")[0].find_all('b')
            return elems[0].text,elems[1].text
        except:
            return None

    #日の出入り時間を計算する（取得）
    def get_sun_info(self):

        location = ephem.Observer()
        res = self.get_latlon()
        if res is None:
            return res
        #緯度、経度をセット
        location.lat = res[0]
        location.lon = res[1]
        #現在時間UTCをセット
        location.date = datetime.utcnow()
   
        sun = ephem.Sun()
        #次の日の入りと日の出時間を取得
        sunrise_time = str(ephem.localtime(location.next_rising(sun)) + self.adjust_time)
        sunset_time = str(ephem.localtime(location.next_setting(sun)) - self.adjust_time)

        return sunset_time, sunrise_time

if __name__ == '__main__':

    suninfo = sun_info('252-0301')
    print(suninfo.get_sun_info())
    suninfo.write_latlon_to_json()
    
