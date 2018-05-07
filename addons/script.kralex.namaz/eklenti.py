import xbmcgui, xbmcaddon, xbmc
import sys, datetime, time
import threading

from resources.lib import namaz

reload(sys)  
sys.setdefaultencoding('utf8')

ayarlar = xbmcaddon.Addon().getSetting
gorunum = ayarlar('gorunum')
il = ayarlar('sehir').decode('utf-8')
arkaplan = ayarlar('arkaplan')


ACTION_PREVIOUS_MENU = 9
ACTION_SELECT_ITEM = 7
ACTION_STEP_BACK = 21

url = 'https://namazvakitleri.diyanet.gov.tr/tr-TR/9270'
#background = 'special://home/addons/script.kralex.namaz/image/b1.png'


if arkaplan == 'Siyah':
    background = 'special://home/addons/script.kralex.namaz/image/b1.png'

elif arkaplan == 'Mavi':
    background = 'special://home/addons/script.kralex.namaz/image/b2.png'

elif arkaplan == 'Bordo':
    background = 'special://home/addons/script.kralex.namaz/image/b3.png'

elif arkaplan == 'Yesil':
    background = 'special://home/addons/script.kralex.namaz/image/b4.png'

elif arkaplan == 'Kahverengi':
    background = 'special://home/addons/script.kralex.namaz/image/b5.png'

elif arkaplan == 'Mor':
    background = 'special://home/addons/script.kralex.namaz/image/b6.png'

elif arkaplan == 'Turuncu':
    background = 'special://home/addons/script.kralex.namaz/image/b7.png'


if gorunum == '0':
    X = int(ayarlar('konumX'))
    Y = int(ayarlar('konumY'))
    W=170
    H=85
    image = xbmcgui.ControlImage(x=X, y=Y, width=W, height=H, filename=background)
    kalanLabel = xbmcgui.ControlLabel(x=X, y=Y+10, width=W, height=H, font='font_clock', label='', alignment=2)
    kalanLabelUst = xbmcgui.ControlLabel(x=X, y=Y-2, width=W, height=H, font='font12', label='', alignment=2)
    kalanLabelAlt = xbmcgui.ControlLabel(x=X, y=Y+62, width=W, height=H, font='font12', label='', alignment=2)


