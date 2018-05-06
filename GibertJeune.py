#!/usr/bin/python

import requests
import json
import re
from lxml import html

def GetGibertJeune( EAN ):
   "This function gets the price for gibertjeune"
   url = 'https://www.gibertjeune.fr/revendez-vos-livres/'
#   print (url)
   resp = requests.post(url=url, data = {'input':EAN}, verify=False)
   tree = html.fromstring(resp.text)
   cols = tree.xpath('//tr[@id="last-item"]/td/text()')
   if len(cols):
     v1=re.sub('[^0-9,]+', '', cols[7])
     Val=re.sub('[,]+', '.', v1)
   else:
     Val="0.0"


   return Val

#v=GetGibertJeune("9782081395534")
#print 'Value of 9782081395534 is '+ v +"\n"

