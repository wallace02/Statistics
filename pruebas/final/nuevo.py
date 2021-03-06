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
	"""
	M = np.array(ByPathLoss.values()).astype(np.float64)
	print M
	mean = M.mean()
	desvest = np.std(M, ddof=1)
	print mean, desvest, "\n"
	"""

	ByNodes = FiltroByNodes(ByPathLoss)
	#print "ByNodes", type(ByNodes)
	#print ByNodes, "\n"
	#print ByNodes['20'].values()
	#print len(ByNodes)
	"""
	M = np.array(ByNodes['50'].values()).astype(np.float64)
	print M
	mean = M.mean()
	desvest = np.std(M, ddof=1)
	print mean, desvest, "\n"

	"""
	ByProtocolos = FiltroByProtocolos(ByNodes)
	#print "ByProtocolos", type(ByProtocolos)
	#print ByProtocolos, "\n"
	"""
	print ByProtocolos['20']['AODV'].values()
	M = np.array(ByProtocolos['20']['AODV'].values()).astype(np.float64)
	print len(ByProtocolos)
	print M
	mean = M.mean()
	desvest = np.std(M, ddof=1)
	print mean, desvest
	"""
	Statistics(ByProtocolos)

def ListOfFiles():
	FilesList = []									  
	for file_ in os.listdir("/home/william/Simulators/statistics/nuevo/"):
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

	FSPL = defaultdict(list)
	LNSPL = defaultdict(list)
	NAKPL = defaultdict(list)
	TRGPL = defaultdict(list)
	ByPathLoss = defaultdict(list)
	for f in FilesList:
		csvfile = csv.DictReader(open(f, 'r'))   ## ABRE EL ARCHIVO A LEER EN FORMATO DICTReader
		for row in csvfile:									
			for k, v in row.iteritems():
				#print k, v
				if opcao in k and (opcao == '-FS-'):
					FSPL[k].append(v)
				if opcao in k and (opcao == '-LNS-'):
					LNSPL[k].append(v)
				if opcao in k and (opcao == '-NAK-'):
					NAKPL[k].append(v)
				if opcao in k and (opcao == '-TRG-'):
					TRGPL[k].append(v)
	if opcao == '-FS-':
		ByPathLoss = copy.deepcopy(FSPL)
	if opcao == '-LNS-':
		ByPathLoss = LNSPL
	if opcao == '-NAK-':
		ByPathLoss = NAKPL
	if opcao == '-TRG-':
		ByPathLoss = TRGPL
	return ByPathLoss

def FiltroByNodes(ByPathLoss):
	Filtro = ['-20-','-50-','-100-','-150-']
	C20Nodes = defaultdict(list)
	C50Nodes = defaultdict(list)
	C100Nodes = defaultdict(list)
	C150Nodes = defaultdict(list)
	CNodes = defaultdict(list)
	CNodes2 = defaultdict(list)
	for k, v in ByPathLoss.iteritems():
		for i in Filtro:
			if i in k and (i == '-20-'):
				C20Nodes[k].append(v)
			if i in k and (i == '-50-'):
				C50Nodes[k].append(v)
			if i in k and (i == '-100-'):
				C100Nodes[k].append(v)
			if i in k and (i == '-150-'):
				C150Nodes[k].append(v)
	CNodes2['20'].append(C20Nodes)
	CNodes2['50'].append(C50Nodes)
	CNodes2['100'].append(C100Nodes)
	CNodes2['150'].append(C150Nodes)
	#print C20Nodes.items(), "\n"
	#print C50Nodes.items(), "\n"
	#print C100Nodes.items(), "\n"
	#print C150Nodes.items(), "\n"
	CNodes = {'20':C20Nodes, '50':C50Nodes, '100':C100Nodes, '150':C150Nodes}
	#print CNodes2, "\n"
	return CNodes #C20Nodes, C50Nodes, C100Nodes, C150Nodes

