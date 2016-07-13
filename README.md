# dash-btn
Amazon Dash Button Hack - prints and speaks Bitstamp bitcoin price

## Setup
Follow Amazon setup instruction, except the last step (selecting product)  
`$ git clone git@github.com:valmassoi/dash-btn.git`  
Linux: `$ sudo apt-get install python-scapy gnustep-gui-runtime` `$ pip install requests json`  
macOS: `$ brew tap Homebrew/python` `$ brew install scapy` `$ sudo easy_install pcapy requests json`  
`$ cd dash-btn`  
`$ sudo python dash_sniff.py`  
Push button  

## TODO
[ ] Fix: command runs twice per button push  
[ ] Fix: `pcapy API` bug on macOS  
[ ] Fix: bitcoin "spoken" price always rounds down
