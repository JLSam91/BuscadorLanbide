#!/usr/bin/env python
# -*- coding: utf8 -*-

# Imports

import json
import datetime
from api import obtenerDatos

# Funciones

def Datos():
    datos = obtenerDatos()
    datosBuenos = datos.getDatos()
    return datosBuenos

def Macrofuncion(**kwargs):
    datos = Datos()
    lista = datos
    diasSemana = []
    longitudSemana = 0

    for i in kwargs.keys():
        if i == "codigo":
            lista = codigo(datos, kwargs["codigo"])
        else: 
            lista = lista
        
        if i == "titulo":
            lista = titulo(lista, kwargs["titulo"])
        
        else: 
            lista = lista

        if i == "municipio":
            lista = municipio(lista, kwargs["municipio"])
        
        else: 
            lista = lista

        if i == "centro":
            lista = centro(lista, kwargs["centro"])
        
        else: 
            lista = lista

        if i == "fin":
            lista = fin(lista, kwargs["fin"])
        
        else: 
            lista = lista

        if i == "inicio":
            lista = inicio(lista, kwargs["inicio"])
        
        else: 
            lista = lista

        if i == "horas":
            lista = horas(lista, kwargs["horas"])
        
        else: 
            lista = lista

        if i == "colectivo":
            lista = colectivo(lista, kwargs["colectivo"])
        
        else: 
            lista = lista

        if i == "modalidad":
            lista = modalidad(lista, kwargs["modalidad"])
        
        else: 
            lista = lista

        if i == "codprov":
            lista = codprov(lista, kwargs["codprov"])
        
        else: 
            lista = lista

        if i == "codmuni":
            lista = codmuni(lista, kwargs["codmuni"])
        
        else: 
            lista = lista

        if i == "hora_ini_m":
            lista = horarioMañana(lista, kwargs["hora_ini_m"])
        else:
            lista = lista 
        
        if i == "hora_fin_m":
            lista = horarioMañana(lista, None, kwargs["hora_fin_m"])
        else:
            lista = lista 

        if i == "hora_ini_t":
            lista = horarioTarde(lista, kwargs["hora_ini_t"])
        else:
            lista = lista 
        
        if i == "hora_fin_t":
            lista = horarioTarde(lista, None, kwargs["hora_fin_t"])
        else:
            lista = lista 

    for i in kwargs.keys():
        if i == "lunes":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 0:      
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "martes":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 1:
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "miercoles":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 2:
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "jueves":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 3:
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "viernes":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 4:
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "sabado":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 5:
        diasSemana.append(0)
        longitudSemana += 1

    for i in kwargs.keys():
        if i == "domingo":
            diasSemana.append(1)
            longitudSemana += 1
    if longitudSemana == 6:
        diasSemana.append(0)
        longitudSemana += 1

    if 1 in diasSemana and longitudSemana == 7:
            
        lista = diadelasemana(lista, L = diasSemana[0], M = diasSemana[1], X = diasSemana[2], J = diasSemana[3], V = diasSemana[4], S = diasSemana[5], D = diasSemana[6])

    else:
        lista = lista

    return lista
        