def FiltroByProtocolos(ByNodes):
	Filtro = ['AODVRouting-','DSRUU-','DYMOUM-','OLSR-']
	AODV = defaultdict(list)
	DYMO = defaultdict(list)
	OLSR = defaultdict(list)
	DSR = defaultdict(list)
	Protocolos = {}#defaultdict(list)
	Protocolos2 = defaultdict(list)
	#AUX2 = dict(list)
	#AUXX2 = dict(list)
	for k, v in ByNodes.iteritems():	
		for kk, vv in v.iteritems():
			for i in Filtro:
				if i in kk and (i == 'AODVRouting-'):
					AODV[kk].append(vv)
				if i in kk and (i == 'DYMOUM-'):
					DYMO[kk].append(vv)
				if i in kk and (i == 'OLSR-'):
					OLSR[kk].append(vv)
				if i in kk and (i == 'DSRUU-'):
					DSR[kk].append(vv)

		AUX={k:{'AODV':AODV, 'DYMO':DYMO, 'OLSR':OLSR, 'DSR':DSR}}
		#print AUX, type(AUX)
		AUX2 = copy.deepcopy(AUX)
		#print type(AUX2)
		#AUXX = {'AODV':AODV, 'DYMO':DYMO, 'OLSR':OLSR, 'DSR':DSR}
		#AUXX2 = copy.deepcopy(AUXX)
		#Protocolos2[key].append(AUXX2)
		Protocolos.update(AUX2)
		AODV.clear()
		DYMO.clear()
		OLSR.clear()
		DSR.clear()
	#print Protocolos2, "\n"
	#print Protocolos, "\n"
	return Protocolos

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
	XXX = [20, 50, 100, 150]
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
			"""
			if '20' in k:
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

			if '100' in k:
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

			if '150' in k:
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
			"""		
			if 'AODV' in kk and '20' in k:
				AODVMean[0]=mean
				AODVDesv[0]=desvest
			if 'AODV' in kk and '50' in k:
				AODVMean[1]=mean
				AODVDesv[1]=desvest
			if 'AODV' in kk and '100' in k:
				AODVMean[2]=mean
				AODVDesv[2]=desvest
			if 'AODV' in kk and '150' in k:
				AODVMean[3]=mean
				AODVDesv[3]=desvest
			
			if 'DYMO' in kk and '20' in k:
				DYMOMean[0]=mean
				DYMODesv[0]=desvest
			if 'DYMO' in kk and '50' in k:
				DYMOMean[1]=mean
				DYMODesv[1]=desvest
			if 'DYMO' in kk and '100' in k:
				DYMOMean[2]=mean
				DYMODesv[2]=desvest
			if 'DYMO' in kk and '150' in k:
				DYMOMean[3]=mean
				DYMODesv[3]=desvest

			if 'OLSR' in kk and '20' in k:
				OLSRMean[0]=mean
				OLSRDesv[0]=desvest
			if 'OLSR' in kk and '50' in k:
				OLSRMean[1]=mean
				OLSRDesv[1]=desvest
			if 'OLSR' in kk and '100' in k:
				OLSRMean[2]=mean
				OLSRDesv[2]=desvest
			if 'OLSR' in kk and '150' in k:
				OLSRMean[3]=mean
				OLSRDesv[3]=desvest

			if 'DSR' in kk and '20' in k:
				DSRMean[0]=mean
				DSRDesv[0]=desvest
			if 'DSR' in kk and '50' in k:
				DSRMean[1]=mean
				DSRDesv[1]=desvest
			if 'DSR' in kk and '100' in k:
				DSRMean[2]=mean
				DSRDesv[2]=desvest
			if 'DSR' in kk and '150' in k:
				DSRMean[3]=mean
				DSRDesv[3]=desvest
			
			E2ED.clear()
			Rate.clear()
	print "AODV", AODVMean, AODVDesv
	print "DSR", DSRMean, DSRDesv
	print "DYMO", DYMOMean, DYMODesv
	print "OLSR", OLSRMean, OLSRDesv

main()
