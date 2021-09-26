"""
 OOP ile ilgili QUIZ - 10 Soru
"""

# --------------------------------------------------------------------------------------#

# Soru 1:
"""
Adı Ogrenci olan bir class tanımlayın.
Ogrenci'nin 2 özelliği var:
* isim (str)
* numara (str)

Bu Ogrenci class'ından iki öğrenci yaratın.
Bilgileri şu şekilde olacak:
1- isim: James Bond, numara: 007
2- isim: Klark Kent, numara: 333

Sonra bu iki öğrencinin adlarını print edin.

İpuçları:
* __init__

Beklenen Sonuç:
James Bond
Klark Kent
"""


# Çözüm 1:
class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara


# Öğrenci nesneleri yarat
ogr_1 = Ogrenci('James Bond', '007')
ogr_2 = Ogrenci('Klark Kent', '333')

# print(ogr_1.isim)
# print(ogr_2.isim)

# --------------------------------------------------------------------------------------#

# Soru 2:
"""
Soru 1'deki Ogrenci class'ımızın şimdi de kayıt olduğu dersleri tutan,
bir attribute'u (özelliği) daha olsun. 
Bu özelliğin adı 'dersler' olsun ve list tipinde olsun.
Bu özellik, Ogrenci yaratılırken boş liste olarak initialize olacak.

Ogrenci derslere birer birer katılacak.
Dolayısı ile 'derse_katil()' adında bir metodu da olacak.
Be metod parametre olarak katılacak dersi alacak.
Eğer ders henüz listede yoksa, o zaman kayıt olacak.

Ek olarak 'get_dersler' adında bir metod daha olacak.
Bu metod bize öğrencinin kayıt olduğu ders listesini verecek.

Buna göre Ogrenci class'ını modifiye edin.

Öğrencinin bilgileri şu şekilde olacak:
isim: Cin Ali, numara: 1111
katılacağı dersler: Temel Python ve Yapay Zeka

Beklenen Sonuç:
ogrenci.get_dersler()  ->  ['Temel Python', 'Yapay Zeka']
"""


# Çözüm 2:
class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara
        # ders listesini -> []
        self.dersler = []

    def derse_katil(self, ders):
        # bu ders yoksa -> ekle
        if not ders in self.dersler:
            self.dersler.append(ders)

    def get_dersler(self):
        return self.dersler


ogrenci = Ogrenci('Cin Ali', '1111')

ogrenci.derse_katil('Temel Python')
ogrenci.derse_katil('Yapay Zeka')

# print(ogrenci.get_dersler())

# --------------------------------------------------------------------------------------#

# Soru 3:
"""
İsmi Point olan bir class tanımlayın. 
X-Y koordinat düzleminde bir noktayı temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir noktayı gösterir."

Point'in iki attribute'u vardır: 
    * x (int) 
    * y (int)

Point'in __init__() metodunu tanımlayın.
Ek olarak uzaklık hesaplayan bir metodu vardır. Adı 'uzaklik'.
'uzaklik' metodu parametre olarak ikinci bir Point alır.
Ve kendisi (self) ile ikinci nokta arasındaki mesafeyi hesaplayarak döner.

İpuçları:
* uzaklık şöyle hesaplanır:
    * x'ler arasındaki farkın karesi ile 
    * y'ler arasındaki farkın karesinin toplamının karekökü
    * d = math.sqrt(x_ler_farki**2 + y_ler_farki**2)
    
Örnek çağırma:
nokta_1 -> (1, 7)
nokta_2 -> (4, 3)
uzaklik = nokta_1.uzaklik(nokta_2)
print(uzaklik)

Beklenen Cevap: 5.0
"""

# Çözüm 3:
import math


class Point:
    """(x,y) koordinat düzlemindeki bir noktayı gösterir."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def uzaklik(self, diger):
        x_ler_farki = self.x - diger.x
        y_ler_farki = self.y - diger.y
        d = math.sqrt(x_ler_farki ** 2 + y_ler_farki ** 2)
        return d


nokta_1 = Point(1, 7)
nokta_2 = Point(4, 3)

# docstring'i yazdır
# print(nokta_1.__doc__)

uzaklik = nokta_1.uzaklik(nokta_2)
# print(uzaklik)

# --------------------------------------------------------------------------------------#

# Soru 4:
"""
İsmi Rectangle olan bir class tanımlayın. 
X-Y koordinat düzleminde bir dikdörtgeni temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir dikdörtgeni gösterir."

