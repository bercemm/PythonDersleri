website="http://www.sadikturan.com"
kursadi="Python Dersleri: Sifirdan İleri Seviye Python Programlama."

#'kursadi' karakter dizisinde kaç karakter bulunmaktadır?
#iki şekilde yapılabilir
print(len(kursadi)) #1. çözüm
sonuc=len(website) #2.çözüm
print(sonuc)
#'website' içinden www karakterlerini alın.
print(website[7:10])
#'website' içinden com karakterlerini alın.
print(website[-3:])
#'kursadi' içinden ilk 15 ve son 15 karakterleri alın.
print(website[:16])
print(website[-15:])
#'kursadi' ifadesindeki karakterleri tersten yazdırın.
print(kursadi[::-1])
#'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s='Hello world'
s=s[0:6] + 'W' + s[-4:]
print(s)

#'abc' ifadesini yanyana 3 defa yazdırın.

print('abc'*3)


name,surname,age,job='Bercem','Ucar',22,'ogrenci'
#yukarıda verilen değişkenler ile ekrana aşağıdakini yazdırın
#'Benim adım Bercem Ucar , Yaşım 32 ve mesleğim öğrenci.'
print(f"Benim adim {name} {surname} , Yasim {age} ve meslegim {job}")
#2. çözüm
sonuc=f"Benim adim {name} {surname} , Yasim {age} ve meslegim {job}"
print(sonuc)



#String methodları
msg="Benim Adim Bercem Ucar"
print(msg.upper()) # upper bütün harfleri büyütür. cıktı : BENIM ADIM BERCEM UCAR   
print(msg.lower()) # lower bütün harfleri kücültür. cıktı : benim adim bercem ucar
print(msg.title()) # title her kelimenin ilk harfini büyük yapar. cıktı : Benim Adim Bercem Ucar
print(msg.capitalize()) # capitalize sadece ilk karakteri büyük harfe çevirir. cıktı : Benim adim bercem ucar
print(msg.index('Bercem')) #Bercem kelimesinin kacıncı indeksten basladıgını gösterir. Cıktı : 11


print(msg.islower()) # cıktı : False  --> cünkü is kullanınca soru soruyoruz ve burda da msg bütün harfleri kücük olmadıgı icin false.
print(msg.istitle()) # cıktı : True --> her kelimenin ilk harfi büyük oldugu icin True geldi


print("  abc  ".strip()) #strip ifadesi bastaki ve sondaki bosluklari kapatir ve bosluksuz cikti verir

print(msg.split()) # burda split ayırma anlamındadır bosluklardan ayır anlamına gelir. 
#cıktısı : ['Benim', 'Adim', 'Bercem', 'Ucar']

sonuc1=msg.split()
print(sonuc1[0]) #cıktı : Benim
sonuc2="-".join(sonuc1)
print(sonuc2) #cıktı : Benim-Adim-Bercem-Ucar -->aralarına tire koyarak kelimeleri birleştirdi.
sonuc1=msg.replace('Bercem','Buse')
print(sonuc1) #cıktı : Benim Adim Buse Ucar   Bercem yerine Buse yazdı.
sonuc1=msg.replace(' ', '-').replace('Ucar', 'Keskin').replace('c', 'ç') # (boşluk yerine -) (Ucar yerine Keskin) (c yerine ç yazdik)
print(sonuc1) #cıktı : Benim-Adim-Berçem-Keskin

msg1="Benim Adim . Bercem Ucar."
print(msg1.split('.')) #noktalardan ayırır. cıktı : ['Benim Adim ', ' Bercem Ucar', '']


#string metotları uygulama 
website1="http://www.sadikturan.com"
kursadi1="Python Dersleri: Sifirdan İleri Seviye Python Programlama."
#' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
s1=' Hello World '.strip()
print(s1)
#s1=' Hello World '.lstrip() lstrip() soldaki boşlukları(karakterleri) siler
#s1=' Hello World '.rstrip() rstlip() sağdaki boşlukları siler
s3=website1.lstrip('pth') #soldan pth karakterlerini siler
print(s3)

#'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
s2= 'www.sadikturan.com'.replace('www.','').replace('.com','')
print(s2)
s2= 'www.sadikturan.com'.strip('w.moc')
print(s2)
#'kursadi1' karakter dizisinin tüm karakterlerini kücük harf yapin.
print(kursadi1.lower())
#'website1' içinde kaç tane a karakteri vardır? (count('a'))
print(website1.count('a'))
#aralık içinde aratmak için = count('a',3,10) 3 ile 10 arasında a var mı? bakılabilir.
#'website1' 'www' ile baslayip com ile bitiryor mu?
print(website1.startswith('www')) #cıktı : False 
print(website1.endswith('com')) #cıktı : True
#'website1' icinde '.com' ifadesi var mı?
print(website1.find('.com')) #-1 gelirse yoktur anlamına gelir
#'kursadi1' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(kursadi1.isalpha())
#'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
c='contents'.center(50,'*') #rjust sağına yıldız , ljust soluna yapılabilir
#'kursadi1' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
print(kursadi1.replace('','-'))
#'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
h='Hello World'.replace('World', 'There')
#'kursadi1' karakter dizisini boşluk karakterlerinden ayirin.
print(kursadi1.split())