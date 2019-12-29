#!/usr/bin/python

import requests
import json
import pprint
import re

def momoFr( EAN ):
   "This function gets the price for momox.fr"

   s = requests.Session()
   s.get('https://www.momox.fr', verify=False)
   s.get('https://www.momox.fr/offer/'+EAN, verify=False)
   r = s.get('https://api.momox.fr/api/latest/find/media/ean/'+EAN, verify=False)

   print(r.text)

#   resp = requests.get(url=url)
#   tree = html.fromstring(resp.text)
#   cols = tree.xpath('//tr[@id="last-item"]/td/text()')

   #Val=re.sub(r'jQuery.*\( (.*) \);', r'\1', resp.text)
   #print ('---' + Val + '---')
   #parsed_json = json.loads(Val)
   #print(json.dumps(parsed_json))
   #print(parsed_json['TakeBackOffer']['PrixPublic'])

   return 0.0

#v=momoFr("978-2081395534")
#print 'Value of 978-2081395534 is '+ str(v)+"\n"

