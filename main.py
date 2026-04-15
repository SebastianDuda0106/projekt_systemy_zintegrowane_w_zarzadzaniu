#Autorzy: Sebastian Duda, Jan Bielecki
logi_global=True

if logi_global:
    print("wczytywanie bibliotek (1/4)")
from src.product import product
if logi_global:
    print("wczytywanie bibliotek (2/4)")
from src.component import component
if logi_global:
    print("wczytywanie bibliotek (3/4)")
from src.menu import menu,menup,lista2_1_2_r,lista2_1_2_tyg
if logi_global:
    print("wczytywanie bibliotek (4/4)")
import os

clear_console=lambda: os.system('clear')

def edycja_mrp(tabela,tryb=0,logi=False):
    tabela.info()
    match(tryb):
        case 0:#wybór szczegółowy
            wybor=menu(lista2_1_2_r,f'wprowadź numer wiersza(1-{len(lista2_1_2_r)}): ')
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
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia(1-{tabela.weeks}): ')
            user_input='start'
            while not(isinstance(user_input,int)):
                try:
                    user_input=int(input('wprowadź wartość liczbową: '))
                except:
                    print('wprowadź poprawną liczbę')
            if wybor in range(0,7):
                tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 7:  tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 8:  tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 9:  tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor ==10:  tabela.req_amount     =tabela.product_info.loc[wiersz,kolumna]=user_input
        case 1:#wybór według wiersza
            wybor=menu(lista2_1_2_r,f'wprowadź numer wiersza(1-{len(lista2_1_2_r)}): ')
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
            if not logi:clear_console()
            tabela.info()
            if wybor in range(0,7):
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                for kolumna in range(1,tabela.weeks+1):
                    if not logi:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'\n{wiersz}, wprowadź nową wartość dla tygodnia {kolumna} : '))
                        except:
                            if not logi:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                    tabela.product_info.loc[wiersz,kolumna]=user_input
            if wybor in range(7,11):
                if not logi:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                    except:
                        print('wprowadź poprawną liczbę')

            if wybor   == 7: tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 8: tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 9: tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor ==10: tabela.req_amount     =tabela.product_info.loc[wiersz,kolumna]=user_input
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
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia od 1 do {tabela.weeks}:\n')
                for wiersz in lista2_1_2_r[0:6]:
                    if not logi:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'wprowadź nową wartość do "{wiersz}":\n'))
                        except:
                            if not logi:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                    tabela.product_info.loc[wiersz,kolumna]=user_input
            if wybor in range(2,6):
                kolumna=1
                if not logi:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                    except:
                        if not logi:clear_console()
                        tabela.info()
                        print('wprowadź poprawną liczbę')

            if wybor   == 2: tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 3: tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 4: tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
            elif wybor == 5: tabela.req_amount     =tabela.product_info.loc[wiersz,kolumna]=user_input
    
    if not logi:clear_console()
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

    saymessage=False
    tryb_edycji=2
    
    if logi:print("wczytywanie list menu")
    lista1=['Wyświetl','Edytuj','Przelicz','zapisz','odczytaj','ustawienia','Zamknij']
    lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
    lista1_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']
    lista2_1_1_r=['Przewidywany popyt','Produkcja','Dostępne','Czas realizacji','Na stanie']
    lista2_1_2=['[1]papier','[1]okładka','[2]skóra']
    lista2_1_1_tyg=['Wartości w tygodniu','Czas realizacji','Na stanie']
    lista6_1_t=['szczegółowy(wiersz,kolumna)','cały wiersz','cały tydzień']
    if logi == True:print("start programu")


    run=1
    while run==1:
        #menu główne
        if not logi:clear_console()
        if saymessage:
            print(message)
            saymessage=False
        match (menu(lista1)):
            case 1:#wyswietlanie
                if not logi:clear_console()
                match(menu(lista1_1)):
                    case 1:#wszystko
                        if logi == True:
                            print("informacje zeszyt")
                        else:clear_console()
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")
                        
                        if logi == True:
                            print("informacje papier")
                        else:clear_console()
                        papier.info()
                        input("Naciśnij enter aby kontynuować\n")
                        
                        if logi == True:
                            print("informacje okladka")
                        else:clear_console()
                        okladka.info()
                        input("Naciśnij enter aby kontynuować\n")

                        if logi == True:
                            print("informacje skora")
                        else:clear_console()
                        skora.info()
                        input("Naciśnij enter aby kontynuować\n")
                    case 2:#GHP
                        if logi == True:
                            print("informacje zeszyt")
                        else:clear_console()
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")
                    case 3:#MRP
                        if not logi:clear_console()
                        match(menu(lista1_1_2)):
                            case 1:#papier
                                if logi == True:
                                    print("informacje zeszyt")
                                else:clear_console()
                                papier.info()
                                input("Naciśnij enter aby kontynuować\n")
                            case 2:#okladka 
                                if logi == True:
                                    print("informacje okladka")
                                else:clear_console()
                                okladka.info()
                                input("Naciśnij enter aby kontynuować\n")
                            case 3:#skora
                                if logi == True:
                                    print("informacje skora")
                                else:clear_console()
                                skora.info()
                                input("Naciśnij enter aby kontynuować\n")
            case 2:#edytowanie
                if not logi:clear_console()
                match(menu(lista2_1)):
                    case 1:#GHP
                        if not logi:clear_console()
                        zeszyt.info()
                        match(tryb_edycji):
                            case 0:#wybór szczegółowy
                                #listy dla GHP
                                kolumna=1
                                wybor=menu(lista2_1_1_r,f'wprowadź numer wiersza(1-{len(lista2_1_1_r)}): ')
                                match(wybor):
                                    case 1:wiersz='Przewidywany popyt'
                                    case 2:wiersz='Produkcja'
                                    case 3:wiersz='Dostępne'
                                    case 4:wiersz='Czas realizacji'
                                    case 5:wiersz='Na stanie'
                                if wybor in range(0,4):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,zeszyt.weeks+1))),f'wprowadź numer tygodnia(1-{zeszyt.weeks}): ')
                                user_input='start'
                                while not(isinstance(user_input,int)):
                                    try:
                                        user_input=int(input('wprowadź nową wartość: '))
                                    except:
                                        print('wprowadź poprawną liczbę')
                                if wybor in range(0,4):
                                    zeszyt.product_info.loc[wiersz,kolumna]=user_input
                                elif wybor == 4: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.production_time=user_input
                                elif wybor == 5: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.stock=user_input
                            case 1:#wybór według wiersza
                                wybor=menu(lista2_1_1_r,f'wprowadź numer wiersza(1-{len(lista2_1_1_r)}): ')
                                match(wybor):
                                    case 1:wiersz='Przewidywany popyt'
                                    case 2:wiersz='Produkcja'
                                    case 3:wiersz='Dostępne'
                                    case 4:wiersz='Czas realizacji'
                                    case 5:wiersz='Na stanie'
                                if wybor in range(0,4):
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    for kolumna in range(1,zeszyt.weeks+1):
                                        if not logi:clear_console()
                                        zeszyt.info()
                                        user_input='start'
                                        while not(isinstance(user_input,int)):
                                            try:
                                                user_input=int(input(f'\n{wiersz}, wprowadź nową wartość dla tygodnia {kolumna} : '))
                                            except:
                                                if not logi:clear_console()
                                                zeszyt.info()
                                                print('wprowadź poprawną liczbę')
                                        zeszyt.product_info.loc[wiersz,kolumna]=user_input
                                if wybor in range(4,6):
                                    kolumna=1
                                    if not logi:clear_console()
                                    zeszyt.info()
                                    user_input='start'
                                    while not(isinstance(user_input,int)):
                                        try:
                                            user_input=int(input(f'wprowadź wartość liczbową: '))
                                        except:
                                            print('wprowadź poprawną liczbę')
                                if wybor == 4: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.production_time=user_input
                                elif wybor == 5: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.stock=user_input
                            case 2:#wybór według tygodnia
                                #listy dla GHP
                                wybor=menu(lista2_1_1_tyg)
                                match(wybor):
                                    case 1:wiersz=0
                                    case 2:wiersz='Czas realizacji'
                                    case 3:wiersz='Na stanie'
                                if wybor ==1:
                                    #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                                    kolumna=menup(list(map(lambda x:x,range(1,zeszyt.weeks+1))),f'wprowadź numer tygodnia od 1 do {zeszyt.weeks}:\n')
                                    for wiersz in lista2_1_1_r[0:3]:
                                        if not logi:clear_console()
                                        zeszyt.info()
                                        user_input='start'
                                        while not(isinstance(user_input,int)):
                                            try:
                                                user_input=int(input(f'wprowadź nową wartość do "{wiersz}":\n'))
                                            except:
                                                if not logi:clear_console()
                                                zeszyt.info()
                                                print('wprowadź poprawną liczbę')
                                        zeszyt.product_info.loc[wiersz,kolumna]=user_input
                                if wybor in range(2,4):
                                    kolumna=1
                                    if not logi:clear_console()
                                    zeszyt.info()
                                    user_input='start'
                                    while not(isinstance(user_input,int)):
                                        try:
                                            user_input=int(input(f'wprowadź wartość liczbową: '))
                                        except:
                                            if not logi:clear_console()
                                            zeszyt.info()
                                            print('wprowadź poprawną liczbę')
                                if wybor == 2: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.production_time=user_input
                                elif wybor == 3: zeszyt.product_info.loc[wiersz,kolumna]=zeszyt.stock=user_input
                        
                        if not logi:clear_console()
                        print("tabela po edycji")
                        zeszyt.info()
                        input("Naciśnij enter aby kontynuować\n")

                        if not logi:clear_console()
                        zeszyt.info()
                    
                    case 2:#MRP
                        #listy dla MRP
                        if not logi:clear_console()
                        match(menu(lista2_1_2)):
                            case 1:#papier
                                if not logi:clear_console()
                                edycja_mrp(papier,tryb_edycji)
                            case 2:#okladka
                                if not logi:clear_console()
                                edycja_mrp(okladka,tryb_edycji)
                            case 3:#skora
                                if not logi:clear_console()
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
                saymessage=True
                message='Przeliczone'
            case 4:#zapis
                zeszyt.saveToXLS()
                papier.saveToXLS()
                okladka.saveToXLS()
                skora.saveToXLS()
                saymessage=True
                message='zapisano do pliku xls'
            case 5:#odczyt
                try:
                    zeszyt.readXLS()
                    papier.readXLS()
                    okladka.readXLS()
                    skora.readXLS()
                    saymessage=True
                    message='odczytano z pliku xls'
                except:
                    saymessage=True
                    message='NIE odczytano z pliku xls!'
            case 6:#ustawienia
                setting=True
                while setting:
                    if not logi:clear_console()
                    lista6_1=[f'Zmień Tryb edycji (obecnie: {tryb_edycji+1} - {lista6_1_t[tryb_edycji]})\n 1 - szczegółowy(wiersz,kolumna),\n 2 - cały wiersz,\n 3 - cały tydzień','wróć']
                    wybor=menu(lista6_1)
                    match(wybor):
                        case 1:
                            tryb_edycji=(tryb_edycji+1)%3
                        case 2:
                            setting=False
            case 7:#bye bye
                print('Do zobaczenia!')
                run=0
                return 0
    return 1

if __name__ == "__main__":
    run=main()
