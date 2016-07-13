# Thanks to Ted Benson: https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.g4yme08zh
from scapy.all import *
import requests
import json
import time
import os

def bitcoin():
    print time.time()
    r = requests.get("https://www.bitstamp.net/api/ticker_hour/")
    data = json.loads(r.content)
    os.system("say bitcoin price is" +data['last'][0:3])
    print data['last']

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    #if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'f0:27:2d:f0:0a:60': # Clorox MAC ADDRESS
        print "Clorox Pushed: f0:27:2d:f0:0a:60"
        bitcoin()
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0) #count=100)
