import os
import signal
import subprocess
import urllib2
import time
from bs4 import BeautifulSoup

def update_pass():
	response = urllib2.urlopen('https://www.vpnme.me/freevpn.html')
	html = response.read()
	soup = BeautifulSoup(html)
	tds = soup.find_all('td')
	file = open('login.txt', 'w')
	file.write('fr-open\n')
	file.write(tds[38].string)
	file.close()
	return

def running(pid):      
    try:
        os.kill(pid, 0)
    except OSError:
    	pass
    	print('pid not found\n')
        return False
    else:
        return True

def connected():
    try:
        response=urllib2.urlopen('https://www.vpnme.me/freevpn.html',timeout = 10)
        return True
    except urllib2.URLError as err: pass
    print('Connerction failed\n')
    return False

ovpn = subprocess.Popen('sudo ./command.sh', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

try:
    while True:
		if not connected() or not running(ovpn.pid):
			print('Connection Fail \n')
			os.killpg(os.getpgid(ovpn.pid), signal.SIGTERM)
			update_pass()
			ovpn = subprocess.Popen('sudo ./command.sh', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
		time.sleep(100)
except KeyboardInterrupt:
    pass
    os.killpg(os.getpgid(ovpn.pid), signal.SIGTERM)