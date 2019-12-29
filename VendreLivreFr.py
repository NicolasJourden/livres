#!/usr/bin/python

import requests
import json
import re
from lxml import html

def VendreLivreFr( EAN ):
   "This function gets the price for vendre-livre.fr"
   url = 'https://vendre-livre.fr/recherche.php?recherche='+EAN+'&id_recherche=411111111159997'
   print (url)
   resp = requests.get(url=url, verify=False)
   tree = html.fromstring(resp.text)
   cols = tree.xpath('//span[@class="style4"]/text()')
   print cols
   Val = cols[0]

   return Val

#v=VendreLivreFr("978-2081395534")
#print 'Value of 978-2081395534 is '+ v +"\n"

