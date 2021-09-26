"""

Ana Sınıf (Base Class)
    - Alt Sınıf 1 (Child Class)
    - Alt Sınıf 2 (Child Class)

"""
import math


class AnaSinif:
    # Ana sınıfın özellikleri
    pass


class AltSinif1(AnaSinif):
    # Ana Sınıfın Özellikleri
    # Alt Sınıf 1 'in özellikleri
    pass


class AltSinif2(AnaSinif):
    # Ana Sınıfın Özellikleri
    # Alt Sınıf 2 'in Özellikleri
    pass


# Örnek --> Şekil
class Sekil:
    """ Şekiller İçin Super Class """

    def __init__(self, renk='kırımızı'):
        self.renk = renk


# sub class -> Daire
class Daire(Sekil):
    """ Daire sınıfı , sekil sınıfından kalıtım alır. """

    def __init__(self, yaricap, renk='mavi'):
        self.yaricap = yaricap
        self.renk = renk

    def alan(self):
        return math.pi ** self.yaricap ** 2


# sub class -> Dikdörtgen

class Dikdortgen(Sekil):
    """ Diktorgen Sınıfı"""

    def __init__(self, kisa=1.0, uzun=1.0, renk='turuncu'):
        super().__init__(renk=renk)
        self.kisa = kisa
        self.uzun = uzun

    def alan(self):
        return self.kisa * self.uzun


# sub class -> kare

class Kare(Sekil):

    def __init__(self, kenar=1.0, renk='beyaz'):
        super().__init__(renk=renk)
        self.kenar = kenar

    def alan(self):
        return self.kenar ** 2


# Nesneler yarat

# Sekil
se = Sekil('Mor')
print('Sekil nesnesi olan se nin rengi : ', se.renk)

# Daire
da = Daire(5)
print("Daire nesnesi olan da'nın rengi : ", da.yaricap)
print("Dairenin rengi : ", da.renk)

# Dikdörtgen
dk = Dikdortgen(10, 20)
print("Dikdörtgenin alanı : ", dk.alan())
print("Dikdörtgenin rengi : ", dk.renk)

"""
object Class'ı:
Python'da bütün classların atası, 'object' classıdır
Tüm sınıflar 'object' sınıfından gelir
"""

# class Sekil : => class Sekil(object)
print("Sekil sınıfı, object sınıfının alt sınıfı mı ? : ", isinstance(se, object))

# issubclass()
# Kare, Sekilin alt sınıfı mı ?
print(issubclass(Kare, Sekil))
