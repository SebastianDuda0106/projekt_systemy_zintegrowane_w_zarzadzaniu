#Autorzy: Sebastian Duda, Jan Bielecki
logi_global=True


if logi_global:
    print("wczytywanie bibliotek")
from src.product import product
from src.component import component
from src.menu import menu,menup,lista2_1_2_r,lista2_1_2_tyg
import os

def edycja_mrp(tabela,tryb=0,logi=False):
    tabela.info()
    match(tryb):
        case 0:#wybór szczegółowy
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
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))))
            user_input='start'
            while not(isinstance(user_input,int)):
                try:
                    user_input=int(input('wprowadź wartość liczbową: '))
                except:
                    print('enter correct input')
            if wybor in range(0,7):
                tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 7: tabela.production_time=user_input
            elif wybor == 8: tabela.batch_size=user_input
            elif wybor == 9: tabela.stock=user_input
            elif wybor == 10: tabela.req_amount=user_input
        case 1:#wybór według wiersza
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
            if not logi:os.system('cls')
            tabela.info()
            if wybor in range(0,7):
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                for kolumna in range(1,tabela.weeks+1):
                    if not logi:os.system('cls')
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'tydzień numer:{kolumna} wprowadź wartość liczbową: '))
                        except:
                            if not logi:os.system('cls')
                            tabela.info()
                            print('enter correct input')
                    tabela.product_info.loc[wiersz,kolumna]=user_input
            if wybor in range(7,11):
                if not logi:os.system('cls')
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                    except:
                        print('enter correct input')

            if wybor == 7: tabela.production_time=user_input
            elif wybor == 8: tabela.batch_size=user_input
            elif wybor == 9: tabela.stock=user_input
            elif wybor == 10: tabela.req_amount=user_input
        case 2:#wybór według tygodnia
            wybor=menu(lista2_1_2_tyg)
            match(wybor):
                case 1:wiersz=0
                case 2:wiersz='Czas realizacji'
                case 3:wiersz='Wielkość parii'
                case 4:wiersz='Na stanie'
                case 5:wiersz='Ilość w BOM'
            if wybor == 1:
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))))
                for wiersz in lista2_1_2_r[0:6]:
                    if not logi:os.system('cls')
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'{wiersz}: wprowadź wartość liczbową: '))
                        except:
                            if not logi:os.system('cls')
                            tabela.info()
                            print('enter correct input')
                    tabela.product_info.loc[wiersz,kolumna]=user_input
            if wybor in range(2,6):
                if not logi:os.system('cls')
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                    except:
                        if not logi:os.system('cls')
                        tabela.info()
                        print('enter correct input')

            if wybor == 2:tabela.production_time=user_input
            elif wybor == 3: tabela.batch_size=user_input
            elif wybor == 4: tabela.stock=user_input
            elif wybor == 5: tabela.req_amount=user_input
    
    if not logi:os.system('cls')
    print("tabela po edycji")
    tabela.info()
    input("Naciśnij enter aby kontynuować\n")


