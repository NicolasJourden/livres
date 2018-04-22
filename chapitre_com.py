#!/usr/bin/python

import requests
import json
import re

def GetChapitreCom( EAN ):
   "This function gets the price for chapitre.com"
#  DATA='jQuery111308934837578997339_1523612400788( {"ReturnCode":0,"TakeBackOffer":{"Auteur":"Zeniter, Alice","Collection":"LITTERATURE FRANCAISE FLAMMARION","DateParution":"\/Date(1502834400000+0200)\/","EAN13":"9782081395534","Editeur":"FLAMMARION","PrixPublic":22.00,"PrixReprise":3.30,"Titre":"l\'art de perdre","UrlImage":"http:\/\/www.images-chapitre.com\/indispo\/vi_chap.gif"}} );';

   url = 'http://revendreunlivre.chapitre.com/furet/BabelMobile.svc/scan?callback=jQuery111308934837578997339_1523612400788&appid=3E1EF7F2-9BB4-4106-8096-CD129D39FBA9&ean='+EAN+'&_=1523612400791'
#   print (url)

   resp = requests.get(url=url)
   Val=re.sub(r'jQuery.*\( (.*) \);', r'\1', resp.text)
#   print ('---' + Val + '---')
   parsed_json = json.loads(Val)

   return str(parsed_json['TakeBackOffer']['PrixReprise'])


#v=GetChapitreCom("9782081395534")
#print 'Value of 9782081395534 is '+ str(v)+"\n"

