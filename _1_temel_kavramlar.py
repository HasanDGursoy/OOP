"""
Object Oriented Programing (OOP)
Nesne Tabanlı Programlama

Nesne --> etrafımızda ki herşey

Python'da nesnelerin özellikleri:
* Öznitelikler (attribute)
* Davranışları (behavior)

Örnek :
Penguen
* Öznitelikleri : adi, yaşı , boyu , kilosu , rengi , türü
* davranışları : yüzme, yürüme, şarkı söyleme, dans etme

OOP : Kod tekrarını önlemek için var
DRY : Do not repeat yourself

"""

"""
Class (Sınıf):
Class bir nesnenin eskiz çizimidir.
Mimari çizimidir.
Nesnenin neye benzeyeceğini anlatır.

Örn: Bina bir nesnedir. O binanın kağıt üstündeki çizimi Class'dır.

Penguen :
Kağıda çizilmiş bir penguen, Sınıfıdır.
O çizimden yapılmış gerçek bir Penguen'de nesnedir.

"""


class Penguen:
    pass


"""
Class yaratmak için 'class' anahtar kelimesi kullanılır.
Tanımladığımız Class'ımızın adı Penguen.
"""

"""
Object (Nesne) : 
Nesne, Class'ın hayat bulmuş şeklidir. (instance)
Class'ın ete kemiğe bürünmüş halidir.
Instance : Tekil olarak Yaratılmış bir nesnedir.
"""

nesne = Penguen()

"""
Nesneler class'ların çağırılması ile oluşturulur.
"""

"""
Class Attribute:
Bütün Penguen'lerin ortak özellikleri vardır.
Bilimsel olarak türü (species) -> kuş
İşte Class'tan üretilmiş bütün varlıklarda (nesnelerde) ortak olan özelliklere:
Class Attribute denir.

Instance Attribute:
Tekil bir nesneye özel nitelikler;
Instance Attribute denir.
Penguen, yaşı, rengi , kilosu, boyu
"""
"""
Metod = Fonksiyon
Method'lar Class'lar için içinde tanımlanan fonksiyonlardır.
"""


class Penguen:
    # class attribute'ları (sınıf öznitelikleri)
    tur = 'Kuş'

    # instance attribute'ları (varlığın öznitelikleri)
    def __init__(self, p_ad, p_yas, p_renk):
        self.ad = p_ad
        self.yas = p_yas
        self.renk = p_renk


"""
self : o anda yaratılan nesneyi anlatır

"""

# iki adet penguen nesnesi yaratalım

kral_penguen = Penguen('Kral Penguen', 4, 'Turuncu')
sari_goz = Penguen('Sarı Gözlü Penguen', 1, 'Kahverengi')

# önce class attribute'larınızı print edelim
print(f'{kral_penguen.ad} in bilimsel türü : {kral_penguen.__class__.tur} ')
print(f'{sari_goz.ad} ün bilimsel türü : {kral_penguen.__class__.tur}')

# instance attribute'larını print edelim
print(f"{kral_penguen.ad}'in yaşı {kral_penguen.yas} ve rengei {kral_penguen.renk}")
print(f"{sari_goz.ad}'in yaşı {sari_goz.yas} ve rengi {sari_goz.renk}")

"""
Attribute'lara -> '.' ile erişilir.
* Class attribute ise -> .__class__.
* Instance Attribute -> .
"""

"""
__init__(self, .....):
Bir class'tan, nesne yaratılırken ilk çağırılan yaratıcı (yapıcı,constructor) metodudur.
__init__() instance oluşturur.

* self : O anda yaratılmakda olan nesneyi anlatır.
Nesnenin özellikleri : 
self.ad = ....
self.renk = ....
self.yas = ....

"""

"""
Methodlar (Davranışlar):
Method bir class içinde tanımlanmış bir fonksiyondur.
Nesnelerin davranışlarını anlatır.
"""


