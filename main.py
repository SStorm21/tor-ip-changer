import time
import threading
import os
import requests
def exit_():
	result=input("\n( ? ) are you sure you want to exit? (YES-NO) > ")
	if result.lower() =="yes" or result.lower()=="y":
		print("\n( ! ) exit ( ! ) ")
		exit(1)
	elif result.lower() =="no" or result.lower()=="n":
		os.system("clear")
	else:
		print("\n( ! ) Error uknown respones, ignore ( ! ) ")
		tor_sleep(times,sleep)
def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',

                       'https': 'socks5://127.0.0.1:9050'}
    return session
	
def tor_sleep(times,sleep):
	try:		
		i=1
		for i in range(times):
			os.system("clear")
			print("( i ) ip change times --> {}\n".format(i))
			print("( i ) sleep is --> {}\n".format(sleep))
			print("( i ) orginal times --> {}".format(times))
			time.sleep(sleep)
			os.system("service tor status")
			print("\n( i ) restarting...")
			os.system("service tor restart")
			time.sleep(2)
			session = get_tor_session()
			print("\nTor ip:")
			print(session.get("http://httpbin.org/ip").text)
			print("\nPublic ip:")
			print(requests.get("http://httpbin.org/ip").text)
			time.sleep(4)
		print("( ! ) done!\ntimes --> {}".format(times))
	except KeyboardInterrupt:
		exit_()
def change(times,sleep):
	times=int(times)
	sleep=int(sleep)
	try:	
		tor_sleep(times,sleep)
	except KeyboardInterrupt:
		exit_()
		
		
def startup():
	try:
	
		print("@StomrTools simple Tor ip changer\n make sure you have service tor installed on your linux machine\n")
		times=input("times (default is 10000) > ") or 10000
		sleep=input("sleep (default is 1min)  > ") or "60"
		print("( * ) times set to ---> {}".format(times)+"\n")
		if sleep:
			sleep = str(sleep)
			print("( * ) sleep set to ---> {}".format(sleep)+"\n")
		print("( * ) starting...\n")
		change(times,sleep)
	except KeyboardInterrupt as e:
		exit_()

if __name__=="__main__":
	startup()
	
