sayilar=[1,5,8,3,4]
harfler=['a','u','p','y','b']

print(min(sayilar)) #cıktı : 1
print(max(sayilar)) #cıktı : 8
print(min(harfler)) #cıktı : a --> alfabetik siralama yapar
print(max(harfler)) #cıktı : y

#ekleme
sayilar.append(13) #sayilar listesine 13 elemanı eklendi. Append ile eleman ekliyoruz.
print(sayilar) #cıktı : [1, 5, 8, 3, 4, 13]
sayilar.insert(3,20) #3. index'e 20 elemanını ekler. İnsert ile index ve eleman veriyoruz
print(sayilar) #cıktı : [1, 5, 8, 20, 3, 4, 13]
sayilar.insert(-1,50) #orijinal listenin sonuna 50 ekler
print(sayilar) #cıktı : [1, 5, 8, 20, 3, 4, 50, 13]

#silme
sayilar.pop() #en sondaki elemani siler.Burda 13 elemanını
sayilar.pop()# burda da 50 elamanini siler . Bu sekildeyken Her zaman en sondan silmeye baslar.
print(sayilar) #cıktı : [1, 5, 8, 20, 3, 4]
sayilar.pop(0) #0. indexteki elemani siler. cıktı : [1, 5, 8, 20, 3, 4]
sayilar.remove(20) #listedeki 20 elemanini siler
print(sayilar) #cıktı : [5, 8, 3, 4]

harfler.remove('y') #harfler listesinden y elemanini siler
print(harfler) #cıktı : ['a', 'u', 'p', 'b']

#sıralama
sayilar.sort() #cıktı : [3, 4, 5, 8]  sayıları kücükten büyüge sıralar
harfler.sort() #cıktı : ['a', 'b', 'p', 'u'] alfabetik sıralar
sayilar.reverse() #cıktı : [8, 5, 4, 3]  kücükten büyüge sıralanmıs sayıları ters cevirir.

print(sayilar.count(5)) #5'ten kac tane oldugunu bulmak icin bulundugu index numarasını verir
print(harfler.count('a')) #a harfinden kac tane oldugunu bulmak icin 
print(sayilar.index(8)) #index count gibi burda da 8'in hangi indexte oldugunu verir

sayilar.clear() #clear bi liste elemanlarının bütün elemanlarını siler. 
print(sayilar) #cıktı : []

#LİSTE METOTLARI UYGULAMA
isimler=['Ada','Yiğit','Hasan','Beril']
yaslar=[1998,2000,1999,1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz"
print(isimler.append("Cenk"))
#2- "Sena" degerini listenin basına ekleyiniz
print(isimler.insert(0,"Sena"))
#3- "Yiğit degerini listeden siliniz"
isimler.remove('yiğit')
print(isimler)
#4-"Yiğit" isminin index'i nedir?
index=isimler.index("Yiğit")
#6-Liste elemanlarini ters cevirin
print(isimler.reverse())
#8-Liste elemanlarını alfabetik sıralayınız.
isimler.sort()
yaslar.sort()
#9- yaslar listesini rakamsal büyüklüğüne göre sıralayınız
yaslar.sort()