# Penguen class'ımıza method ekleyelim
class Penguen:
    # class attribute
    tur = 'Kuş'

    # instance attribute
    def __init__(self, ad, yas, renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

    # instance method (varlığın metodu)
    def yuzme(self):
        return f'{self.ad} yüzebilir.'

    def sarki_soyle(self, soyleyebilir_mi=False):
        if soyleyebilir_mi:
            return f'{self.ad} şarkı söylebilir.'
        else:
            return f'{self.ad} şarkı söylemeyemez.'

    def dans_et(self, dans_edebilir_mi=False):
        if dans_edebilir_mi:
            return f'{self.ad} dans edebilir.'
        else:
            return f'{self.ad} dans edemez.'


# yeni penguen nesneleri oluşturalım

makoroni = Penguen('Makaroni Penguen', 8, 'Sarı-Siyah')

print(makoroni.yuzme())
print(makoroni.dans_et())
# Makaroni Pengueni şarkı söylebilir

print(makoroni.sarki_soyle(True))

# Neşeli Ayaklar Pengueni yaratalım
neseli_ayaklar = Penguen('Neşeli Ayaklar', 1, 'Gri-Papyon')

print(neseli_ayaklar.yuzme())
print(neseli_ayaklar.sarki_soyle())
print(neseli_ayaklar.dans_et(True))

"""
Kalıtım (Inheritance) : 
Aynen gerçek hayattaki gibi, OOP'de Class'lar birbirinden Kalıtım alabilirler.
Kalıtım Alan Class -> Child Class, Derived Class
Kalıtım Veren Class -> Parent Class, Base Class (Ana Class)
"""


# Kuş Sınıfını Yaratalım
class Kus:

    def __init__(self):
        print('Kuş Yaratıldı')

    def kimim_ben(self):
        print('Ben bir Kuşum')

    def ucma(self):
        print('Kuşların çoğu uçabilir.')

    def yuzme(self):
        print('Kuşlar Yüzebilir')


# bir kuş nesnesi yaratalım

minik_kus = Kus()
minik_kus.kimim_ben()
minik_kus.ucma()
minik_kus.yuzme()

# Kuş türleri için bir ana class'ımız var.
# Baykuş da bir kuş --> child class olucak
print("======================================")
print()


# child class - derived class
class Baykus(Kus):
    # Bir sınıf hangi sınıfdan kalıtım alıyorsa, parantez içinde ana sınıf yazılır

    def __init__(self):
        # önce ana sınıfının, super(), __init__() methodunu çağırıcaz.
        super().__init__()
        print('Baykuş Yaratıldı')

    def kimim_ben(self):
        print('Ben bir Baykuşum')

    # Baykuş da tüm kuşlar gibi uçtuğu için ucma() metodunu override etmeye gerek yok.

    def yuzme(self):
        print('Baykuşlar yüzemez.')

    def gece_gorusu(self):
        print('Baykuşun gece görüşü vardır.')


kucuk_baykus = Baykus()
kucuk_baykus.ucma()
kucuk_baykus.kimim_ben()
kucuk_baykus.gece_gorusu()
kucuk_baykus.yuzme()

"""
Encapsulation (Gizleme) :
OOP'de dışarıdan direk olarak bizim class'ımız içindeki 
attribute 'lara erişilmesini istemeyebiliriz.

Attribute Gizleme : __ ile yapılır
İki alt tireli (__<name>) Private olmuş olur.
"""
print("=======================================")
print()


# Örneğin bir Telefon Sınıfımız olsun
class Telefon:
    def __init__(self):
        # telefonun standart fiyatını belirleyelim
        self.__fiyat = 1000

    def sat(self):
        print('Satış Fiyatı : {} TL dir.'.format((self.__fiyat * 3) - self.__fiyat))

    def set_fiyat(self, yeni_fiyat):
        # Kontrol -> fiyat negatif mi ?
        if yeni_fiyat <= 0:
            print('Negatif fiyat veremessin')
        else:
            self.__fiyat = yeni_fiyat

    def get_fiyat(self):
        return self.__fiyat


# şimdi bir telefon nesnesi yarat
telefon = Telefon()

# AttributeError: 'Telefon' object has no attribute '__fiyat'
# print(telefon.__fiyat)
# çünkü __fiyat -> Private

telefon.sat()
telefon.set_fiyat(10000)

# sadece fiyatı görmek istiyorum
print(telefon.get_fiyat())

"""
Get-Set Metotları --> Getter-Setter
Class'ın private attribute'ları için alma ve set etme işlemlerini yapar
"""

"""
Peki neden Encapsulation ?
Kontrolün Class'ta olması için var.
Set Metodunda konrol yapılır.
"""

# Örnek:
# Fiyatı -2000 Tl vermek istesek
telefon.set_fiyat(-2000)
print(telefon.get_fiyat())

# -------------------------- POLYMORPHISM ------------------------ #
"""
Polymphism:
Çok şekillik -> Bir arayüz(interface) farklı yerlerde farklı amaçlar için kullanılması.
"""


# Yukarıda kuş örneğimiz
# Kuş ana sınıfı vardır (parent class)

# Kuş Sınıfı yaratalım

class Kus:

    def __init__(self):
        print('Kuş yaratıldı')

    def kimim_ben(self):
        print('Ben bir Kuşum')

    def ucma(self):
        print('Kuşlar uçabilir')

    def yuzme(self):
        print('Kusalar yüzebilir.')


class Baykus(Kus):

    def __init__(self):
        # super().__init__()
        print('Baykuş Yaratıldı')

    def kimim_ben(self):
        print('Ben bir Baykuşum')

    def yuzme(self):
        print('Baykuşlar yüzemez.')

    def gece_gorusu(self):
        print('Baykuşun gece görüşü vardır.')


# Kus ana sınıfından kalıtım alan bir kus daha yapalım

class Penguen(Kus):
    def __init__(self):
        # super().__init__()
        print('Penguen Yaratıldı')

    def kimim_ben(self):
        print('Ben bir penguenim')

    def ucma(self):
        print('Penguen oldugum için uçamam')

    # Penguenler yüzdüğü için --> yuzme() method'u ana class'da kalsın


# Aynı sınıftan (Kus) kalıtım almış iki alt sınıfımız var (Baykus,Penguen)
# Polymorphism'i bir örnek ile görelim

# ortak arayüz
# ucma'yı test eden bir fonksiyon yazalım

def ucabilir_mi(kus):
    # parametre olarak gelen kus nesnesinin ucma metodunu cagıracak
    kus.ucma()


# şimdi üç adet nesne yaratalım
kus = Kus()
baykus = Baykus()
penguen = Penguen()

ucabilir_mi(kus)
ucabilir_mi(baykus)
ucabilir_mi(penguen)

# Bakın ucabilir_mi() Kus sınıfı türünden
# Bir nesne aldı ve onun ucma() metodunu çağırdı
# ucma() metodu çağırıldığı yere göre farklı davrandı.
# İşte aynı arayüzün farklı verilere göre farklı sonuçlar vermesine POLYMORPHISM denir.

