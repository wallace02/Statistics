import sys
from threading import Thread
from collections import defaultdict
import matplotlib.pyplot as plt
import csv, random, os
import numpy as np

def main():
	FilesList = ListOfFiles()
	#print FilesList

	print "Path Loss: LNS, TRG, NAK, FS"
	opcao = raw_input("Ingrese opcion: ")
	ByPathLoss = FiltroByPathLoss(FilesList, opcao)
	#print ByPathLoss.items()

	ByNodes20, ByNodes50, ByNodes100, ByNodes150 = FiltroByNodes(ByPathLoss)
	#print ByNodes20.items(), ByNodes50.items(), ByNodes100.items(), ByNodes150.items()

	Statistics(ByPathLoss)


def ListOfFiles():
	FilesList = []									  
	for file_ in os.listdir("/home/william/Simulators/statistics/pruebas/"):
	    if file_.endswith(".csv"):
			FilesList.append(file_)  	
			#print(file_) #MUESTRA TODOS LOS FILES EN LA CARPETA
			#print FilesList   #MUESTRA TODOS LOS FILES GUARDADOS EN LA LISTA 
	return FilesList

def FiltroByPathLoss(FilesList, opcao):
	Filtro = ['-FS-','-LNS-','-NAK-','-TRG-']
	for i in Filtro:
		if opcao in i:
			opcao = i	
	
	FSPL= defaultdict(list)
	LNSPL= defaultdict(list)
	NAKPL= defaultdict(list)
	TRGPL= defaultdict(list)
	ByPathLoss = defaultdict(list)
	for f in FilesList:
		csvfile = csv.DictReader(open(f, 'r'))   ## ABRE EL ARCHIVO A LEER EN FORMATO DICTReader
		for row in csvfile:									
			for k, v in row.items():
				if opcao in k and (opcao == '-FS-'):
					FSPL[k].append(v)
				if opcao in k and (opcao == '-LNS-'):
					LNSPL[k].append(v)
				if opcao in k and (opcao == '-NAK-'):
					NAKPL[k].append(v)
				if opcao in k and (opcao == '-TRG-'):
					TRGPL[k].append(v)
	if opcao == '-FS-':
		ByPathLoss = FSPL
	if opcao == '-LNS-':
		ByPathLoss = LNSPL
	if opcao == '-NAK-':
		ByPathLoss = NAKPL
	if opcao == '-TRG-':
		ByPathLoss = TRGPL
	return ByPathLoss

				
def FiltroByNodes(ByPathLoss):
	Filtro = ['-20-','-50-','-100-','-150-']
	C20Nodes= defaultdict(list)
	C50Nodes= defaultdict(list)
	C100Nodes= defaultdict(list)
	C150Nodes= defaultdict(list)
	for k, v in ByPathLoss.items():
		for i in Filtro:
			if i in k and (i == '-20-'):
				C20Nodes[k].append(v)
			if i in k and (i == '-50-'):
				C50Nodes[k].append(v)
			if i in k and (i == '-100-'):
				C100Nodes[k].append(v)
			if i in k and (i == '-150-'):
				C150Nodes[k].append(v)
	#print C20Nodes.items()
	#print C50Nodes.items()
	#print C100Nodes.items()
	#print C150Nodes.items()
	return C20Nodes, C50Nodes, C100Nodes, C150Nodes

def Statistics(ByPathLoss):
	FiltProt = ['-AODV-','-DSR-','-DYMO-','-OLSR-']
	FiltNodes = ['-20-','-50-','-100-','-150-']
	AODV20 = AODV50 = AODV100 = AODV150 = defaultdict(list)
	DSR20 = DSR50 = DSR100 = DSR150 = defaultdict(list)
	DYMO20 = DYMO50 = DYMO100 = DYMO150 = defaultdict(list)
	OLSR20 = OLSR50 = OLSR100 = OLSR150 = defaultdict(list)
	for k, v in ByPathLoss.items():
		for i in FiltProt:
			if i in k and (i == '-AODV-'):
				for j in FiltNodes:
					if j in k and (j == '-20-'):
						AODV20[k].append(v)
					if j in k and (j == '-50-'):
						AODV50[k].append(v)
					if j in k and (j == '-100-'):
						AODV100[k].append(v)
					if j in k and (j == '-150-'):
						AODV150[k].append(v)				
			if i in k and (i == '-DSR-'):
				for j in FiltNodes:
					if j in k and (j == '-20-'):
						DSR20[k].append(v)
					if j in k and (j == '-50-'):
						DSR50[k].append(v)
					if j in k and (j == '-100-'):
						DSR100[k].append(v)
					if j in i and (j == '-150-'):
						DSR150[k].append(v)			
			if i in k and (i == '-DYMO-'):
				for j in FiltNodes:
					if j in k and (j == '-20-'):
						DYMO20[k].append(v)	
					if j in k and (j == '-50-'):
						DYMO50[k].append(v)
					if j in k and (j == '-100-'):
						DYMO100[k].append(v)
					if j in k and (j == '-150-'):
						DYMO150[k].append(v)			
			if i in k and (i == '-OLSR-'):
				for j in FiltNodes:
					if j in k and (j == '-20-'):
						OLSR20[k].append(v)
					if j in k and (j == '-50-'):
						OLSR50[k].append(v)
					if j in k and (j == '-100-'):
						OLSR150[k].append(v)
					if j in k and (j == '-150-'):
						OLSR100[k].append(v)			
	print AODV20.items()

main()

