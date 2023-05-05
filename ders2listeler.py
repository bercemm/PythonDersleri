msg='Bugün hava cok güzel'.split()
print(msg[0]) #cıktı : Bugün --> cünkü split ile ayırdık ['Bugün','hava'.. seklinde]
print(msg[0][1]) #cıktı : u --> 0. index'in (Bugün) 1. index'ini alır = u
msg='Bugün hava cok güzel'
print(msg[0]) #cıktı : B --> split ile ayirmadigimiz icin ilk karakteri alır 0. index

#Liste
sayilar=[1,4,3,9,10]
print(sayilar[2]) #cıktı : 3
# print(sayilar[5]) hata alır cünkü 5. index listede yok.

isimler=['ali','ahmet','buse']
print(isimler) #cıktı : ['ali', 'ahmet', 'buse']
print(isimler[1]) #cıktı : ahmet

listebuse=['buse',22]
print(listebuse[1]) #cıktı : 22

ogrenciler=[['ali',20],['ahmet',22],listebuse]
print(ogrenciler[0]) #cıktı : ['ali', 20]
print(ogrenciler[0][1]) #cıktı : 20
print(ogrenciler[1][0]) #cıktı : ahmet
print(ogrenciler[2][0]) #cıktı : buse  --> ayrı olarak olusturdugumuz listeyi yeni olusturdugumuz ogrenciler listesine de ekleyebiliriz.

diller=['Python', 'C#','Java','Javascript']
print(type(diller)) #cıktı : <class 'list'>
print(diller[0]) #cıktı : Python
print(diller[0:2]) #cıktı : ['Python', 'C#'] --> 0. indexten 2. index'e kadar 2 dahil değil
print(diller[:3]) #cıktı : ['Python', 'C#', 'Java', 'Javascript'] --> bastan sonuncu index'e kadar
print(diller[2:]) #cıktı : ['Java', 'Javascript'] --> 2. index'ten sonuncusuna kadar
print(diller[-1]) #cıktı : Javascript --> -1. index= en sondaki 
print(diller[-4:-1]) #cıktı : ['Python', 'C#', 'Java']

diller[0]='Html'
print(diller) #cıktı : ['Html', 'C#', 'Java', 'Javascript'] --> 0. index'i Html ile değiştirdik.
print(len(diller)) #cıktı : 4 --> liste uzunlugu
diller=diller+['Angular','React']
print(diller) #cıktı : ['Html', 'C#', 'Java', 'Javascript', 'Angular', 'React']  --> diller listesine 2 eleman daha ekledik.


#if koşul ifadesi deneme
if "Html" in diller:
    print("evet") #cıktı evet --> cünkü diller listesinde Html elemanı var

#döngüler
for x in diller: #listedeki her elemanı x içine alır ve print ile her birini alt alta teker teker yazar
    print(x)
    
del diller[0]
print(diller) #diller listesinden 0. index yani 1. elemanı siler
#cıktı : ['C#', 'Java', 'Javascript', 'Angular', 'React']


#Listeler UYGULAMA

#1-"Samsung S5, Samsung S6, Samsung S7, Samsung S8" elemanlarına sahip lise olustur
telefonlar=['Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8']
#2-liste kac elemanlıdır?
print(len(telefonlar)) #cıktı : 4
#3-listenin ilk ve son elemanı nedir?
print(telefonlar[0])
print(telefonlar[-1])
#4-"Samsung S5" degerini "Samsung S9 " ile degistirin
telefonlar[0]='Samsung S9'
print(telefonlar)
#5-"Samsung S6" listenin bir elemanı mıdır?
if 'Samsung S6' in telefonlar:
    print("Samsung S6 listenin elemanidir")
#6-Listenin -3 indeksindeki deger nedir?
print(telefonlar[-3])
#7-Listenin ilk 2 elemanını alın.
print(telefonlar[:2])
#8-Listenin son 2 elamanı yerine "Samsung S9" ve "Samsung S10" degerleri ekleyin.
telefonlar[-2:]=['Samsung S9','Samsung S10']
print(telefonlar) #cıktı : ['Samsung S9', 'Samsung S6', 'Samsung S9', 'Samsung S10']
#9-Listenin üzerine "IPhone X" ve "IPhone XR" degerlerini ekleyin
telefonlar=telefonlar+['IPhone X','IPhone XR']
print(telefonlar) #cıktı : ['Samsung S9', 'Samsung S6', 'Samsung S9', 'Samsung S10', 'IPhone X', 'IPhone XR']
#10-Listenin son elemanini silin
del telefonlar[-1]
print(telefonlar) #cıktı : ['Samsung S9', 'Samsung S6', 'Samsung S9', 'Samsung S10', 'IPhone X']
#11-Liste elemanlarını tersten yazdirin.
print(telefonlar[::-1]) #cıktı : ['IPhone X', 'Samsung S10', 'Samsung S9', 'Samsung S6', 'Samsung S9']
#12-liste elemanlarini ekrana yazdirin
for tel in telefonlar:
    print(tel)
########################################################################################
ogrenciA=["Yigit","Bilgi",2000,[70,90,30]]
ogrenciB=["Sena","Turan",1999,[60,70,40]]
ogrenciC=["Ahmet","Deniz",1998,[80,60,10]]

ogrencilist=[ogrenciA,ogrenciB,ogrenciC]
 
for ogrenci in ogrencilist:
    ad=ogrenci[0]
    soyad=ogrenci[1]
    yas=2023-ogrenci[2]
    notort=(ogrenci[3][0] +ogrenci[3][1]+ogrenci[3][2])/3
    print(f"{ad} {soyad} {yas} {notort}")
    '''
    Cikti:
    Yigit Bilgi 23 63.333333333333336
    Sena Turan 24 56.666666666666664
    Ahmet Deniz 25 50.0
    '''



