import sys
from threading import Thread
from collections import defaultdict
import matplotlib.pyplot as plt
import csv, random, os, copy
import numpy as np


def main():
	FilesList = ListOfFiles()
	print "FilesList"
	print FilesList, "\n"

	print "Path Loss: LNS, TRG, NAK, FS"
	opcao = raw_input("Ingrese opcion: ")
	ByPathLoss = FiltroByPathLoss(FilesList, opcao)
	#print "ByPathLoss", type(ByPathLoss)
	#print ByPathLoss.items(), "\n"
	#print len(ByPathLoss)


def ListOfFiles():
	FilesList = []									  
	for file_ in os.listdir("/home/william/Simulators/Statistics/simulation_data/ALL/LNS"):
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
			break	

	AODV25E2ED, AODV25RATE, AODV50E2ED, AODV50RATE, AODV75E2ED, AODV75RATE, AODV100E2ED, AODV100RATE  = [defaultdict(list) for dummy in range(8)]
	DSR25E2ED, DSR25RATE, DSR50E2ED, DSR50RATE, DSR75E2ED, DSR75RATE, DSR100E2ED, DSR100RATE  = [defaultdict(list) for dummy in range(8)]
	DYMO25E2ED, DYMO25RATE, DYMO50E2ED, DYMO50RATE, DYMO75E2ED, DYMO75RATE, DYMO100E2ED, DYMO100RATE  = [defaultdict(list) for dummy in range(8)]
	OLSR25E2ED, OLSR25RATE, OLSR50E2ED, OLSR50RATE, OLSR75E2ED, OLSR75RATE, OLSR100E2ED, OLSR100RATE  = [defaultdict(list) for dummy in range(8)]
	Recived='rcvdPk'
	Sent='sentPk'
	E2ED='E2ED'
	for f in FilesList:
		csvfile = csv.DictReader(open(f, 'r'))   ## ABRE EL ARCHIVO A LEER EN FORMATO DICTReader
		for row in csvfile:
			for k, v in row.iteritems():
				if opcao in k:
					if 'AODVRouting-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								AODV25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								AODV25RATE[Recived].append(v)
							if 'sentPk' in k:
								AODV25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								AODV50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								AODV50RATE[Recived].append(v)
							if 'sentPk' in k:
								AODV50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								AODV75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								AODV75RATE[Recived].append(v)
							if 'sentPk' in k:
								AODV75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								AODV100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								AODV100RATE[Recived].append(v)
							if 'sentPk' in k:
								AODV100RATE[Sent].append(v)
					elif 'DSRUU-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								DSR25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DSR25RATE[Recived].append(v)
							if 'sentPk' in k:
								DSR25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								DSR50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DSR50RATE[Recived].append(v)
							if 'sentPk' in k:
								DSR50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								DSR75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DSR75RATE[Recived].append(v)
							if 'sentPk' in k:
								DSR75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								DSR100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DSR100RATE[Recived].append(v)
							if 'sentPk' in k:
								DSR100RATE[Sent].append(v)
					elif 'DYMOUM-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								DYMO25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DYMO25RATE[Recived].append(v)
							if 'sentPk' in k:
								DYMO25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								DYMO50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DYMO50RATE[Recived].append(v)
							if 'sentPk' in k:
								DYMO50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								DYMO75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DYMO75RATE[Recived].append(v)
							if 'sentPk' in k:
								DYMO75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								DYMO100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								DYMO100RATE[Recived].append(v)
							if 'sentPk' in k:
								DYMO100RATE[Sent].append(v)
					elif 'OLSR-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								OLSR25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								OLSR25RATE[Recived].append(v)
							if 'sentPk' in k:
								OLSR25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								OLSR50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								OLSR50RATE[Recived].append(v)
							if 'sentPk' in k:
								OLSR50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								OLSR75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								OLSR75RATE[Recived].append(v)
							if 'sentPk' in k:
								OLSR75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								OLSR100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								OLSR100RATE[Recived].append(v)
							if 'sentPk' in k:
								OLSR100RATE[Sent].append(v)
	AODV = [AODV25E2ED, AODV25RATE, AODV50E2ED, AODV50RATE, AODV75E2ED, AODV75RATE, AODV100E2ED, AODV100RATE]
	DSR = [DSR25E2ED, DSR25RATE, DSR50E2ED, DSR50RATE, DSR75E2ED, DSR75RATE, DSR100E2ED, DSR100RATE]
	DYMO = [DYMO25E2ED, DYMO25RATE, DYMO50E2ED, DYMO50RATE, DYMO75E2ED, DYMO75RATE, DYMO100E2ED, DYMO100RATE]
	OLSR = [OLSR25E2ED, OLSR25RATE, OLSR50E2ED, OLSR50RATE, OLSR75E2ED, OLSR75RATE, OLSR100E2ED, OLSR100RATE]
	Protocolos = [AODV,DSR,DYMO,OLSR]

	AODVMean, AODVDesv, AODVPDR, DYMOMean, DYMODesv, DYMOPDR, OLSRMean, OLSRDesv, OLSRPDR, DSRMean, DSRDesv, DSRPDR  = [[0]*4 for dummy in range(12)]

	Statistics(AODV, AODVMean, AODVDesv, AODVPDR)
	#print AODVMean
	#print AODVDesv
	Statistics(DSR, DSRMean, DSRDesv, DSRPDR)
	#print DSRMean
	#print DSRDesv
	#Statistics(DYMO, DYMOMean, DYMODesv, DYMOPDR)
	#print DYMOMean
	#print DYMODesv
	#Statistics(OLSR, OLSRMean, OLSRDesv, OLSRPDR)
	#print OLSRMean
	#print OLSRDesv
	
	XAxis = [25, 50, 75, 100]
	TODO=[AODVMean,DSRMean,DYMOMean,OLSRMean]
	TODODesv=[AODVDesv,DSRDesv,DYMODesv,OLSRDesv]
	TODOPDR=[AODVPDR,DSRPDR,DYMOPDR,OLSRPDR]
	
	label=["AODV","DSR","DYMO","OLSR"]
	marker=['*','p','o','D']
	
	fig = plt.figure(figsize=(20, 10)) 
	subplot1 = fig.add_subplot(1, 1, 1)
	i=0
	while i<4:
		subplot1.errorbar(XAxis,TODO[i],yerr=TODODesv[i], label=label[i], marker = marker[i])
		i+=1
	
	subplot1.legend(loc='upper left', ncol = 1, prop={'size':20})
	subplot1.set_xlim((0, 125))
	subplot1.set_ylim((0, 10))
	plt.title('Impact on Protocols over Free-Space Pathloss', fontsize=20)
	plt.ylabel('E2ED in seconds', fontsize=20)
	plt.xlabel('Quantity of Nodes', fontsize=20)
	
	# major ticks every 25, minor ticks every 5 en el eje X                                   
	major_ticksx = np.arange(0, 126, 25)
	minor_ticksx = np.arange(0, 126, 5)
	# major ticks every 1, minor ticks every 0.25 en el eje Y
	major_ticksy = np.arange(0, 10.1, 1)
	minor_ticksy = np.arange(0, 10, 0.25)
	#Dibujar en el plot
	subplot1.set_xticks(major_ticksx) 
	subplot1.set_xticks(minor_ticksx, minor=True)
	subplot1.set_yticks(major_ticksy)
	subplot1.set_yticks(minor_ticksy, minor=True)
	# 		and a corresponding grid on both axes                                                    
	#		subplot1.grid(which='both')
	# differnet settings for the grids:                               
	subplot1.grid(which='minor', alpha=0.4)
	subplot1.grid(which='major', alpha=0.9, linewidth=1.1)
	plt.show()

	


	figProt = plt.figure(figsize=(20, 10)) 
	subplot2 = figProt.add_subplot(1, 1, 1)
	i=0
	while i<4:
		subplot2.errorbar(XAxis,TODOPDR[i], label=label[i], marker = marker[i])
		i+=1
	
	subplot2.legend(loc='upper left', ncol = 1, prop={'size':20})
	subplot2.set_xlim((0, 125))
	subplot2.set_ylim((0, 0.5))
	plt.title('Impact on Protocols over Free-Space Pathloss', fontsize=20)
	plt.ylabel('Packet Delivery Rate', fontsize=20)
	plt.xlabel('Quantity of Nodes', fontsize=20)
	
	# major ticks every 25, minor ticks every 5 en el eje X                                   
	major_ticksx = np.arange(0, 126, 25)
	minor_ticksx = np.arange(0, 126, 5)
	# major ticks every 1, minor ticks every 0.25 en el eje Y
	major_ticksy = np.arange(0, 1.001, 0.1)
	minor_ticksy = np.arange(0, 1.001, 0.025)
	#Dibujar en el plot
	subplot2.set_xticks(major_ticksx) 
	subplot2.set_xticks(minor_ticksx, minor=True)
	subplot2.set_yticks(major_ticksy)
	subplot2.set_yticks(minor_ticksy, minor=True)
	# 		and a corresponding grid on both axes                                                    
	#		subplot1.grid(which='both')
	# differnet settings for the grids:                               
	subplot2.grid(which='minor', alpha=0.4)
	subplot2.grid(which='major', alpha=0.9, linewidth=1.1)
	plt.show()

	return