Rectangle'in 4 attribute'u vardır: 
    * kose_1 (Point)
    * kose_2 (Point)
    * kose_3 (Point)
    * kose_4 (Point)
Bu dört köşenin tipi Soru 3'de tanımladığınız Point class'ıdır.

Köşelerden 1 ve 2 aynı doğru üzerinde, 3 ve 4 aynı doğru üzerindedir.

1..............2
.              .
.              .
.              .
3..............4

Rectangle'in __init__() metodunu tanımlayın.
Ek olarak enini ve boyunu hesaplayan metodları vardır:
    * en = 1 - 2 arası mesafe  -> en_hesapla()
    * boy = 1 - 3 arası mesafe -> boy_hesapla()
Rectangle bu mesafeleri hesaplamak için Point class'ını kullanır.

Son olarak alan hesaplayan bir metodu vardır. Adı 'alan'.
'alan' metodu dikdörtgenin alanını hesaplayarak döner.

Örnek çağırma:
p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

en = rect.en
boy = rect.boy
alan = rect.alan()

Beklenen Sonuç:
en: 4.0
boy: 6.0
alan: 24.0
"""


# Çözüm 4:
class Rectangle:
    """(x,y) koordinat düzlemindeki bir dikdörtgeni gösterir."""

    def __init__(self, p_1, p_2, p_3, p_4):
        self.kose_1 = p_1
        self.kose_2 = p_2
        self.kose_3 = p_3
        self.kose_4 = p_4
        self.en_hesapla()
        self.boy_hesapla()

    def en_hesapla(self):
        self.en = self.kose_1.uzaklik(self.kose_2)

    def boy_hesapla(self):
        self.boy = self.kose_1.uzaklik(self.kose_3)

    def alan(self):
        return self.en * self.boy


p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

rect = Rectangle(p_1, p_2, p_3, p_4)

en = rect.en
boy = rect.boy
alan = rect.alan()

# print('en:', en)
# print('boy:', boy)
# print('alan:', alan)

# --------------------------------------------------------------------------------------#

# Soru 5:

"""
Adı BankaHesabi olan bir class tanımlayın.
BankaHesabi'nin bir attibute'u vardır: bakiye (int)
Ek olarak iki adet metodu vardır:
* para_cek(tutar)   -> hesaptan para çeker
* para_yatir(tutar) -> hesaba para yatırır

İki metod da bakiye'yi günceller ve ikisi de geriye, kalan bakiye'yi döner.
Hesap açılırken (__init__) bakiye değeri 0'dır.
Ek olarak her seferinde print() yazmamak için, class içerisinde 'bakiye_goruntule' diye
bir metod olsun.
Bu metod çağrılınca şöyle yazsın: Hesap bakiyesi: xxxxxx

Örnek Çağırma:
hesap = BankaHesabi()
hesap.bakiye_goruntule()
hesap.para_yatir(500)
hesap.bakiye_goruntule()
hesap.para_cek(200)
hesap.bakiye_goruntule()

Beklenen Sonuç:
Hesap bakiyesi: 0
Hesap bakiyesi: 500
Hesap bakiyesi: 300
"""


# Çözüm 5:
class BankaHesabi:
    def __init__(self):
        self.bakiye = 0

    def para_cek(self, tutar):
        self.bakiye -= tutar
        return self.bakiye

    def para_yatir(self, tutar):
        self.bakiye += tutar
        return self.bakiye

    def bakiye_goruntule(self):
        print('Hesap Bakiyesi: {}'.format(self.bakiye))


# hesap = BankaHesabi()
# hesap.bakiye_goruntule()
#
# hesap.para_yatir(500)
# hesap.bakiye_goruntule()
#
# hesap.para_cek(200)
# hesap.bakiye_goruntule()

# --------------------------------------------------------------------------------------#

# Soru 6:
"""
Adı MinimumBakiyeHesabi olan bir class tanımlayın.
Bu class, Soru 5'te tanımladığınız BankaHesabi class'ından kalıtım alacak.
Bu class içinde bakiye'nin bir minimum değeri tutulacak. (minimum_bakiye)
Bu değer hesap yaratılırken girilecek.

Eğer kullanıcı para çekmek isterse, 'para_cek(tutar)' metodu ile, 
o zaman minimum_bakiye'yi kontrol edeceğiz.
Eğer bu tutar çekilince, hesap bakiyesi minimum_bakiye'nin altına düşecek olursa,
para çekme işlemini iptal edip ekrana şöyle yazacak:
"Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında."

