
import pogyasz1


print("III/A,B:")
csomagLista = pogyasz1.fajlBeolvasas()
print(f"\tA pogyászok száma: {len(csomagLista)}")


print("III/C:")
atlag = pogyasz1.pogyasz_atlagsuly(csomagLista)
print(f"\tAz 51 cm-es pogyászok átlag súlyértéke: {round(atlag)} g")


print("III/D:")
legMag = pogyasz1.Legmagasabb(csomagLista)
print(f"A legmagasabb pogyász méretei: {legMag[0]}x{legMag[1]}x{legMag[2]}, súlya: {legMag[3]} kg")
									# 47x46x16, súlya: 4 kg








