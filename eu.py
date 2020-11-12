#Ausztria;1995.01.01
import colliction
with open('csatlakozás.txt', encoding="utf-8") as f:
  lista=[]
  for sor in f:
    lista.append(sor.strip().split(";"))
#3.feladat
print(f"tag álamok száma {len(lista)}")

#4.feladat
sz=0
for orszag,datum in lista: 
  if int(datum[0:4])==2007:
    sz=sz+1
print(sz)

#5.feladat
for orszag,datum in lista:
  if orszag=="Magyarország":
    print(f"magyarország {datum} csatlakozot az europaiuniohoz.")

#6.feladat
sz=0
for orszag,datum in lista:
  if datum[5:7]=="05":
    sz=sz+1
if sz>0:
  print("csatlakoztak májusban az eu-hoz")
else:
  print("nem csatlakoztak májusban az eu-hoz")

utolsódatum=""
for orszag,datum in lista:
  if utolsódatum<datum:
    utolso_datum=datum
    utolso_orszag=orszag 
print(utolso_orszag)

cnt = colliction.counter()
for orszag,datum in cnt.items():
  cnt[datum[0:4]] +=1
print("8.felaladat statisztika")
for év,darab in cnt.items():
  print(f"    {év} - {darab}, ország")


    




