"""
Çoklu Kalıtım:
Bir sınıfın, birden fazla ana sınıfdan kalıtım alması

"""


# Örnek:
class Ana_1:
    pass


class Ana_2:
    pass


class Alt(Ana_1, Ana_2):
    pass


# Örnek:
# Saat ve Takvim -> SaatliTakvim ikisinden de kalıtım alan alt sınıf

class Saat:
    """
    Saat'i simüle eder
    """

    def __init__(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return f'{self.__saat} : {self.__dakika} : {self.__saniye}'


clock = Saat(0, 0, 0)
print(clock.saat_kac())
clock.saati_kur(10, 23, 57)
print(clock.saat_kac())


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


print("=========================================================")
takvim = Takvim(6, 11, 2019)
print(takvim.d)
print(takvim.m)
print(takvim.y)
print(takvim.bugun_ne())
takvim.takvim_kur(23, 1, 1888)
print(takvim.bugun_ne())


# Saatli Takvim Class

class SaatliTakvim(Saat, Takvim):
    """
    Saat ve Takvimi beraber tutar.
    """

    def __init__(self, gun, ay, yil, saat, dakika, saniye):
        Saat.__init__(self, saat, dakika, saniye)
        Takvim.__init__(self, gun, ay, yil)

    def saat_ve_takvim_cagir(self):
        deger = f'Saat : {self.saat_kac()} \n' \
                f'Gün  : {self.bugun_ne()}'
        return deger


# bu kadar basit
print("========== SAATLİ TAKVİM ============")
saatli_takvim = SaatliTakvim(15, 12, 1987, 15, 2, 11)
print(saatli_takvim.saat_ve_takvim_cagir())

