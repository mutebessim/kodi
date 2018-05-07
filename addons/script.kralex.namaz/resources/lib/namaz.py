# -*- coding: utf-8 -*-
import os, sys
from os import path
from datetime import datetime, timedelta
import requests, json, xbmcaddon
import xbmcvfs

reload(sys)  
sys.setdefaultencoding('utf8')

ayarlar = xbmcaddon.Addon().getSetting
il = ayarlar('sehir')

il2 = il.replace('İ', 'I').replace('Ğ', 'G').replace('Ç', 'C').replace('Ş', 'S').replace('Ü', 'U').replace('Ö', 'O')

anadizin = os.path.abspath(os.path.dirname(__file__))

dosya = anadizin + "/vakitler-" + il2 + ".json"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36' }

def vakitler():
    sehirler = 'https://ezanvakti.herokuapp.com/sehirler?ulke=2'
    datas = requests.get(sehirler, headers=header)
    datas = datas.json()

    sehir = []
    for data in datas:
        if data['SehirAdi'] == il:
            datas1 = requests.get('https://ezanvakti.herokuapp.com/ilceler?sehir=' + data['SehirID'], headers=header)
            datas1 = datas1.json()
            for data1 in datas1:
                if data1['IlceAdi'] == il:
                    sehir = data1['IlceID']

    url = "https://ezanvakti.herokuapp.com/vakitler?ilce=" + sehir
    veri = requests.get(url, headers=header)
    veri = veri.text

    data = xbmcvfs.File(dosya, 'w+')
    #data = open(dosya, 'w+')
    data.write(str(veri.encode('utf-8')))

if not os.path.exists(dosya):
    vakitler()

one_day_ago = datetime.now() - timedelta(days=3)
filetime = datetime.fromtimestamp(path.getmtime(dosya))


if filetime < one_day_ago:
    vakitler()

with open(dosya) as jveri:
    data = json.load(jveri)

