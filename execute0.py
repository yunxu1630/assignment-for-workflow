# WPS Execute Operation

import requests, os

#payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\buffer_geojson.xml").read()
#payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\coords_transform.xml").read()
#payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\centroid_reference.xml").read()


#wpsServerUrl = "http://130.89.221.193:85/geoserver/ows?"
#wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s6039774/gpw/wps.py?" # Use your SNUMBER

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\geom_intersection.xml").read()
wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s6039774/gpw/wps.py?" 

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)