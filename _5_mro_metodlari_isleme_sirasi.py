"""
Çok seviyeli kalıtım:
Annane -> Anne -> Çocuk
"""


class AnneAnne(object):
    # AnneAnne'nin özellikleri
    pass


class Anne(AnneAnne):
    # AnneAnne'nin özellikleri
    # Anne'nin kendi özellikleri
    pass


class Cocuk(Anne):
    # AnneAnne Özellikleri
    # Anne'nin Özellikleri
    # Çocucuğun Özellikleri
    pass


# Örnek :
# Saat ve KumSaat'inden kalıtım alsın
# Saat ve Takvim -> SaatliTakvim ikisinden kalıtım alan alt sınıf

# Kum Saati

class KumSaati(object):
    def __init__(self):
        self.kum_saati_baslasin()
        print('selamlar')
    def kum_saati_baslasin(self):
        print('Kum Saati başladı')


# Saat Sınıfı
class Saat(KumSaati):
    """
    Saat'i simüle eder
    """

    def __init__(self, saat, dakika, saniye):
        self.saati_kur(saat, dakika, saniye)
        KumSaati.__init__(self)

    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return f'{self.__saat} : {self.__dakika} : {self.__saniye}'


# Takvim Class'ı
class Takvim(object):
    """
    Takvimi simule eder.
    """

    def __init__(self, d, m, y):
        self.takvim_kur(d, m, y)

    def takvim_kur(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def bugun_ne(self):
        return f'{self.d} : {self.m} : {self.y}'


# Saatli Takvim

class SaatliTakvim(Saat, Takvim):
    def __init__(self, gun, ay, yil, saat, dakika, saniye):
        Saat.__init__(self, saat, dakika, saniye)
        Takvim.__init__(self, gun, ay, yil)


# SaatliTakvim
saatli_takvim = SaatliTakvim(12, 1, 2020, 13, 25, 48)
print(saatli_takvim.bugun_ne())
print(saatli_takvim.saat_kac())

"""
Soru : Eğer aynı method bir kaç atada varsa, hangisini çalıştırır ? 
Cevap : En yakın kalıtım aldığı class dan başlicak
Method Resolution Order -> MRO
"""

# Class'ların Method Resolution Order -> MRO
print(f"MRO : {SaatliTakvim.__mro__}")
for m in SaatliTakvim.__mro__:
    print(m)





