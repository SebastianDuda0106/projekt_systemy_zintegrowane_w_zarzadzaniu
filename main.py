#Autorzy: Sebastian Duda, Jan Bielecki
from src.product import product
from src.component import component
from src.menu import menu,menup

def main():
    production_amount=[0,0,0,0,20,30,0,0,20]
    weeks=len(production_amount)
    

    zeszyt = product(
        name='zeszyt',
        production_time=2,
        stock=20,
        req_amount=[5,5,5,5,10,15,30,5,10],
        production_amount=production_amount,
        weeks=weeks
    )
    papier = component(
        name='papier',
        production_time=2,
        batch_size=4000,
        BOM_level=1,
        stock=1024,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.production_amount,
        weeks=weeks,
        req_amount=64
    )
    okladka = component(
        name='okladka',
        production_time=1,
        batch_size=30,
        BOM_level=1,
        stock=5,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.production_amount,
        weeks=weeks
    )
    skora = component(
        name='skora',
        production_time=1,
        batch_size=50,
        BOM_level=2,
        stock=40,
        parent_assembly_time=okladka.production_time,
        parent_demand=okladka.product_info.loc['Planowane zamówienia'].tolist(),
        weeks=weeks
    )
    lista1=['Wyświetl','Edytuj','Przelicz','Zamknij']
    lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
    lista1_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']
    lista2_1_1_r=['Przewidywany popyt',
        'Produkcja',
        'Dostępne',
        'Czas realizacji',
        'Na stanie']
    lista2_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1_2_r=['Całkowite zapotrzebowanie',
                'Planowane przyjęcia',
                'Przewidywane na stanie',
                'Zapotrzebowanie netto',
                'Planowane zamówienia',
                'Planowane przyjęcie zamówień',
                'Czas realizacji',
                'Wielkość parii',
                'Na stanie',
                'Ilość w BOM']
    run=1
    while run==1:
        #menu główne
        match (menu(lista1)):
            case 1:
                #wyswietlanie
                match(menu(lista1_1)):
                    case 1:
                        zeszyt.info()
                        papier.info()
                        okladka.info()
                        skora.info()
                    case 2:
                        zeszyt.info()
                    case 3:
                        match(menu(lista1_1_2)):
                            case 1: papier.info()
                            case 2: okladka.info()
                            case 3: skora.info()
            case 2:
                #edytowanie
                match(menu(lista2_1)):
                    case 1:
                        zeszyt.info()
                        #listy dla GHP
                        wybor=menu(lista2_1_1_r)
                        match(wybor):
                            case 1:wiersz='Przewidywany popyt'
                            case 2:wiersz='Produkcja'
                            case 3:wiersz='Dostępne'
                            case 4:wiersz='Czas realizacji'
                            case 5:wiersz='Na stanie'
                        if wybor in range(0,4):
                            #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                            kolumna=menup(list(map(lambda x:x,range(1,zeszyt.weeks+1))))
                        user_input='start'
                        while not(isinstance(user_input,int)):
                            try:
                                user_input=int(input('wprowadź wartość liczbową: '))
                            except:
                                print('enter correct input')
                        if wybor in range(0,4):
                            zeszyt.product_info.loc[wiersz,kolumna]=user_input
                            print(zeszyt.product_info.loc[wiersz,kolumna])
                        elif wybor == 4: zeszyt.production_time=user_input
                        elif wybor == 5: zeszyt.stock=user_input
                    case 2:
                        #listy dla MRP
                        
                        match(menu(lista2_1_2)):
                            case 1:
                                papier.info()
                                wybor=menu(lista2_1_2_r)
                                match(wybor):
                                    case 1:wiersz='Całkowite zapotrzebowanie'
                                    case 2:wiersz='Planowane przyjęcia'
                                    case 3:wiersz='Przewidywane na stanie'
                                    case 4:wiersz='Zapotrzebowanie netto'
                                    case 5:wiersz='Planowane zamówienia'
                                    case 6:wiersz='Planowane przyjęcie zamówień'
                                    case 7:wiersz='Czas realizacji'
                                    case 8:wiersz='Wielkość parii'
                                    case 9:wiersz='Na stanie'
                                    case 10:wiersz='Ilość w BOM'
                                if wybor in range(0,7):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,papier.weeks+1))))
                                user_input='start'
                                while not(isinstance(user_input,int)):
                                    try:
                                        user_input=int(input('wprowadź wartość liczbową: '))
                                    except:
                                        print('enter correct input')
                                if wybor in range(0,7):
                                    papier.product_info.loc[wiersz,kolumna]=user_input
                                elif wybor == 7: papier.production_time=user_input
                                elif wybor == 8: papier.batch_size=user_input
                                elif wybor == 9: papier.stock=user_input
                                elif wybor == 10: papier.req_amount=user_input
                            case 2:
                                okladka.info()
                                wybor=menu(lista2_1_2_r)
                                match(wybor):
                                    case 1:wiersz='Całkowite zapotrzebowanie'
                                    case 2:wiersz='Planowane przyjęcia'
                                    case 3:wiersz='Przewidywane na stanie'
                                    case 4:wiersz='Zapotrzebowanie netto'
                                    case 5:wiersz='Planowane zamówienia'
                                    case 6:wiersz='Planowane przyjęcie zamówień'
                                    case 7:wiersz='Czas realizacji'
                                    case 8:wiersz='Wielkość parii'
                                    case 9:wiersz='Na stanie'
                                    case 10:wiersz='Ilość w BOM'
                                if wybor in range(0,7):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,okladka.weeks+1))))
                                user_input='start'
                                while not(isinstance(user_input,int)):
                                    try:
                                        user_input=int(input('wprowadź wartość liczbową: '))
                                    except:
                                        print('enter correct input')
                                if wybor in range(0,7):
                                    okladka.product_info.loc[wiersz,kolumna]=user_input
                                elif wybor == 7: okladka.production_time=user_input
                                elif wybor == 8: okladka.batch_size=user_input
                                elif wybor == 9: okladka.stock=user_input
                                elif wybor == 10: okladka.req_amount=user_input
                            case 3:
                                skora.info()
                                wybor=menu(lista2_1_2_r)
                                match(wybor):
                                    case 1:wiersz='Całkowite zapotrzebowanie'
                                    case 2:wiersz='Planowane przyjęcia'
                                    case 3:wiersz='Przewidywane na stanie'
                                    case 4:wiersz='Zapotrzebowanie netto'
                                    case 5:wiersz='Planowane zamówienia'
                                    case 6:wiersz='Planowane przyjęcie zamówień'
                                    case 7:wiersz='Czas realizacji'
                                    case 8:wiersz='Wielkość parii'
                                    case 9:wiersz='Na stanie'
                                    case 10:wiersz='Ilość w BOM'
                                if wybor in range(0,7):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,skora.weeks+1))))
                                user_input='start'
                                while not(isinstance(user_input,int)):
                                    try:
                                        user_input=int(input('wprowadź wartość liczbową: '))
                                    except:
                                        print('enter correct input')
                                if wybor in range(0,7):
                                    skora.product_info.loc[wiersz,kolumna]=user_input
                                elif wybor == 7: skora.production_time=user_input
                                elif wybor == 8: skora.batch_size=user_input
                                elif wybor == 9: skora.stock=user_input
                                elif wybor == 10: skora.req_amount=user_input
            case 3:
                zeszyt.calculate()
                papier.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                papier.calculate()      
                okladka.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                okladka.calculate()  
                skora.getTotalDemand(okladka.product_info.loc['Planowane zamówienia'].tolist())
                skora.calculate()      
            case 4:
                print('Do zobaczenia!')
                run=0
                zeszyt.saveToXLS()
                return 0
    return 1

if __name__ == "__main__":
    run=1
    while run:
        run=main()
