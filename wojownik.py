class Wojownik:
    def __init__(self):
        self.doswiadczenie = 0

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f'{nazwa}: hp={self.zycie}, exp={self.doswiadczenie}'

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f'{nazwa}: Przeszedłem {dystans} m')
        self.doswiadczenie += 0.2 * dystans


print('Base Class - Wojownik')
