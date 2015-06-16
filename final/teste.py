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
	for file_ in os.listdir("/home/william/Simulators/Statistics/final/"):
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
	AODV=[AODV25E2ED, AODV25RATE, AODV50E2ED, AODV50RATE, AODV75E2ED, AODV75RATE, AODV100E2ED, AODV100RATE]
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

	for i in Protocolos:
		print i


			
	M00 = np.array(AODV25E2ED.values()).astype(np.float64)
	mean = M00.mean()
	desvest = np.std(M00, ddof=1)
	
	return
"""
def Statistics(ByProtocolos):
	Filtro = ['endToEndDelay','rcvdPk','sentPk']
	E2ED = defaultdict(list)
	Rate = defaultdict(list)
	Stats = defaultdict(list)
	AODVMean = [0]*4
	AODVDesv = [0]*4
	DYMOMean = [0]*4
	DYMODesv = [0]*4
	OLSRMean = [0]*4
	OLSRDesv = [0]*4
	DSRMean = [0]*4
	DSRDesv = [0]*4
	XXX = [25, 50, 75, 100]
	for k, v in ByProtocolos.iteritems():
		#print k
		for kk, vv in v.iteritems():
			#print kk
			for kkk, vvv in vv.iteritems():
				#print kkk
				for i in Filtro:
					if i in kkk and (i == 'endToEndDelay'):
						E2ED[i].append(vvv)
					if i in kkk and (i == 'rcvdPk'):
						Rate[i].append(vvv)
					if i in kkk and (i == 'sentPk'):
						Rate[i].append(vvv)
			#print E2ED, "\n"
			#print Rate, "\n"
			M = np.array(E2ED.values()).astype(np.float64)
			#print M
			mean = M.mean()
			desvest = np.std(M, ddof=1)
			#print mean, desvest
			if '25' in k:
				if 'AODV' in kk:
					AODVMean[0]=mean
					AODVDesv[0]=desvest
				if 'DYMO' in kk:
					DYMOMean[0]=mean
					DYMODesv[0]=desvest
				if 'DSR' in kk:
					DSRMean[0]=mean
					DSRDesv[0]=desvest
				if 'OLSR' in kk:
					OLSRMean[0]=mean
					OLSRDesv[0]=desvest

			if '50' in k:
				if 'AODV' in kk:
					AODVMean[1]=mean
					AODVDesv[1]=desvest
				if 'DYMO' in kk:
					DYMOMean[1]=mean
					DYMODesv[1]=desvest
				if 'DSR' in kk:
					DSRMean[1]=mean
					DSRDesv[1]=desvest
				if 'OLSR' in kk:
					OLSRMean[1]=mean
					OLSRDesv[1]=desvest

			if '75' in k:
				if 'AODV' in kk:
					AODVMean[2]=mean
					AODVDesv[2]=desvest
				if 'DYMO' in kk:
					DYMOMean[2]=mean
					DYMODesv[2]=desvest
				if 'DSR' in kk:
					DSRMean[2]=mean
					DSRDesv[2]=desvest
				if 'OLSR' in kk:
					OLSRMean[2]=mean
					OLSRDesv[2]=desvest

			if '100' in k:
				if 'AODV' in kk:
					AODVMean[3]=mean
					AODVDesv[3]=desvest
				if 'DYMO' in kk:
					DYMOMean[3]=mean
					DYMODesv[3]=desvest
				if 'DSR' in kk:
					DSRMean[3]=mean
					DSRDesv[3]=desvest
				if 'OLSR' in kk:
					OLSRMean[3]=mean
					OLSRDesv[3]=desvest

			E2ED.clear()
			Rate.clear()
	print "AODV", AODVMean, AODVDesv
	print "DSR", DSRMean, DSRDesv
	print "DYMO", DYMOMean, DYMODesv
	print "OLSR", OLSRMean, OLSRDesv
	TODO=[AODVMean,DSRMean,DYMOMean,OLSRMean]
	TODODesv=[AODVDesv,DSRDesv,DYMODesv,OLSRDesv]
	i=0
	print TODO
	print TODO[2]
	label=["AODV","DSR","DYMO","OLSR"]
	marker=['*','p','o','D']
	fig = plt.figure(figsize=(20, 10)) 
	subplot1 = fig.add_subplot(1, 1, 1)
	while i<4:
		subplot1.errorbar(XXX,TODO[i],yerr=TODODesv[i], label=label[i], marker = marker[i])
		i+=1
	subplot1.legend(loc='upper left', ncol = 1)
	subplot1.set_xlim((0, 160))
	plt.title('Impact on Protocols over Free-Space Pathloss')
	plt.ylabel('E2ED in seconds')
	plt.xlabel('Quantity of Nodes')
	plt.show()
"""
main()
