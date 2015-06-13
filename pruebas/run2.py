from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, random, os
import numpy as np


## ALMACENA LISTA DE ARCHIVOS
Simulations = ["20-FS", "50-FS", "100-FS", "20-LNS", "50-LNS", "100-LNS", "20-NAK", "50-NAK", "100-NAK", "20-NAK", "50-NAK", "100-NAK",]
FilesList = []									  
for file_ in os.listdir("/home/william/Simulators/statistics/222/"):
	for k in Simulations:
	    if k in file_:
			FilesList.append(file_)  	
			#print(file_) #MUESTRA TODOS LOS FILES EN LA CARPETA
			print FilesList   #MUESTRA TODOS LOS FILES GUARDADOS EN LA LISTA 


###########################Lo Manetengo solo como prueba
"""
for i in FilesList:
	print i
	csvfile = csv.reader(open(i, 'r'))
	csvfile.next()
	csvlist=list(csvfile)
	csvarray=np.array(csvlist)
	finalarray = csvarray[0:,1:].astype(np.float32)
	mean = finalarray.mean()
	#x,y = finalarray.shape
	desvest = np.std(finalarray, ddof=1)
	print mean, desvest
"""
#########################


## CREACION DE DICT DONDE SE GUARDARAN LOS VALORES DE LA SIMULACON 
ValTypeSim= defaultdict(list)						

for f in FilesList:
	csvfile = csv.DictReader(open(f, 'r'))   ## ABRE EL ARCHIVO A LEER EN FORMATO DICT
	Headers = csvfile.fieldnames		     ## GUARDA LOS HEADERS
	TypeSimBase = ['AODV', 'DSR', 'DYMO', 'OLSR', 'nombre', 'apellido', 'direxion', 'loc']
## LO ANTERIOR SON TODAS LAS POSIBLES SIMULACIONES, TODAS LAS OPCIONES DE PROTOCO-PATH-CANTNODOS
	TypeSim = []
	for i in TypeSimBase:					 ## GUARDA EL TIPO DE SIMULACION PROT-PATH-CANTNODOS
	 	for j in Headers:
			if (i in j) and (i not in TypeSim):
				TypeSim.append(i)
	#print TypeSim

    ## ANALISIS DE CADA FILA DEL "row"=(KEY, VALUE), Y SI TIENE AODV, DSR, ETC..., ES UN DICT(BASE O KEY) PARA C/U DE LOS CSV
	for row in csvfile:									
		for k, v in row.items():
			for i in TypeSim:
				if i in k:
					ValTypeSim[i].append(v)			
	#print ValTypeSim.items()
	#print ValTypeSim.values()
"""
ValueMeans = []
ValueDeStd = []
ValueNames = []

for k in ValTypeSim:
	print k #, ValTypeSim[k]	
	MATRIX = np.array(ValTypeSim[k]).astype(np.float64)
	#x,y = finalarray.shape
	mean = MATRIX.mean()
	desvest = np.std(MATRIX, ddof=1)
	ValueNames.append(k)
	ValueMeans.append(mean)
	ValueDeStd.append(desvest)
	print mean, desvest
	#print ValueMeans, ValueDeStd, ValueNames

N=len(ValueNames)
ind = np.arange(N)
width = 0.5
color = ['r', 'g', 'y', 'c', 'b']
fig = plt.figure()
sub1 = fig.add_subplot(111)
i=0
for k in ValueMeans:
	p1 = plt.bar(ind[i], k, width, color=color[i], label=ValueNames[i], yerr=ValueDeStd[i])
	i+=1

plt.ylabel('E2ED in seconds')
plt.title('Average E2ED (Free Space Pathloss)')
plt.xticks(ind+width/2., ValueNames)
y_maximo = 1.4*max(np.sum([ValueMeans, ValueDeStd], axis=0))
plt.yticks(np.arange(0,y_maximo,y_maximo/10.))
sub1.legend(loc=0, prop={'size':10.5})
plt.savefig('prueba1.png', format='png')
sub1.set_ylim((0, y_maximo))
plt.show()

"""





