from wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 60
        # self.doswiadczenie = 0

    # def __repr__(self):  # prawie to samo, co str
    #     return f'Rycerz: hp = {self.zycie}, exp = {self.doswiadczenie}'
    #
    # def maszeruj(self, dystans):
    #     print(f'Rycerz: Przeszedłem {dystans} m')
    #     self.doswiadczenie += 0.2 * dystans

    def atakuj(self):
        print('Rycerz: Machnąłem mieczem!')
        self.doswiadczenie += 0.3