def main(logi=False):
    
    if logi:print("wczytywanie wartości domyślnych GHP")
    
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
    
    if logi:print("wczytywanie wartości domyślnych papier")
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
    
    if logi: print("wczytywanie wartości domyślnych okladka")
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
    
    if logi:print("wczytywanie wartości domyślnych skora")
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

    
    if logi:print("wczytywanie list menu")
    lista1=['Wyświetl','Edytuj','Przelicz','Zamknij']
    lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
    lista1_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']
    lista2_1_1_r=['Przewidywany popyt','Produkcja','Dostępne','Czas realizacji','Na stanie']
    lista2_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1_1_tyg=['Wartości w tygodniu','Czas realizacji','Na stanie']
    if logi == True:print("start programu")

    przelicz=False
    tryb_edycji=2

    run=1
    while run==1:
        #menu główne
        if not logi:os.system('cls')
        if przelicz:
            print('Przeliczone')
            przelicz=False
        match (menu(lista1)):
            case 1:#wyswietlanie
                if not logi:os.system('cls')
                match(menu(lista1_1)):
                    case 1:#wszystko
                        if logi == True:
                            print("informacje zeszyt")
                        else:os.system('cls')
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")
                        
                        if logi == True:
                            print("informacje papier")
                        else:os.system('cls')
                        papier.info()
                        input("Naciśnij enter aby kontynuować\n")
                        
                        if logi == True:
                            print("informacje okladka")
                        else:os.system('cls')
                        okladka.info()
                        input("Naciśnij enter aby kontynuować\n")

                        if logi == True:
                            print("informacje skora")
                        else:os.system('cls')
                        skora.info()
                        input("Naciśnij enter aby kontynuować\n")
                    case 2:#GHP
                        if logi == True:
                            print("informacje zeszyt")
                        else:os.system('cls')
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")
                    case 3:#MRP
                        if not logi:os.system('cls')
                        match(menu(lista1_1_2)):
                            case 1:#papier
                                if logi == True:
                                    print("informacje zeszyt")
                                else:os.system('cls')
                                papier.info()
                                input("Naciśnij enter aby kontynuować\n")
                            case 2:#okladka 
                                if logi == True:
                                    print("informacje okladka")
                                else:os.system('cls')
                                okladka.info()
                                input("Naciśnij enter aby kontynuować\n")
                            case 3:#skora
                                if logi == True:
                                    print("informacje skora")
                                else:os.system('cls')
                                skora.info()
                                input("Naciśnij enter aby kontynuować\n")
            case 2:#edytowanie
                if not logi:os.system('cls')
                match(menu(lista2_1)):
                    case 1:#GHP
                        zeszyt.info()
                        match(tryb_edycji):
                            case 0:#wybór szczegółowy
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
                            case 1:#wybór według wiersza
                                wybor=menu(lista2_1_1_r)
                                match(wybor):
                                    case 1:wiersz='Przewidywany popyt'
                                    case 2:wiersz='Produkcja'
                                    case 3:wiersz='Dostępne'
                                    case 4:wiersz='Czas realizacji'
                                    case 5:wiersz='Na stanie'
                                if wybor in range(0,4):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    for kolumna in range(1,zeszyt.weeks+1):
                                        if not logi:os.system('cls')
                                        zeszyt.info()
                                        user_input='start'
                                        while not(isinstance(user_input,int)):
                                            try:
                                                user_input=int(input(f'tydzień numer:{kolumna} wprowadź wartość liczbową: '))
                                            except:
                                                if not logi:os.system('cls')
                                                zeszyt.info()
                                                print('enter correct input')
                                        zeszyt.product_info.loc[wiersz,kolumna]=user_input
                                if wybor in range(4,6):
                                    if not logi:os.system('cls')
                                    zeszyt.info()
                                    user_input='start'
                                    while not(isinstance(user_input,int)):
                                        try:
                                            user_input=int(input(f'wprowadź wartość liczbową: '))
                                        except:
                                            print('enter correct input')
                                if wybor == 4: zeszyt.production_time=user_input
                                elif wybor == 5: zeszyt.stock=user_input
                            case 2:#wybór według tygodnia
                                #listy dla GHP
                                wybor=menu(lista2_1_1_tyg)
                                match(wybor):
                                    case 1:wiersz=0
                                    case 2:wiersz='Czas realizacji'
                                    case 3:wiersz='Na stanie'
                                if wybor ==1:
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,zeszyt.weeks+1))))
                                    for wiersz in lista2_1_1_r[0:3]:
                                        if not logi:os.system('cls')
                                        zeszyt.info()
                                        user_input='start'
                                        while not(isinstance(user_input,int)):
                                            try:
                                                user_input=int(input(f'{wiersz}: wprowadź wartość liczbową: '))
                                            except:
                                                if not logi:os.system('cls')
                                                zeszyt.info()
                                                print('enter correct input')
                                        zeszyt.product_info.loc[wiersz,kolumna]=user_input
                                    if wybor in range(2,4):
                                        if not logi:os.system('cls')
                                        zeszyt.info()
                                        user_input='start'
                                        while not(isinstance(user_input,int)):
                                            try:
                                                user_input=int(input(f'wprowadź wartość liczbową: '))
                                            except:
                                                if not logi:os.system('cls')
                                                zeszyt.info()
                                                print('enter correct input')
                                elif wybor == 4: zeszyt.production_time=user_input
                                elif wybor == 5: zeszyt.stock=user_input
                        
                        if not logi:os.system('cls')
                        print("tabela po edycji")
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")

                        if not logi:os.system('cls')
                        zeszyt.info()

                        
                    case 2:#MRP
                        #listy dla MRP
                        if not logi:os.system('cls')
                        match(menu(lista2_1_2)):
                            case 1:#papier
                                if not logi:os.system('cls')
                                edycja_mrp(papier,tryb_edycji)
                            case 2:#okladka
                                if not logi:os.system('cls')
                                edycja_mrp(okladka,tryb_edycji)
                            case 3:#skora
                                if not logi:os.system('cls')
                                edycja_mrp(skora,tryb_edycji)
            case 3:#przeliczanie
                if logi == True:print("przeliczanie wartości w tabelach")
                if logi == True:print("przeliczanie wartości w GHP")                 
                zeszyt.calculate()
                
                if logi == True:print("przeliczanie wartości w papier")
                papier.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                papier.calculate()      
                
                if logi == True:print("przeliczanie wartości w okladka")
                okladka.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                okladka.calculate()  

                if logi == True:print("przeliczanie wartości w skora")
                skora.getTotalDemand(okladka.product_info.loc['Planowane zamówienia'].tolist())
                skora.calculate()
                przelicz=True
            case 4:#bye bye
                print('Do zobaczenia!')
                run=0
                zeszyt.saveToXLS()
                return 0
    return 1

if __name__ == "__main__":
    run=main()
