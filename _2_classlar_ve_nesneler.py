# Class tanımlayalım
# docstring - > class

class Araba:
    """
    Bu araba classıdır.
    """

    marka = 'BMW'

    def calisma(self):
        print('Bu araba çalışıyor')


# marka attribute'una erişmek için
# nesne yaratmadan direk class olarak erişmek
print(Araba.marka)

"""
dunder (double underscore):
iki alt tire (__) metodlara ve attribute'lara 'dunder' adı verilir.
"""

# tanımladığımız Araba Class'ının docstring'ine erişelim
print(Araba.__doc__)

# calisma metdonun özelliği
print(Araba.calisma)

# calisma() cağırsak ne olacakdı ?
# Araba.calisma()
# nesne yaratmadan çağırdığımız için --> TypeError : calisma() missing required positional argument : 'self'

yeni_araba = Araba()
print(yeni_araba.marka)
yeni_araba.calisma()
# calisma() metodu çalışabilir çünkü bir nesne var artık

"""
Soru 'self' parametresi nerde ? 
yeni_araba.calisma()

Cevap : 
'self' parametresi yeni_araba'nın kendisi
"""

# ilk parametre 'self' ise -> Araba.calisma(yeni_araba)
Araba.calisma(yeni_araba)

# Örnek
import math


class Cember:

    def __init__(self, yaricap):
        self.__yaricap = yaricap

    def get_yaricap(self):
        return self.__yaricap

    def set_yaricap(self, yeni_yaricap):
        if yeni_yaricap > 0:
            self.__yaricap = yeni_yaricap
        else:
            print('Yarı çap pozitif olmalı')

    def cevre(self):
        return (self.__yaricap ** 2) * math.pi


cember_1 = Cember(10)
print(cember_1.get_yaricap())
cember_1.set_yaricap(11)
print(cember_1.get_yaricap())
print(cember_1.cevre())

print('----------------- set -----------------')
cember_1.set_yaricap(20)
cevre = cember_1.cevre()
print(cevre)

# Yeni bir sınıf
print('-------------- Ogrenci Sınıfı -----------------')


class Ogrenci:
    def __init__(self, isim, yas, sinif):
        self.isim = isim
        self.yas = yas
        self.sinif = sinif
        self.kod_adi = 'Sillias'


ogr = Ogrenci('Cin Ali', 8, '3-A')
print(ogr.isim)
print(ogr.yas)
print(ogr.sinif)
print(ogr.kod_adi)

print('--------------------- Silme ---------------------')

# nesnelerin attribute'larını silelim --> del

del ogr.yas
# print(ogr.yas)  bunu çalıştırırsak hata alıcaz.

"""
Attribute Silme:
del nesne.attribute

Nesnenin Kendisini Silmek:
del nesne
"""
# Ogrenci nesnesi --> ogr -> sil
del ogr
# print(ogr.isim)
