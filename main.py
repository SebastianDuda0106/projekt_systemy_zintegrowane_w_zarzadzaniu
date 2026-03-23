#Autorzy: Sebastian Duda, Jan Bielecki
def main():
    print("Hello from projekt-systemy-zintegrowane-w-zarzadzaniu!")
    #hello(str(input("what is your name?\n")))
    x= tabela('acocieto')
    for row in x.table:
        print(row)

# obj tabela
    # czas realizacji
    # ilość parti   
    # ilość wymagana
    # poziom bom

class tabela:
    def __init__(self,name):
        self.time=2#czas realizacji
        self.delivery_amount=80#wielkosc partii
        self.bom_level=1#poziom bom
        self.storage=80#na stanie
        self.bom_amount=4#ilosc w bom
        self.table=[
            [1,2,3,4,5,6],# tydzien
            [0,0,0,0,0,0],#GHP Przewydiwany popyt
            [0,0,0,72,0,160],#calkowite zapotrzebowanie/GHP produkcja
            [0,0,0,0,0,0],#planowanie przyjecia
            [40,40,48,48,-32],#przewidywane na stanie/GHP dostepne
            [0,0,0,32,0,112],#zapotrzebowanie netto
            [0,0,0,80,0,80],#planowane przyjecie zamowien
            [0,0,0,80,0,80]#planowane przyjecie zamowien
                    ]


def hello(name):
    print(f'Hello {name}!')

if __name__ == "__main__":
    main()
