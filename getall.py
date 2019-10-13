import csv
import time
import os
from trails.feeds.chinad import fetch as chinadfetch
from trails.feeds.conficker import fetch as confickerfetch
from trails.feeds.cryptolocker import fetch as cryptolockerfetch
from trails.feeds.gameover import fetch as gameoverfetch
from trails.feeds.locky import fetch as lockyfetch
from trails.feeds.necurs import fetch as necursfetch
from trails.feeds.tofsee import fetch as tofseefetch
from trails.feeds.virut import fetch as virutfetch
from trails.feeds.abuseipdb import fetch as abuseipdbfetch
from trails.feeds.alienvault import fetch as alienvaultfetch
from trails.feeds.atmos import fetch as atmosfetch
from trails.feeds.badips import fetch as badipsfetch
from trails.feeds.bambenekconsultingc2dns import fetch as dnsfetch
from trails.feeds.bambenekconsultingdga import fetch as dgafetch
from trails.feeds.bitcoinnodes import fetch as bitfetch
from trails.feeds.blackbook import fetch as blackfetch
from trails.feeds.blocklist import fetch as blockfetch
from trails.feeds.botscout import fetch as botfetch
from trails.feeds.bruteforceblocker import fetch as brufetch
from trails.feeds.ciarmy import fetch as ciafetch
from trails.feeds.cobaltstrike import fetch as cobfetch
from trails.feeds.cruzit import fetch as crufetch
from trails.feeds.cybercrimetracker import fetch as cybfetch
from trails.feeds.dataplane import fetch as datafetch
from trails.feeds.dshielddns import fetch as nsfetch
from trails.feeds.dshieldip import fetch as dsfetch
from trails.feeds.emergingthreatsbot import fetch as emfetch
from trails.feeds.emergingthreatscip import fetch as cipfetch
from trails.feeds.emergingthreatsdns import fetch as emerfetch
from trails.feeds.greensnow import fetch as snowfetch
from trails.feeds.loki import fetch as lokifetch
from trails.feeds.magento import fetch as magfetch
from trails.feeds.malc0de import fetch as malfetch
from trails.feeds.malwaredomainlistdns import fetch as maldnsfetch
from trails.feeds.malwaredomains import fetch as malmainsfetch
from trails.feeds.maxmind import fetch as maxmindfetch
from trails.feeds.minerchk import fetch as minerfetch
from trails.feeds.myip import fetch as myipfetch
from trails.feeds.nothink import fetch as nothinkfetch
from trails.feeds.openphish import fetch as openfetch
from trails.feeds.policeman import fetch as policefetch
from trails.feeds.pony import fetch as ponyfetch
from trails.feeds.proxyrss import fetch as proxyrssfetch
from trails.feeds.proxylists import fetch as proxylistsfetch
from trails.feeds.proxyspy import fetch as proxyspyfetch
from trails.feeds.ransomwaretrackerdns import fetch as randnsfetch
from trails.feeds.ransomwaretrackerip import fetch as ranipfetch
from trails.feeds.ransomwaretrackerurl import fetch as ranurlfetch
from trails.feeds.riproxies import fetch as ripfetch
from trails.feeds.rutgers import fetch as rutfetch
from trails.feeds.sblam import fetch as sblamfetch
from trails.feeds.socksproxy import fetch as sockfetch
from trails.feeds.sslipbl import fetch as sslipfetch
from trails.feeds.sslproxies import fetch as sslprofetch
from trails.feeds.talosintelligence import fetch as talofetch
from trails.feeds.torproject import fetch as torfetch
from trails.feeds.torstatus import fetch as torsfetch
from trails.feeds.trickbot import fetch as trickbotfetch
from trails.feeds.turris import fetch as turrisfetch
from trails.feeds.urlhaus import fetch as urlhausfetch
from trails.feeds.urlvir import fetch as urlvirfetch
from trails.feeds.voipbl import fetch as voipblfetch
from trails.feeds.vxvault import fetch as vxfetch
a=[chinadfetch(),confickerfetch(),cryptolockerfetch(),gameoverfetch(),lockyfetch(),necursfetch(),tofseefetch(),virutfetch(),abuseipdbfetch(),alienvaultfetch(),atmosfetch(),badipsfetch(),dnsfetch(),dgafetch(),bitfetch(),blackfetch(),blockfetch(),botfetch(),brufetch(),ciafetch(),cobfetch(),crufetch(),cybfetch(),datafetch(),nsfetch(),dsfetch(),emfetch(),cipfetch(),emerfetch(),snowfetch(),lokifetch(),magfetch(),malfetch(),maldnsfetch(),malmainsfetch(),maxmindfetch(),minerfetch(),myipfetch(),nothinkfetch(),openfetch(),policefetch(),ponyfetch(),proxyrssfetch(),proxylistsfetch(),proxyspyfetch(),randnsfetch(),ranipfetch(),ranurlfetch(),ripfetch(),rutfetch(),sblamfetch(),sockfetch(),sslipfetch(),sslprofetch(),talofetch(),torfetch(),torsfetch(),trickbotfetch(),turrisfetch(),urlhausfetch(),urlvirfetch(),voipblfetch(),vxfetch()]
directory="/home/sameen"
os.chdir(directory)
t = time.strftime('%Y-%m-%d',time.localtime())
suffix=".csv"
newfile=t+suffix
if not os.path.exists(newfile):
    f=open(newfile,'a')
    write=csv.writer(f)
    for i in a:
        re=i
        for k,v in re.items():
            x,y=v
            row=[k,x,y]
            write.writerow(row)
'''re=chinadfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=confickerfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=cryptolockerfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=gameoverfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=lockyfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=necursfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=tofseefetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=virutfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=abuseipdbfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=alienvaultfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=atmosfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=badipsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=dnsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=dgafetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=bitfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=blackfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=blockfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=botfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=brufetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=ciafetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=cobfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=crufetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=cybfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=datafetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=nsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=dsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=emfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=cipfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=emerfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=snowfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=lokifetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=magfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=malfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=maldnsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=malmainsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=maxmindfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=minerfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=myipfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=nothinkfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=openfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=policefetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=ponyfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=proxylistsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=proxyspyfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=randnsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=ranipfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=ranurlfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=ripfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=rutfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=sblamfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=sockfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=sslipfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=sslprofetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=talofetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=torfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=torsfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=trickbotfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=turrisfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=urlhausfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=urlvirfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=voipblfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)
re=vxfetch()
with open('/home/sameen/2019-09-28.csv','a') as f:
    write=csv.writer(f)
    for k,v in re.items():
        x,y=v
        row=[k,x,y]
        write.writerow(row)'''

