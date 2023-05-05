#Sayısal operatörler
print(type(3)) #<class 'int'>
print(type(4.0)) #<class 'float'>
print(2+2) #4
print(2+2.0) #4.0
print(3**2) #9      ** üs alma için kullanılır
print(10%3) #1      % mod almak için kullanılır 10un 3e bölümünden kalanı verdi
print(10/3)  #3.3333333333333335    / normal bölme işlemi yapar bu yüzden ondalıklı olabilir
print(10//3) #3 bölündüğünde sonuç virgüllü bi sayı olsa da tam kısmı verir //

#Değişken tanımlama
urunA=100
urunB=200
kdv=0.15
print("urunA fiyatı=" , urunA+(urunA*kdv)) #urunA fiyatı= 115.0
print("urunB fiyatı=" , urunB+(urunB*kdv)) #urunB fiyatı= 230.0

a,b,c=10,20,30
name="bercem"
surname='ucar'
isStudent=True
isStudent=False
print(type(isStudent))  #<class 'bool'>

x,y,name,isStudent=1,1.5,'bercem',True  #bu şekilde tanımlayabiliriz.

ogrenciAd='cem'
ogrenciSoyad='ucar'
ogrenciAdSoyad=ogrenciAd+' '+ogrenciSoyad
print(ogrenciAdSoyad) #cem ucar


urun1=50
urun2=60.5
toplam=urun1+urun2
print("toplam:",urun1+urun2) #toplam: 110.5

a='10'
b='20'
toplam=a+b
print(toplam) # çıktı : 1020


a1=int(input("a1 degeri:")) #input ile kullanıcıdan değer alıyoruz
a2=int(input("a2 degeri:"))
toplam=a1+a2
print(toplam)

#değişken dönüştürme

age=10
weight=40.4
name="seda"
isStudent=True

result=int(weight)
print(type(result)) #<class 'int'>

result=float(age)
print(type(result)) #<class 'float'>

result=str(isStudent)
print(type(result))  #<class 'str'>

result=bool(name)
print(type(result)) #<class 'bool'>

result=int(isStudent)
print(type(result)) #<class 'int'>
print(result) #1
print(isStudent) #True

#UYGULAMA
#daire alanı=pi.r.r  daire çevresi=2pi.r  yarıçapı verilen bir dairenin alanı ve cevresini hesaplayınız (3.14)
pi=3.14
yaricap=float(input("yaricapi giriniz:"))
dairealan=pi*(yaricap**2)
dairecevre=2*pi*yaricap
print("alan=",dairealan,"cevre",dairecevre)  #alan= 28.26 cevre 18.84
result="daire alanı=" +str(dairealan) + "  daire cevresi=" +str(dairecevre)
print(result) #daire alanı=28.26  daire cevresi=18.84


#string
ad='sadik'
soyad='turan'
yas='32'

msj="adim " + ad + " soyadim " +soyad + " yasim "+yas
print(msj) #adim sadik soyadim turan yasim 30
print(msj[0]) #a
print(msj[-2]) #3
print(msj[-1]) #2
print(len(msj)) #karakter sayısı,uzunlugunu öğrenebiliriz len ile #33

#String slicing (string parçalama)
print(msj[0:5]) #0. karakterden 5e kadar yazar 5 dahil değil #çıkıt:adim
print(msj[10:]) #10. karakterden başlayıp sonuncusuna kadar yazar  #Çıktı: soyadim turan yasim 32
print(msj[:8]) # baştan 8. karaktere kadar yazar 8 dahil değil   #Çıktı: adim sad
print(msj[2:19:3]) #2den 9a kadar 19 dahil değil 3 şer aralıklarla yazdırır  #çıkıt: isisam
print(msj[::-1]) #sondan başa doğru tersten yazar  #Çıktı: 23 misay narut midayos kidas mida
print(msj[-10:-1]) #Çıktı: n yasim 3    -10dan -1e kadar -1 dahil değil

#String formatlama 

isim='bercem'
soyisim='ucar'
yas=22

print("My name is {} {} I'am {} years old. ".format(isim,soyisim,yas)) #1. paranteze isim 2. paranteze soyisim 3. için yas yazar.
#cıktı : My name is bercem ucar I'am 22 years old.
print("My name is {0} {1}".format(isim,soyisim))
#cıktı : My name is bercem ucar
print('{2} {0} {1}'.format(isim,soyisim,yas))
#cıktı : 22 bercem ucar

print(f"My name is {isim} {soyisim} , and I'am {yas} years old. ")
#cıktı : My name is bercem ucar , and I'am 22 years old.