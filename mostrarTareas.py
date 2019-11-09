"""
Julian Guillermo Zapata Rugeles
2019
uso:
	Breve script que abre un documento de excel
	lee sus lineas y genera un reporte usando notify-send
	implementado para Ubuntu

	windows:
		se debe instalar a travez de pip win10toast
		y sustituir en la linea 28 (c="notify-send '"+lista[x]+"'")
		con la respectiva orden para generar el mensaje en pantalla
		dificultad :
		**	Facil	**



"""
#importamos 
import time
import os
import pandas as pd 

#inicio del programa 
def iniciar():

	read_file=pd.ExcelFile('main.xls') #abre el documento main.xls (se puede reemplazar)
	hoja=read_file.parse('main') #nombre de la hoja donde se leera.(alojada en el archivo, hoja1,hoja2,..etc)
	string_convert=str(hoja)
	lista=string_convert.split('\n') #se genera una lista para iterar
	for x in range(1,len(lista)): #inicia el ciclo desde el elemento 1 hasta el N
		run="notify-send '"+lista[x]+"'" #genera el comando en gnu_linux
		os.system(run)
		time.sleep(2.5) #tiempo de espera luego de cada notificacion.

if __name__ == '__main__':
	iniciar()