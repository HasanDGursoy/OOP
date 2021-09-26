class Nokta:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __str__() metodunu overload edelim
    def __str__(self):
        return f'Bu bir noktadir. Koordinatları : x = {self.x} y = {self.y}'
