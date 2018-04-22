#!/usr/bin/python

import requests
import json
import pprint
import re
from GibertJeune import GetGibertJeune
from GibertJoseph import GetGibertJoseph
from chapitre_com import GetChapitreCom

print "ISBN\tGibertJeune\tChapitre.com\tGibertJoseph"

file = open("isbn.list", "r") 

for line in file:
   ISBN = str(re.sub('[^0-9\-]+', '', line))

   gib = GetGibertJeune(ISBN)
   gij = GetGibertJoseph(ISBN)
   cha = GetChapitreCom(ISBN)

   print ISBN +"\t"+ gib +"\t"+ cha +"\t"+ gij 
 
file.close()

