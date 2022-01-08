import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title WARP-PLUS-CLOUDFLARE By HUNGNOPRO")
os.system('cls' if os.name == 'nt' else 'clear')
print ("WARP-PLUS-CLOUDFLARE By HUNGNOPRO")
print ("[+] TINH NANG:")
print ("[-] HACK VO HAN GB WARP+")
print ("[-] Version: Latest")
print ("--------")  
print ("[-] FACEBOOK: facebook.com/HungNeMaOi/") 
print ("[-] TIKTOK: tiktok.com/@hung_uwu")
print ("--------")
print ("NHAC NHO AE:")
print ("AE WAY TAY IT THOI NHA :))")
print ("")
print ("--------")
print ("Cach lay WARP+ ID:")
print ("B1: Vao setting trong app 1.1.1.1")
print ("B2: Chon Advanced => Diagnostics")
print ("B3: Sao chep ID trong phan Client configuration xong dan vao tool")
referrer = input("[#] NHAP WARP+ ID:")

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "vn_VN"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + " By HUNGNOPRO")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.3)
			sys.stdout.write("\r[+] DANG LAM VIEC... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] DANG THUC HIEN ID: {referrer}")    
		print(f"[:)] {g} GB DA DUOC THEM VAO TAI KHOAN CUA BAN.")
		print(f"[#] Ket qua: {g} OK {b} LOI")
		print ("--------")
		print("NHAP LAI LICENSE KEY CUA BAN DE NHAN KET QUA.")
		print(" ")
		print ("--------")
		print("[*] SAU 15S, TIEP TUC THUC HIEN.")
		print("[?] VUI LONG CHO DE SERVER KHONG BI QUA TAI.")
		print ("--------")
		
		time.sleep(15)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("            WARP-PLUS-CLOUDFLARE (script)" + " By HUNGNOPRO")
		print("")
		print("[:(] LOI KET NOI TOI SERVER.")
		print(f"[#] Total: {g} OK {b} LOI")
        