meniu = ['papanasi']*10 + ['ceafa']*3 + ['guias']*6
preturi = [['papanasi', 7], ['ceafa', 10], ['guias', 5]]
studenti = ['Liviu', 'Ion', 'George', 'Ana', 'Florica'] #queue
comenzi = ['guias', 'ceafa', 'ceafa', 'papanasi', 'ceafa'] #queue
tavi = ['tava']*7  #stack
istoric_comenzi = []

portii = {}

while len(studenti) > 0:
    meniu.remove(comenzi[0])
    if comenzi[0] in portii.keys():
        portii[comenzi[0]] += 1
    else:
        portii[comenzi[0]] = 1
    comanda = f"{studenti.pop(0)} a comandat {comenzi.pop(0)}."
    istoric_comenzi.append(comanda)
    print(comanda)
    tavi.pop()
print()

istoric_portii = 'Nu s-a comandat nimic.'
for key in portii.keys():
    if 'nimic' in istoric_portii:
        istoric_portii = 'S-a comandat'
    istoric_portii += f' {portii[key]} {key},'
istoric_portii = istoric_portii[:len(istoric_portii)-1] + '.'
print(istoric_portii+'\n')

print(f"Mai sunt {len(tavi)} tavi.")

for item in preturi:
    print(f"Mai este {item[0]}: {item[0] in meniu}.")

total = 0
for item in preturi:
    if item[0] in portii.keys():
        total += portii[item[0]]*item[1]
print(f"\nCantina a incasat: {total} lei.")

thingy = []
for pret in preturi:
    if pret[1] <= 7:
        thingy.append(pret)
print(f"Produse care costa cel mult 7 lei:�{thingy}")