def Statistics(Prot,ProtMeans,ProtDesvs,ProtPDR):
	sumS, sumR = [[0]*4 for dummy in range(2)]
	m=0
	for i in Prot:
		if m == 0:
			M = np.array(i.values()).astype(np.float64)
			mean = M.mean()
			desvest = np.std(M, ddof=1)
			ProtMeans[0]=mean
			ProtDesvs[0]=desvest
			m+=1
		elif m == 1:
			for k,v in i.iteritems():
				if 'rcvdPk' in k:
					M = np.array(v).astype(np.float64)
					sumR[0] = np.sum(M)
				if 'sentPk' in k:
					M = np.array(v).astype(np.float64)
					sumS[0] = np.sum(M)
			ProtPDR[0]=sumR[0]/sumS[0]
			m+=1
		elif m == 2:
			M = np.array(i.values()).astype(np.float64)
			mean = M.mean()
			desvest = np.std(M, ddof=1)
			ProtMeans[1]=mean
			ProtDesvs[1]=desvest
			m+=1
		elif m == 3:
			for k,v in i.iteritems():
				if 'rcvdPk' in k:
					M = np.array(v).astype(np.float64)
					sumR[1] = np.sum(M)
				if 'sentPk' in k:
					M = np.array(v).astype(np.float64)
					sumS[1] = np.sum(M)
			ProtPDR[1]=sumR[1]/sumS[1]
			m+=1
		elif m == 4:
			M = np.array(i.values()).astype(np.float64)
			mean = M.mean()
			desvest = np.std(M, ddof=1)
			ProtMeans[2]=mean
			ProtDesvs[2]=desvest
			m+=1
		elif m == 5:
			for k,v in i.iteritems():
				if 'rcvdPk' in k:
					M = np.array(v).astype(np.float64)
					sumR[2] = np.sum(M)
				if 'sentPk' in k:
					M = np.array(v).astype(np.float64)
					sumS[2] = np.sum(M)
			ProtPDR[2]=sumR[2]/sumS[2]
			m+=1
		elif m == 6:
			M = np.array(i.values()).astype(np.float64)
			mean = M.mean()
			desvest = np.std(M, ddof=1)
			ProtMeans[3]=mean
			ProtDesvs[3]=desvest
			m+=1
		elif m == 7:
			for k,v in i.iteritems():
				if 'rcvdPk' in k:
					M = np.array(v).astype(np.float64)
					sumR[3] = np.sum(M)
				if 'sentPk' in k:
					M = np.array(v).astype(np.float64)
					sumS[3] = np.sum(M)
			#ProtPDR[3]=sumR[3]/sumS[3]
			m+=1
	#print ProtMeans
	#print ProtDesvs
	#print PDR
	return

main()