def codigo(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el código indicado. 
    En caso de no especificar un código, devolver todos los cursos.
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["codigo"] == valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista

def titulo(datos, valor = None):
    """
    Devuelve la estructura datos que contenga en su título el valor indicado. 
    En caso de no especificar nada en valor, devolver todos los títulos.
    """
    if valor is not None:
        lista = []
        for i in datos:
            if valor.upper() in i["titulo"].upper():
                lista.append(i)
    else: 
        lista = datos 
    return lista
def municipio(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el municipio indicado.
    En caso de no indicar valor, devolver los cursos de todos los municipios
    """
    if valor is not None:
        lista = []
        for i in datos:
            if valor.upper() in i["municipio"].upper():
                lista.append(i)
    else: 
        lista = datos 
    return lista
def centro(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el centro indicado. 
    En caso de no especificar un centro en concreto, devolver todos los cursos    
    """
    if valor is not None:
        lista = []
        for i in datos:
            if valor.upper() in i["centro"].upper():
                lista.append(i)
    else: 
        lista = datos 
    return lista

def fin(datos, valor = None):
    """
    Devuelve la estructura datos que contenga cursos ANTERIORES a fecha fin
    Se debe indicar una fecha, hasta la cual se puede asistir al curso.
    Debe ir en formato cadena "DD/MM/YYYY"
    """
    if valor is not None:
        lista = []
        for i in datos:
            if datetime.date(int(i["f_fin"][6:]), int(i["f_fin"][3:5]), int(i["f_fin"][0:2])) <= datetime.date(int(valor[6:]), int(valor[3:5]), int(valor[0:2])):
                lista.append(i)
    else: 
        lista = datos 
    return lista

def inicio(datos, valor = None):
    """
    Devuelve la estructura datos que contenga cursos POSTERIORES a fecha inicio
    Se debe indicar una fecha, a partir de la cual se puede asistir al curso.
    Debe ir en formato cadena "DD/MM/YYYY"    
    """
    if valor is not None:
        lista = []
        for i in datos:
            if datetime.date(int(i["f_inicio"][6:]), int(i["f_inicio"][3:5]), int(i["f_inicio"][0:2])) >= datetime.date(int(valor[6:]), int(valor[3:5]), int(valor[0:2])):
                lista.append(i)
    else: 
        lista = datos 
    return lista

def horas(datos, valor = None):
    """
    Devuelve la estructura datos que contenga cursos de menor o igual número de horas.
    Valor será un entero. 
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["horas"] <= valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista

def colectivo(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el código indicado
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["colectivo"] == valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista
def modalidad(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el código indicado
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["modalidad"] == valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista

def codprov(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el código provincial indicado
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["codprov"] == valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista

def codmuni(datos, valor = None):
    """
    Devuelve la estructura datos que contenga el código municipal indicado
    """
    if valor is not None:
        lista = []
        for i in datos:
            if i["codmuni"] == valor:
                lista.append(i)
    else: 
        lista = datos 
    return lista

def diadelasemana(datos, L = 0, M = 0, X = 0, J = 0, V = 0, S = 0, D = 0):
    """
    Devuelve la estructura datos que contenga los cursos que se impartan los días de la semana que yo puedo asistir
    """
    lista = []
    for i in datos:
        if str(i["lunes"]) == str(L) and str(i["martes"]) == str(M) and str(i["miercoles"]) == str(X) and str(i["jueves"]) == str(J) and str(i["viernes"]) == str(V) and str(i["sabado"]) == str(S) and str(i["domingo"]) == str(D):
            lista.append(i)
    return lista

def horarioMañana(datos, h_inicio = None, h_fin = None):
    lista = []
    if h_inicio is not None and h_fin is None:
        for i in datos:
            try:
                if datetime.time(int(i["hora_ini_m"][0:2]), int(i["hora_ini_m"][3:])) >= datetime.time(int(h_inicio[0:2]),int(h_inicio[3:])):
                    lista.append(i)
            except: 
                continue
                
        return lista
    
    if h_inicio is None and h_fin is not None:
        for i in datos:
            try:
                if datetime.time(int(i["hora_fin_m"][0:2]), int(i["hora_fin_m"][3:])) <= datetime.time(int(h_fin[0:2]),int(h_fin[3:])):
                    lista.append(i)
            except:
                continue

        return lista

    if h_inicio is not None and h_fin is not None:
        for i in datos:
            try:

                if datetime.time(int(i["hora_ini_m"][0:2]), int(i["hora_ini_m"][3:])) >= datetime.time(int(h_inicio[0:2]),int(h_inicio[3:])) and datetime.time(int(i["hora_fin_m"][0:2]), int(i["hora_fin_m"][3:])) <= datetime.time(int(h_fin[0:2]),int(h_fin[3:])):
                    lista.append(i)
            except:
                continue

        return lista

def horarioTarde(datos, h_inicio = None, h_fin = None):
    lista = []
    if h_inicio is not None and h_fin is None:
        for i in datos:
            try:
                if datetime.time(int(i["hora_ini_t"][0:2]), int(i["hora_ini_t"][3:])) >= datetime.time(int(h_inicio[0:2]),int(h_inicio[3:])):
                    lista.append(i)
            except: 
                continue
                
        return lista
    
    if h_inicio is None and h_fin is not None:
        for i in datos:
            try:
                if datetime.time(int(i["hora_fin_t"][0:2]), int(i["hora_fin_t"][3:])) <= datetime.time(int(h_fin[0:2]),int(h_fin[3:])):
                    lista.append(i)
            except:
                continue

        return lista

    if h_inicio is not None and h_fin is not None:
        for i in datos:
            try:

                if datetime.time(int(i["hora_ini_t"][0:2]), int(i["hora_ini_t"][3:])) >= datetime.time(int(h_inicio[0:2]),int(h_inicio[3:])) and datetime.time(int(i["hora_fin_m"][0:2]), int(i["hora_fin_m"][3:])) <= datetime.time(int(h_fin[0:2]),int(h_fin[3:])):
                    lista.append(i)
            except:
                continue

        return lista
    




if __name__ == "__main__":
    # Programa principal
    datos = json.load(open("JsonData.json"))
    #print(datos)
    # print(datos[0].keys())
    # cursos = horarioMañana(datos, "08:30", "12:00")
    # print(cursos)
    datos = Datos()