elif gorunum == '1':
    X=400
    Y=25
    W=600
    H=600
    image = xbmcgui.ControlImage(x=X, y=Y, width=W, height=H, filename=background)
    ayLabel = xbmcgui.ControlImage(X+370, Y, 128, 128, '')
    tarihLabel = xbmcgui.ControlLabel(x=X+100, y=Y+20, width=240, height=60, font='font13', label='',alignment=1)

    Label1 = xbmcgui.ControlLabel(x=X, y=Y+140, width=W/2, height=H, font='font13', label='',alignment=2)
    Label1a = xbmcgui.ControlLabel(x=X, y=Y+170, width=W/2, height=H, font='font14', label='',alignment=2)

    Label2 = xbmcgui.ControlLabel(x=X+300, y=Y+140, width=W/2, height=H, font='font13', label='',alignment=2)
    Label2a = xbmcgui.ControlLabel(x=X+300, y=Y+170, width=W/2, height=H, font='font14', label='',alignment=2)

    Label3 = xbmcgui.ControlLabel(x=X+15, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label3a = xbmcgui.ControlLabel(x=X+15, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    Label4 = xbmcgui.ControlLabel(x=X+115, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label4a = xbmcgui.ControlLabel(x=X+115, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    Label5 = xbmcgui.ControlLabel(x=X+215, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label5a = xbmcgui.ControlLabel(x=X+215, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    Label6 = xbmcgui.ControlLabel(x=X+315, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label6a = xbmcgui.ControlLabel(x=X+315, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    Label7 = xbmcgui.ControlLabel(x=X+415, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label7a = xbmcgui.ControlLabel(x=X+415, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    Label8 = xbmcgui.ControlLabel(x=X+515, y=Y+215, width=60, height=80, font='font15', label='',alignment=2)
    Label8a = xbmcgui.ControlLabel(x=X+515, y=Y+240, width=60, height=80, font='font17', label='',alignment=2)

    LabelKible = xbmcgui.ControlLabel(x=X+65, y=Y+285, width=100, height=80, font='font10', label='',alignment=2)
    LabelKiblea = xbmcgui.ControlLabel(x=X+65, y=Y+302, width=100, height=80, font='font10', label='',alignment=2)
  
    LabelDogus = xbmcgui.ControlLabel(x=X+250, y=Y+285, width=100, height=80, font='font10', label='',alignment=2)
    LabelDogusa = xbmcgui.ControlLabel(x=X+250, y=Y+302, width=100, height=80, font='font10', label='',alignment=2)

    LabelBatis = xbmcgui.ControlLabel(x=X+440, y=Y+285, width=100, height=80, font='font10', label='',alignment=2)
    LabelBatisa = xbmcgui.ControlLabel(x=X+440, y=Y+302, width=100, height=80, font='font10', label='',alignment=2)

    LabelHaftalik = xbmcgui.ControlLabel(x=X, y=Y+355, width=W, height=80, font='font14', label='',alignment=2)

    LabelTarih = xbmcgui.ControlLabel(x=X+10, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelTariha = xbmcgui.ControlLabel(x=X+7, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelImsak = xbmcgui.ControlLabel(x=X+115, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelImsaka = xbmcgui.ControlLabel(x=X+115, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelGunes = xbmcgui.ControlLabel(x=X+195, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelGunesa = xbmcgui.ControlLabel(x=X+195, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelOgle = xbmcgui.ControlLabel(x=X+275, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelOglea = xbmcgui.ControlLabel(x=X+275, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelIkindi = xbmcgui.ControlLabel(x=X+355, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelIkindia = xbmcgui.ControlLabel(x=X+355, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelAksam = xbmcgui.ControlLabel(x=X+435, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelAksama = xbmcgui.ControlLabel(x=X+435, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

    LabelYatsi = xbmcgui.ControlLabel(x=X+515, y=Y+395, width=100, height=280, font='font12', label='',alignment=2)
    LabelYatsia = xbmcgui.ControlLabel(x=X+515, y=Y+420, width=100, height=280, font='font12', label='',alignment=2)

dt  = datetime.datetime


bugun = datetime.date.today().isoformat()
yarin = datetime.date.today() + datetime.timedelta(days=1)
ikigun = datetime.date.today() + datetime.timedelta(days=2)
ucgun = datetime.date.today() + datetime.timedelta(days=3)
dortgun = datetime.date.today() + datetime.timedelta(days=4)
besgun = datetime.date.today() + datetime.timedelta(days=5)
altigun = datetime.date.today() + datetime.timedelta(days=6)

def saat(girdi):
    cikti = dt.strptime(girdi, "%H:%M").strftime('%H:%M')
    return cikti

def in_between(now, start, end):
    if start <= end:
        return str(start) <= str(now) < str(end)
    else: # over midnight e.g., 23:30-04:15
        return str(start) <= str(now) or str(now) < str(end)

def kalan(tarih, saat):
    simdi = dt.now()
    kalan = dt.strptime(tarih + ' ' + saat, "%Y-%m-%d %H:%M") - simdi
    kalan = kalan.seconds
    hours = kalan // 3600
    minutes = (kalan % 3600) // 60
    seconds = kalan % 60
    if hours == 0:
        return '{}:{:02d}'.format(minutes, seconds)
    elif hours == 0 and minutes == 0:
        return '{:02d}'.format(seconds)
    else:
        return '{}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def kalin(metin):
    cikti = '[B]' + metin + '[/B]'
    return cikti

veriler = namaz.data

tarih = []
imsak = []
gunes = []
ogle = []
ikindi = []
aksam = []
yatsi = []
ayinsekli = []
miladi = []
hicri = []
kible = []
dogus = []
batis = []
miladit = []

for veri in veriler:
    Tarih = veri['MiladiTarihUzunIso8601']
    Imsak = veri['Imsak']
    Gunes = veri['Gunes']
    Ogle = veri['Ogle']
    Ikindi = veri['Ikindi']
    Aksam = veri['Aksam']
    Yatsi = veri['Yatsi']
    AyinSekli = veri['AyinSekliURL']
    Miladi = veri['MiladiTarihUzun']
    Hicri = veri['HicriTarihUzun']
    Kible = veri['KibleSaati']
    Dogus = veri['GunesDogus']
    Batis = veri['GunesBatis']
    Miladit = veri['MiladiTarihKisa']

    a = [bugun, str(yarin), str(ikigun), str(ucgun), str(dortgun), str(besgun), str(altigun)]

    if any(x in Tarih for x in a):
        tarih.append(Tarih)
        imsak.append(Imsak)
        gunes.append(Gunes)
        ogle.append(Ogle)
        ikindi.append(Ikindi)
        aksam.append(Aksam)
        yatsi.append(Yatsi)
        ayinsekli.append(AyinSekli)
        miladi.append(Miladi)
        hicri.append(Hicri)
        kible.append(Kible)
        dogus.append(Dogus)
        batis.append(Batis)
        miladit.append(Miladit)


class namazThreadClass(threading.Thread):
    def run(self):
        self.shutdown = False
        while not self.shutdown:
            if in_between(dt.now().time(), saat(imsak[0]), saat(gunes[0])):
                Metin = 'Vaktin çıkmasına'
                Kalan = kalan(bugun, gunes[0])
                Vakit = u'G\u00FCne\u015F: ' + gunes[0]

            elif in_between(dt.now().time(), saat(gunes[0]), saat(ogle[0])):
                Metin = 'Öğle namazına'
                Kalan = kalan(bugun, ogle[0])
                Vakit = u'\u00D6\u011Fle: '  + ogle[0]

            elif in_between(dt.now().time(), saat(ogle[0]), saat(ikindi[0])):
                Metin = 'İkindi namazına'
                Kalan = kalan(bugun, ikindi[0])
                Vakit = u'\u0130kindi: '  + kalin(ikindi[0])

            elif in_between(dt.now().time(), saat(ikindi[0]), saat(aksam[0])):
                Metin = 'Akşam namazına'
                Kalan = kalan(bugun, aksam[0])
                Vakit = u'Ak\u015Fam: '  + kalin(aksam[0])

            elif in_between(dt.now().time(), saat(aksam[0]), saat(yatsi[0])):
                Metin = 'Yatsı namazına'
                Kalan = kalan(bugun, yatsi[0])
                Vakit = u'Yats\u0131: '  + kalin(yatsi[0])

            elif in_between(dt.now().time(), saat(yatsi[0]), saat('23:59')):
                Metin = 'İmsak vaktine'
                Kalan = kalan(bugun, imsak[1])
                Vakit = u'\u0130msak: ' + imsak[1]

            elif in_between(dt.now().time(), saat('23:59'), saat(imsak[0])):
                Metin = 'İmsak vaktine'
                Kalan = kalan(bugun, imsak[0])
                Vakit = u'\u0130msak: ' + imsak[0]

            else:
                Metin = ''
                Kalan = ''
                Vakit = ''

            if gorunum == '0':
                kalanLabelUst.setLabel(Metin)     
                kalanLabel.setLabel(Kalan)
                kalanLabelAlt.setLabel(Vakit)

            if gorunum == '1':
                ayLabel.setImage(ayinsekli[0])
                tarihLabel.setLabel(miladi[0] + '\n\n' + hicri[0])
                Label1.setLabel(Metin)
                Label1a.setLabel(kalin(Kalan))
                Label2.setLabel('Sistem Saati')
                Label2a.setLabel(kalin('{:02d}:{:02d}:{:02d}'.format(dt.now().hour, dt.now().minute, dt.now().second)))
                Label3.setLabel('İmsak')
                Label3a.setLabel(kalin(imsak[0]))
                Label4.setLabel('Güneş')
                Label4a.setLabel(kalin(gunes[0]))
                Label5.setLabel('Öğle')
                Label5a.setLabel(kalin(ogle[0]))
                Label6.setLabel('İkindi')
                Label6a.setLabel(kalin(ikindi[0]))
                Label7.setLabel('Akşam')
                Label7a.setLabel(kalin(aksam[0]))
                Label8.setLabel('Yatsı')
                Label8a.setLabel(kalin(yatsi[0]))
                LabelKible.setLabel('Kıble Zamanı')
                LabelKiblea.setLabel(kalin(kible[0]))
                LabelDogus.setLabel('Gün Doğumu')
                LabelDogusa.setLabel(kalin(dogus[0]))
                LabelBatis.setLabel('Gün Batımı')
                LabelBatisa.setLabel(kalin(batis[0]))
                LabelHaftalik.setLabel(kalin(il + ' İÇİN HAFTALIK NAMAZ VAKİTLERİ'))
                LabelTarih.setLabel(kalin('Miladi Tarih'))
                LabelTariha.setLabel(miladit[0] + '\n' + miladit[1] + '\n' + miladit[2] + '\n' + miladit[3] + '\n' + miladit[4] + '\n' + miladit[5] + '\n' + miladit[6])
                LabelImsak.setLabel(kalin('İmsak'))
                LabelImsaka.setLabel(imsak[0] + '\n' + imsak[1] + '\n' + imsak[2] + '\n' + imsak[3] + '\n' + imsak[4] + '\n' + imsak[5] + '\n' + imsak[6])
                LabelGunes.setLabel(kalin('Güneş'))
                LabelGunesa.setLabel(gunes[0] + '\n' + gunes[1] + '\n' + gunes[2] + '\n' + gunes[3] + '\n' + gunes[4] + '\n' + gunes[5] + '\n' + gunes[6])
                LabelOgle.setLabel(kalin('Öğle'))
                LabelOglea.setLabel(ogle[0] + '\n' + ogle[1] + '\n' + ogle[2] + '\n' + ogle[3] + '\n' + ogle[4] + '\n' + ogle[5] + '\n' + ogle[6])
                LabelIkindi.setLabel(kalin('İkindi'))
                LabelIkindia.setLabel(ikindi[0] + '\n' + ikindi[1] + '\n' + ikindi[2] + '\n' + ikindi[3] + '\n' + ikindi[4] + '\n' + ikindi[5] + '\n' + ikindi[6])
                LabelAksam.setLabel(kalin('Akşam'))
                LabelAksama.setLabel(aksam[0] + '\n' + aksam[1] + '\n' + aksam[2] + '\n' + aksam[3] + '\n' + aksam[4] + '\n' + aksam[5] + '\n' + aksam[6])
                LabelYatsi.setLabel(kalin('Yatsı'))
                LabelYatsia.setLabel(yatsi[0] + '\n' + yatsi[1] + '\n' + yatsi[2] + '\n' + yatsi[3] + '\n' + yatsi[4] + '\n' + yatsi[5] + '\n' + yatsi[6])


            time.sleep(1.0)
            


class namazDialog(xbmcgui.WindowDialog):
    def __init__(self):
        if gorunum == '0':
            self.addControl(image)
            self.addControl(kalanLabel)
            self.addControl(kalanLabelUst)
            self.addControl(kalanLabelAlt)

        if gorunum == '1':
            self.addControl(image)
            self.addControl(ayLabel)
            self.addControl(tarihLabel)
            self.addControl(Label1)
            self.addControl(Label1a)
            self.addControl(Label2)
            self.addControl(Label2a)
            self.addControl(Label3)
            self.addControl(Label3a)
            self.addControl(Label4)
            self.addControl(Label4a)
            self.addControl(Label5)
            self.addControl(Label5a)
            self.addControl(Label6)
            self.addControl(Label6a)
            self.addControl(Label7)
            self.addControl(Label7a)
            self.addControl(Label8)
            self.addControl(Label8a)
            self.addControl(LabelKible)
            self.addControl(LabelKiblea)
            self.addControl(LabelDogus)
            self.addControl(LabelDogusa)
            self.addControl(LabelBatis)
            self.addControl(LabelBatisa)
            self.addControl(LabelHaftalik)
            self.addControl(LabelTarih)
            self.addControl(LabelTariha)
            self.addControl(LabelImsak)
            self.addControl(LabelImsaka)
            self.addControl(LabelGunes)
            self.addControl(LabelGunesa)
            self.addControl(LabelOgle)
            self.addControl(LabelOglea)
            self.addControl(LabelIkindi)
            self.addControl(LabelIkindia)
            self.addControl(LabelAksam)
            self.addControl(LabelAksama)
            self.addControl(LabelYatsi)
            self.addControl(LabelYatsia)

        self.kurThread = namazThreadClass()
        self.kurThread.start()

    def onAction(self, action):
        if action == ACTION_SELECT_ITEM :
            self.close()

if __name__ == '__main__':
    xbmc.executebuiltin ('ActivateWindow (home, return)')
    xbmc.sleep(200)
    xbmc.executebuiltin('xbmc.activatewindow(fullscreenvideo, return)')
    xbmc.sleep(300)
    dialog = namazDialog()
    dialog.doModal()
    del dialog
    xbmc.executebuiltin('Dialog.Close(10138)')
    sys.modules.clear()

'''
    params = urlparse.parse_qs('&'.join(sys.argv[1:]))
    xbmc.executebuiltin('xbmc.activatewindow(0)')
    xbmc.sleep(200)
    xbmc.executebuiltin('xbmc.activatewindow(fullscreenvideo)')
    xbmc.sleep(300)
    window = PopupWindow.altin()
    window.doModal()
    xbmc.sleep(30000)
    xbmc.executebuiltin('Dialog.Close(10138)')
    window.close()
    del window
    sys.modules.clear()

'''