Ek olarak bu class'ı print eden biri anlamlı bir metin görsün diye,
"Bu MinimumBakiye sınıfıdır." şeklinde dönsün.

İpuçları:
* super()
* __str__
* para çekme işlemini bu class içinde yapmayın, ana class'ı yapıyor zaten

Örnek Çağırma:
minimum_hesap = MinimumBakiyeHesabi(100)
print(minimum_hesap)
minimum_hesap.para_yatir(500)
minimum_hesap.bakiye_goruntule()
minimum_hesap.para_cek(200)
minimum_hesap.bakiye_goruntule()
minimum_hesap.para_cek(300)
minimum_hesap.bakiye_goruntule()

Beklenen Sonuç:
Bu MinimumBakiye sınıfıdır.
Hesap bakiyesi: 500
Hesap bakiyesi: 300
Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında.
Hesap bakiyesi: 300
"""


# Çözüm 6:
class MinimumBakiyeHesabi(BankaHesabi):
    def __init__(self, minimum_bakiye):
        super().__init__()
        self.minimum_bakiye = minimum_bakiye

    # para_cek() metodunu override et
    def para_cek(self, tutar):
        if self.bakiye - tutar < self.minimum_bakiye:
            print("Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında.")
        else:
            BankaHesabi.para_cek(self, tutar)

    # __str__() -> overload
    def __str__(self):
        return "Bu Minimum Bakiye Sınıfıdır."


minimum_hesap = MinimumBakiyeHesabi(100)

# print(minimum_hesap)
#
# minimum_hesap.para_yatir(500)
# minimum_hesap.bakiye_goruntule()
#
# # para çekelim
# minimum_hesap.para_cek(200)
# minimum_hesap.bakiye_goruntule()
#
# # kalan tüm parayı çek -> 300
# minimum_hesap.para_cek(300)
# minimum_hesap.bakiye_goruntule()

# --------------------------------------------------------------------------------------#

# Soru 7:
"""
Aşağıdaki print() fonksiyonları ekrana ne yazar?

class K:
    def a(self):
        return self.b()

    def b(self):
        return 'K'

class L(K):
    def b(self):
        return 'L'

k = K()
l = L()
print(k.a(), l.a())
print(k.b(), l.b())
"""


# Çözüm 7:


class K:
    def a(self):
        return self.b()

    def b(self):
        return 'K'


class L(K):
    def b(self):
        return 'L'


k = K()
l = L()

# print(k.a(), l.a())
# print(k.b(), l.b())

"""
Cevap:
K L
K L

k.a() :
K -> a() -> b() -> 'K'

l.a():
L -> a() : K a() -> L b() -> 'L'

k.b():
K -> 'K'

l.b():
L -> 'L'
"""

# --------------------------------------------------------------------------------------#

# Soru 8:
"""
Aşağdaki şekilde iki class tanımlayın:

Sarki:
Şarkılarımızı tutmak için kullanacağız.
Her şarkının; 'adi', 'sanatci', 'album' ve 'sarki_no' diye özellikleri var.
'album' adlı özellik Album class'ı tipinde olacak.

Album:
Albümlerimizi tutacak.
Her albümün; 'adi', 'sanatci', 'yil' ve 'sarkilar' diye özellikleri var.
'sarkilar' bir liste olacak ve içinde Sarki nesnelerini tutacak.
Album'un içinde 'sarki_ekle()' adlı bir metod var ve bu metod albüme şarkı ekler.
Bunu yaparken bir şarkı numarası üretir ve öyle ekler.

Album içindeki şarkıları tek tek ekrana yazdırın.

İpuçları:
* önce albüm sonra şarkı üretin

Örnek Çağırma:
album = Album('Yesterday and Today', 'The Beatles', 1966)
album.sarki_ekle('Yesterday')
album.sarki_ekle('Act Naturally')
album.sarki_ekle('What Goes On')

