#!/usr/bin/python

import requests
import json
import re
from lxml import html

def GetGibertJoseph( EAN ):
   "This function gets the price for gibertjoseph"
   url = 'http://www.gibertjoseph.com/sao/sao/addProduct/?isAjax=true'
   resp = requests.post(url=url, data = {'codes':EAN, 'form_key':'FY1U0HnY0YzCBv3W'})
   #print resp.text
   prices=re.findall("([0-9.]+)&nbsp;&euro;", resp.text)
   if prices:
     Val=prices[0]
   else:
     Val="0.0"

   return Val


#v=GetGibertJoseph("9782081395534")
#print 'Value of 9782081395534 is '+ v +"\n"

