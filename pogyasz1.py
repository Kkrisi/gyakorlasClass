# fajl beolvasas
from Csomag import Csomag


def fajlBeolvasas():
	fajl = open("csomag.txt","r",encoding="UTF-8")
	fajl.readline()
	sorokLista = fajl.readlines()
	fajl.close()

	csomagLista = []
	for i in range(0,len(sorokLista),1):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split('#')
		a = int(sorLista[0])
		b = int(sorLista[1])
		c = int(sorLista[2])
		m = int(sorLista[3])
		csomag=Csomag(a,b,c,m)
		csomagLista.append(csomag)

	return csomagLista


def pogyasz_atlagsuly(lista):
	ossz = 0
	db = 0
	for i in range(0,len(lista),1):
		if lista[i].a == 51:
			ossz += lista[i].m
			db += 1
	return ossz/db *1000




def Legmagasabb(lista):
	legmag = 0
	adatok = 0
	for i in range(0,len(lista),1):
		if lista[i].b > legmag:
			legmag = lista[i].b
			adatok = lista[i].a, lista[i].b, lista[i].c, lista[i].m
	return adatok


































