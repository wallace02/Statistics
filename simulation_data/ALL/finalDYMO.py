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

	#print "Path Loss: AODV, DSR,DYMO,OLSR"
	#opcao = raw_input("Ingrese opcion: ")
	opcao = "DYMO"
	ByProt = FiltroByPathLoss(FilesList, opcao)
	#print "ByPathLoss", type(ByPathLoss)
	#print ByPathLoss.items(), "\n"
	#print len(ByPathLoss)


def ListOfFiles():
	FilesList = []									  
	for file_ in os.listdir("/home/william/Simulators/Statistics/simulation_data/ALL"):
		if file_.endswith(".csv"):
			FilesList.append(file_)  	
			#print(file_) #MUESTRA TODOS LOS FILES EN LA CARPETA
			#print FilesList   #MUESTRA TODOS LOS FILES GUARDADOS EN LA LISTA 
	return FilesList

def FiltroByPathLoss(FilesList, opcao):
	Filtro = ['AODVRouting-','DSRUU-','DYMOUM-','OLSR-']
	for i in Filtro:
		if opcao in i:
			opcao = i
			break	

	FS25E2ED, FS25RATE, FS50E2ED, FS50RATE, FS75E2ED, FS75RATE, FS100E2ED, FS100RATE  = [defaultdict(list) for dummy in range(8)]
	LNS25E2ED, LNS25RATE, LNS50E2ED, LNS50RATE, LNS75E2ED, LNS75RATE, LNS100E2ED, LNS100RATE  = [defaultdict(list) for dummy in range(8)]
	NAK25E2ED, NAK25RATE, NAK50E2ED, NAK50RATE, NAK75E2ED, NAK75RATE, NAK100E2ED, NAK100RATE  = [defaultdict(list) for dummy in range(8)]
	TRG25E2ED, TRG25RATE, TRG50E2ED, TRG50RATE, TRG75E2ED, TRG75RATE, TRG100E2ED, TRG100RATE  = [defaultdict(list) for dummy in range(8)]
	
	Recived='rcvdPk'
	Sent='sentPk'
	E2ED='E2ED'
	for f in FilesList:
		csvfile = csv.DictReader(open(f, 'r'))   ## ABRE EL ARCHIVO A LEER EN FORMATO DICTReader
		for row in csvfile:
			for k, v in row.iteritems():
				if opcao in k:
					if '-FS-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								FS25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								FS25RATE[Recived].append(v)
							if 'sentPk' in k:
								FS25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								FS50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								FS50RATE[Recived].append(v)
							if 'sentPk' in k:
								FS50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								FS75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								FS75RATE[Recived].append(v)
							if 'sentPk' in k:
								FS75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								FS100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								FS100RATE[Recived].append(v)
							if 'sentPk' in k:
								FS100RATE[Sent].append(v)
					elif '-LNS-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								LNS25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								LNS25RATE[Recived].append(v)
							if 'sentPk' in k:
								LNS25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								LNS50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								LNS50RATE[Recived].append(v)
							if 'sentPk' in k:
								LNS50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								LNS75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								LNS75RATE[Recived].append(v)
							if 'sentPk' in k:
								LNS75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								LNS100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								LNS100RATE[Recived].append(v)
							if 'sentPk' in k:
								LNS100RATE[Sent].append(v)
					elif '-TRG-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								TRG25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								TRG25RATE[Recived].append(v)
							if 'sentPk' in k:
								TRG25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								TRG50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								TRG50RATE[Recived].append(v)
							if 'sentPk' in k:
								TRG50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								TRG75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								TRG75RATE[Recived].append(v)
							if 'sentPk' in k:
								TRG75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								TRG100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								TRG100RATE[Recived].append(v)
							if 'sentPk' in k:
								TRG100RATE[Sent].append(v)
	"""
					elif '-NAK-' in k:
						if '-25n-' in k:
							if 'endToEndDelay' in k:
								NAK25E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								NAK25RATE[Recived].append(v)
							if 'sentPk' in k:
								NAK25RATE[Sent].append(v)
						if '-50n-' in k:
							if 'endToEndDelay' in k:
								NAK50E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								NAK50RATE[Recived].append(v)
							if 'sentPk' in k:
								NAK50RATE[Sent].append(v)
						if '-75n-' in k:
							if 'endToEndDelay' in k:
								NAK75E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								NAK75RATE[Recived].append(v)
							if 'sentPk' in k:
								NAK75RATE[Sent].append(v)
						if '-100n-' in k:
							if 'endToEndDelay' in k:
								NAK100E2ED[E2ED].append(v)
							if 'rcvdPk' in k:
								NAK100RATE[Recived].append(v)
							if 'sentPk' in k:
								NAK100RATE[Sent].append(v)
	"""
	FS = [FS25E2ED, FS25RATE, FS50E2ED, FS50RATE, FS75E2ED, FS75RATE, FS100E2ED, FS100RATE]
	LNS = [LNS25E2ED, LNS25RATE, LNS50E2ED, LNS50RATE, LNS75E2ED, LNS75RATE, LNS100E2ED, LNS100RATE]
	TRG = [TRG25E2ED, TRG25RATE, TRG50E2ED, TRG50RATE, TRG75E2ED, TRG75RATE, TRG100E2ED, TRG100RATE]
	#NAK = [DYMO25E2ED, DYMO25RATE, DYMO50E2ED, DYMO50RATE, DYMO75E2ED, DYMO75RATE, DYMO100E2ED, DYMO100RATE]
	Protocolos = [FS,LNS] #[FS,LNS,NAK,TRG]

	FSMean, FSDesv, FSPDR, NAKMean, NAKDesv, NAKPDR, TRGMean, TRGDesv, TRGPDR, LNSMean, LNSDesv, LNSPDR  = [[0]*4 for dummy in range(12)]

	Statistics(FS, FSMean, FSDesv, FSPDR)
	#print AODVMean
	#print AODVDesv
	Statistics(LNS, LNSMean, LNSDesv, LNSPDR)
	#print DSRMean
	#print DSRDesv
	Statistics(TRG, TRGMean, TRGDesv, TRGPDR)
	#print DYMOMean
	#print DYMODesv
	##################Statistics(NAK, NAKMean, NAKDesv, NAKPDR)
	#print OLSRMean
	#print OLSRDesv
	
	XAxis = [25, 50, 75, 100]
	TODO=[FSMean,LNSMean,TRGMean] #,NAKMean]
	TODODesv=[FSDesv,LNSDesv,TRGDesv] #,NAKDesv]
	TODOPDR=[FSPDR,LNSPDR,TRGPDR] #,NAKPDR]
	
	label=["FS","LNS","TRG"] #,"NAK"]
	marker=['*','p','o'] #,'D']
	
	fig = plt.figure(figsize=(20, 10)) 
	subplot1 = fig.add_subplot(1, 1, 1)
	i=0
	while i<3: #4:
		subplot1.errorbar(XAxis,TODO[i],yerr=TODODesv[i], label=label[i], marker = marker[i])
		i+=1
	
	subplot1.legend(loc='upper left', ncol = 1, prop={'size':20})
	subplot1.set_xlim((0, 125))
	subplot1.set_ylim((0, 5))
	plt.title('Impact of DYMO over Pathloss', fontsize=20)
	plt.ylabel('E2ED in seconds', fontsize=20)
	plt.xlabel('Quantity of Nodes', fontsize=20)
	
	# major ticks every 25, minor ticks every 5 en el eje X                                   
	major_ticksx = np.arange(0, 126, 25)
	minor_ticksx = np.arange(0, 126, 5)
	# major ticks every 1, minor ticks every 0.25 en el eje Y
	major_ticksy = np.arange(0, 5.1, 1)
	minor_ticksy = np.arange(0, 5, 0.25)
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
	plt.savefig('DYMO-E2ED.png', format='png')
	#plt.show()

	


	figProt = plt.figure(figsize=(20, 10)) 
	subplot2 = figProt.add_subplot(1, 1, 1)
	i=0
	while i<3: #4:
		subplot2.errorbar(XAxis,TODOPDR[i], label=label[i], marker = marker[i])
		i+=1
	
	subplot2.legend(loc='upper left', ncol = 1, prop={'size':20})
	subplot2.set_xlim((0, 125))
	subplot2.set_ylim((0, 0.5))
	plt.title('Impact of DYMO over Pathloss', fontsize=20)
	plt.ylabel('Packet Delivery Rate', fontsize=20)
	plt.xlabel('Quantity of Nodes', fontsize=20)
	
	# major ticks every 25, minor ticks every 5 en el eje X                                   
	major_ticksx = np.arange(0, 126, 25)
	minor_ticksx = np.arange(0, 126, 5)
	# major ticks every 1, minor ticks every 0.25 en el eje Y
	major_ticksy = np.arange(0, 0.5001, 0.1)
	minor_ticksy = np.arange(0, 0.5001, 0.025)
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
	plt.savefig('DYMO-PDR.png', format='png')
	#plt.show()

	return

def Statistics(Prot,ProtMeans,ProtDesvs,ProtPDR):
	sumS, sumR = [[0]*4 for dummy in range(2)]
	m=0
	for i in Prot:
		if m == 0:
			M = np.array(i.values()).astype(np.float64)
			mean = M.mean()
			desvest = np.std(M, ddof=1) / 2
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
			desvest = np.std(M, ddof=1) / 2
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
			desvest = np.std(M, ddof=1) / 2
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
			desvest = np.std(M, ddof=1) / 2
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
			ProtPDR[3]=sumR[3]/sumS[3]
			m+=1
	#print ProtMeans
	#print ProtDesvs
	#print PDR
	return

main()
