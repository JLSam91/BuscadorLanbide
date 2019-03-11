#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:20:16 2019

@author: oscar
"""

from requests import get
import argparse
import json

class obtenerDatos(object):
	
	def getDatos(self):
		r=get(self.url)
		if r.status_code == 200:
			data=(r.text)
			data=data[7:]
			data=data[:-2]
			jdata = json.loads(data)
			
			return jdata
			
		else:
			raise Exception("La Url indicada no existe")
	

	def __init__(self, **kwargs):
		if ((not 'url' in kwargs.keys()) or (kwargs['url']=='')):
			self.url='http://apps.lanbide.euskadi.net/apps/FR_CURSOS_ODE_JSON?jsonCallBack=nombre'
		try:
			self.getDatos()
		except:
			pass
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="Dirección URL")
	
	args = parser.parse_args()
	
	argumentos={}
	
	
		
	
	#Deja la comprobacion de los argumentos a la clase
	if args.url and args.operacion is not None:
		argumentos['url']=args.url
	
	datosObtenidos=obtenerDatos(**argumentos)