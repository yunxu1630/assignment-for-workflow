# WPS Execute Operation

import requests, os

#payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\chaining_cen.xml").read()
#payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\chaining_cen_buff.xml").read()
payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\chaining_cen_buff_inter_length.xml").read()


wpsServerUrl = "http://130.89.221.193:85/geoserver/ows?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)