Beklenen Sonuç:
Yesterday
Act Naturally
What Goes On
"""


# Çözüm 8:
class Sarki:
    def __init__(self, adi, sanatci, album, sarki_no):
        self.adi = adi
        self.sanatci = sanatci
        self.album = album
        self.sarki_no = sarki_no

    def __str__(self):
        return self.adi


class Album:
    def __init__(self, adi, sanatci, yil):
        self.adi = adi
        self.sanatci = sanatci
        self.yil = yil
        self.sarkilar = []

    def sarki_ekle(self, sarki_adi):
        # toplam şarkı sayısı
        sarki_no = len(self.sarkilar)

        # Sarki nesnesi yarat
        sarki = Sarki(sarki_adi, self.sanatci, self, sarki_no)

        # şimdi bu şarkıyı sarkilar listeye ekle
        self.sarkilar.append(sarki)

    def __str__(self):
        return self.adi


album = Album('Yesterday and Today', 'The Beatles', 1966)
album.sarki_ekle('Yesterday')
album.sarki_ekle('Act Naturally')
album.sarki_ekle('What Goes On')

# print(album.sarkilar)
#
# for sarki in album.sarkilar:
#     print(sarki)


# --------------------------------------------------------------------------------------#

# Soru 9:
"""
Sanatci adında bir class tanımlayın.
Her sanatçının; 'isim' ve 'albumler' özellikleri vardır.
'albumler' Soru 8'deki Album tipinde bir liste olacak.
Metodları: 
    * 'album_ekle(Album)' album ekler

Sanatçıya ait tüm şarkıları ekrana yazdırın.

Örnek Çağırma:
beatles = Sanatci('The Beatles')

album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.sarki_ekle('Yesterday')
album_1.sarki_ekle('Act Naturally')
beatles.album_ekle(album_1)

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.sarki_ekle('Let It Be')
album_2.sarki_ekle('For You Blue')
beatles.album_ekle(album_2)

Beklenen Sonuç:
Yesterday
Act Naturally
Let It Be
For You Blue
"""


# Çözüm 9:
class Sanatci:
    def __init__(self, isim):
        self.isim = isim
        self.albumler = []

    def album_ekle(self, album):
        if not album in self.albumler:
            self.albumler.append(album)


# Sanatci
beatles = Sanatci('The Beatles')

# Album
album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.sarki_ekle('Yesterday')
album_1.sarki_ekle('Act Naturally')
beatles.album_ekle(album_1)

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.sarki_ekle('Let It Be')
album_2.sarki_ekle('For You Blue')
beatles.album_ekle(album_2)

# print("----- albümler -----")
# for album in beatles.albumler:
#     print(album)
#
# print("----- şarkılar -----")
# for album in beatles.albumler:
#     for sarki in album.sarkilar:
#         print(sarki)
#
# print("----- şarkılar - comprehension ------")
# [print(sarki)
#  for album in beatles.albumler
#  for sarki in album.sarkilar]

# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Soru 8'de tanımladığınız Album class'ı için toplama (+) operatörünü overload edin.
Böylece 'Album + Album' şeklide toplama yapınca Python bize kızmasın ve 
iki albümün tüm şarkılarını bir arada bir liste olarak getirsin.
Eğer bu overload işlemini yapmadan direk olarak;
print(album_1 + album_2)
şeklinde çağırısanız hata alırsınız:
TypeError: unsupported operand type(s) for +: 'Album' and 'Album'

İpuçları:
* __add__()

Örnek Çağırma:
album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.sarki_ekle('Yesterday')
album_1.sarki_ekle('Act Naturally')

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.sarki_ekle('Let It Be')
album_2.sarki_ekle('For You Blue')

Beklenen Sonuç:
Yesterday
Act Naturally
Let It Be
For You Blue
"""


# Çözüm 10:
class Album:
    def __init__(self, adi, sanatci, yil):
        self.adi = adi
        self.sanatci = sanatci
        self.yil = yil
        self.sarkilar = []

    def sarki_ekle(self, sarki_adi):
        # toplam şarkı sayısı
        sarki_no = len(self.sarkilar)

        # Sarki nesnesi yarat
        sarki = Sarki(sarki_adi, self.sanatci, self, sarki_no)

        # şimdi bu şarkıyı sarkilar listeye ekle
        self.sarkilar.append(sarki)

    # __str__  -> print()
    def __str__(self):
        return self.adi

    # __add__  ->  + operatoru
    def __add__(self, other):
        toplam_sarkilar = self.sarkilar + other.sarkilar
        return toplam_sarkilar


album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.sarki_ekle('Yesterday')
album_1.sarki_ekle('Act Naturally')

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.sarki_ekle('Let It Be')
album_2.sarki_ekle('For You Blue')

sarkilar_toplami = album_1 + album_2

for sarki in sarkilar_toplami:
    print(sarki)

# --------------------------------------------------------------------------------------#
