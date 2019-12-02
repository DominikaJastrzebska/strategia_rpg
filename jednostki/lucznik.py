from wojownik import Wojownik

class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 40
        # self.doswiadczenie = 0
        self.strzaly = 10

    # def __repr__(self):  # prawie to samo, co str
    #     return f'Lucznik: hp = {self.zycie}, exp = {self.doswiadczenie}, arrow = {self.strzaly}'
    #
    # def maszeruj(self, dystans):
    #     print(f'Lucznik: Przeszedłem {dystans} m')
    #     self.doswiadczenie += 0.2 * dystans

    def atakuj(self):
        if self.strzaly > 0:
            print('Lucznik: Wypuściłem strzałę!')
            self.doswiadczenie += 0.4
            self.strzaly -= 1
        elif self.strzaly == 0:
            print('Lucznik: Nie mam strzał, nie zastrzelę Cię')
