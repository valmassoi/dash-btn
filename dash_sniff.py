# Thanks to Ted Benson: https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.g4yme08zh
from scapy.all import *
import requests
import json
import time
import os
from devices import *

def sayBitcoin():
    print time.time()
    r = requests.get("https://www.bitstamp.net/api/ticker_hour/")
    data = json.loads(r.content)
    lastPrice = data['last']
    os.system("say bitcoin price is" +lastPrice[0:3])
    print lastPrice

def remoteLock():
    os.system("gnome-screensaver-command -a")

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    print pkt[ARP].psrc
    if pkt[ARP].psrc != '192.168.1.1': # ARP Probe
        if pkt[ARP].hwsrc == MAC_ADDRESS_CLOROX:
            print "Clorox Pushed: " + MAC_ADDRESS_CLOROX
            sayBitcoin()
        elif pkt[ARP].hwsrc == MAC_ADDRESS_CHARMIN:
            print "Charmin Pushed: " + MAC_ADDRESS_CHARMIN
            remoteLock()
        else:
            print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0) #count=100)
