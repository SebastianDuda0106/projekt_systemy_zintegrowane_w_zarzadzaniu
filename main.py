#Autorzy: Sebastian Duda, Jan Bielecki

#samouczek
#ustawienia

logi_global=True

if logi_global:
    print("wczytywanie bibliotek (1/5)")
from src.product import product
if logi_global:
    print("wczytywanie bibliotek (2/5)")
from src.component import component
if logi_global:
    print("wczytywanie bibliotek (3/5)")
from src.menu import menu,menup,lista2_1_2_r,lista2_1_1_r,lista2_1_1_tyg,lista2_1_2_tyg,lista6_1_t,lista1,listatest,listatest_1
if logi_global:
    print("wczytywanie bibliotek (4/5)")
from src.menu import browse_file
if logi_global:
    print("wczytywanie bibliotek (5/5)")
import os

clear_console=lambda: os.system('cls' if os.name == 'nt' else 'clear')



def zmien_tryb_edycji(tryb_edycji,logi,samouczek):
    setting=True
    while setting:
        if not logi==1:clear_console()
        lista_wl=['wyłączone','włączone']
        lista6_1=[f'Zmień Tryb edycji (obecnie: {tryb_edycji+1} - {lista6_1_t[tryb_edycji]})\n 1 - szczegółowy(wiersz,kolumna),\n 2 - cały wiersz,\n 3 - cały tydzień'
                  ,f'Logi (obecnie: {lista_wl[logi]})'
                  ,f'Samouczek (obecnie: {lista_wl[samouczek]})'
                  ,'wróć']
        wybor=menu(lista6_1)
        match(wybor):
            case 1:
                tryb_edycji=(tryb_edycji+1)%3
            case 2:
                logi=(logi+1)%2
            case 3:
                samouczek=(samouczek+1)%2
            case 4:
                setting=False
    return tryb_edycji,logi,samouczek

def edycja_ghp(tabela,tryb=0,logi=0):
    if not logi==1:clear_console()
    tabela.info()
    match(tryb):
        case 0:#wybór szczegółowy
            #listy dla GHP
            kolumna=1
            wybor=menu(lista2_1_1_r,f'wprowadź numer wiersza(1-{len(lista2_1_1_r)}): ')
            match(wybor):
                case 1:wiersz='Przewidywany popyt'
                case 2:wiersz='Produkcja'
                case 3:wiersz='Czas realizacji'
                case 4:wiersz='Na stanie'
            if wybor in range(0,3):
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia(1-{tabela.weeks}): ')
            user_input='start'
            while not(isinstance(user_input,int)):
                try:
                    user_input=int(input('wprowadź nową wartość: '))
                    if wybor in range(0,3):
                        tabela.product_info.loc[wiersz,kolumna]=user_input
                    elif wybor == 3: tabela.product_info.loc[wiersz,kolumna]=tabela.production_time=user_input
                    elif wybor == 4: tabela.product_info.loc[wiersz,kolumna]=tabela.stock=user_input  
                except:
                    print('wprowadź poprawną liczbę')
                    user_input='start'
        case 1:#wybór według wiersza
            wybor=menu(lista2_1_1_r,f'wprowadź numer wiersza(1-{len(lista2_1_1_r)}): ')
            match(wybor):
                case 1:wiersz='Przewidywany popyt'
                case 2:wiersz='Produkcja'
                case 3:wiersz='Czas realizacji'
                case 4:wiersz='Na stanie'
            if wybor in range(0,3):
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                for kolumna in range(1,tabela.weeks+1):
                    if not logi==1:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'\n{wiersz}, wprowadź nową wartość dla tygodnia {kolumna} : '))
                            tabela.product_info.loc[wiersz,kolumna]=user_input
                        except:
                            if not logi==1:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                            user_input='start'
            if wybor in range(3,5):
                kolumna=1
                if not logi==1:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                        if wybor == 3: tabela.product_info.loc[wiersz,kolumna]=tabela.production_time=user_input
                        elif wybor == 4: tabela.product_info.loc[wiersz,kolumna]=tabela.stock=user_input    
                    except:
                        print('wprowadź poprawną liczbę')
                        user_input='start'
        case 2:#wybór według tygodnia
            #listy dla GHP
            wybor=menu(lista2_1_1_tyg)
            match(wybor):
                case 1:wiersz=0
                case 2:wiersz='Czas realizacji'
                case 3:wiersz='Na stanie'
            if wybor ==1:
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia od 1 do {tabela.weeks}:\n')
                for wiersz in lista2_1_1_r[0:2]:
                    if not logi==1:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'wprowadź nową wartość do "{wiersz}":\n'))
                            tabela.product_info.loc[wiersz,kolumna]=user_input
                        except:
                            if not logi==1:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                            user_input='start'
            if wybor in range(2,4):
                kolumna=1
                if not logi==1:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                        if wybor == 2: tabela.product_info.loc[wiersz,kolumna]=tabela.production_time=user_input
                        elif wybor == 3: tabela.product_info.loc[wiersz,kolumna]=tabela.stock=user_input
                    except:
                        if not logi==1:clear_console()
                        tabela.info()
                        print('wprowadź poprawną liczbę')
                        user_input='start'
    
    if not logi==1:
        clear_console()
    else:
        print("tabela po edycji")
        tabela.info()
        input("Naciśnij enter aby kontynuować\n")

def edycja_mrp(tabela,tryb=0,logi=0):
    if not logi==1:clear_console()
    tabela.info()
    kolumna=1
    match(tryb):
        case 0:#wybór szczegółowy
            wybor=menu(lista2_1_2_r,f'wprowadź numer wiersza(1-{len(lista2_1_2_r)}): ')
            wiersz=lista2_1_2_r[wybor-1]
            if wybor==1:
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia(1-{tabela.weeks}): ')
            user_input='start'
            while not(isinstance(user_input,int)):
                try:
                    user_input=int(input('wprowadź wartość liczbową: '))
                    if   wybor == 1:  tabela.product_info.loc[wiersz,kolumna]=user_input
                    elif wybor == 2:  tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
                    elif wybor == 3:  tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
                    elif wybor == 4:  tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
                    elif wybor == 5:  tabela.req_amount     =user_input
                except:
                    print('wprowadź poprawną liczbę')
                    user_input='start'     
        case 1:#wybór według wiersza
            wybor=menu(lista2_1_2_r,f'wprowadź numer wiersza(1-{len(lista2_1_2_r)}): ')
            wiersz=lista2_1_2_r[wybor-1]
            if not logi==1:clear_console()
            tabela.info()
            if wybor == 1:
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                for kolumna in range(1,tabela.weeks+1):
                    if not logi==1:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'\n{wiersz}, wprowadź nową wartość dla tygodnia {kolumna} : '))
                            tabela.product_info.loc[wiersz,kolumna]=user_input
                        except:
                            if not logi==1:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                            user_input='start'
            if wybor in range(2,6):
                if not logi==1:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                        if wybor   == 2: tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 3: tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 4: tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 5: tabela.req_amount     =user_input
                    except:
                        print('wprowadź poprawną liczbę')
                        user_input='start'
        case 2:#wybór według tygodnia
            wybor=menu(lista2_1_2_tyg)
            match(wybor):
                case 1:wiersz=0
                case 2:wiersz='Czas realizacji'
                case 3:wiersz='Wielkość partii'
                case 4:wiersz='Na stanie'
                case 5:wiersz='Ilość w BOM'
            if wybor == 1:
                #lista2_1_t=[''] #tutaj wpisać listę z numerami tygodni
                kolumna=menup(list(map(lambda x:x,range(1,tabela.weeks+1))),f'wprowadź numer tygodnia od 1 do {tabela.weeks}:\n')
                for wiersz in lista2_1_2_r[0:1]:
                    if not logi==1:clear_console()
                    tabela.info()
                    user_input='start'
                    while not(isinstance(user_input,int)):
                        try:
                            user_input=int(input(f'wprowadź nową wartość do "{wiersz}":\n'))
                            tabela.product_info.loc[wiersz,kolumna]=user_input
                        except:
                            if not logi==1:clear_console()
                            tabela.info()
                            print('wprowadź poprawną liczbę')
                            user_input='start'
            if wybor in range(2,6):
                kolumna=1
                if not logi==1:clear_console()
                tabela.info()
                user_input='start'
                while not(isinstance(user_input,int)):
                    try:
                        user_input=int(input(f'wprowadź wartość liczbową: '))
                        if wybor   == 2: tabela.production_time=tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 3: tabela.batch_size     =tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 4: tabela.stock          =tabela.product_info.loc[wiersz,kolumna]=user_input
                        elif wybor == 5: tabela.req_amount     =user_input
                    except:
                        if not logi==1:clear_console()
                        tabela.info()
                        print('wprowadź poprawną liczbę')
                        user_input='start'

    
    if not logi==1:
        clear_console()
    else:
        print("tabela po edycji")
        tabela.info()
        input("Naciśnij enter aby kontynuować\n")

def menu_tabela(tabela,tryb_edycji,logi,ghp=False,parent_demand=0):
    wyswietlanie=True
    while wyswietlanie==True:
        listatest_1[4]=f'Zmień Tryb edycji (obecnie: {tryb_edycji+1} - {lista6_1_t[tryb_edycji]})'
        if not logi==1:clear_console()
        tabela.info()
        match(menu(listatest_1)):
            case 1:
                if ghp:
                    edycja_ghp(tabela,tryb_edycji,logi)
                else:
                    edycja_mrp(tabela,tryb_edycji,logi)
            case 2:
                tabela.calculate()
                if not ghp:
                    tabela.getTotalDemand(parent_demand)
            case 3:
                try:
                    path = browse_file(tabela.name,True)
                    tabela.saveToXLS(path)
                except:
                    input('Nie udało się zapisać, naciśnij enter aby kontynuować\n')
            case 4:
                try:
                    path = browse_file()
                    tabela.readXLS(path)
                except:
                    input('Nie udało się odzczytać, naciśnij enter aby kontynuować\n')
            case 5:
                tryb_edycji=(tryb_edycji+1)%3
            case 6:
                wyswietlanie=False

def samouczekf(logi):
    if not logi==1:clear_console()
    print('Dlaczego Python?\n'\
    '1. Mamy z nim najwięcej doświadczenia\n'\
    '2. dzięki biblioteką numpy i pandas możemy ładnie wyświetlać dane w tabelach, jak i łatwo zapisywać i odczytywać dane do/z plików\n'\
    '3. dzięki bibliotece pyinstaller łatwo udało nam się skompilować program do formatu .exe'
        )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('Czym się zajmowaliśmy:\n'\
    'Sebastian: Menu główne, małe poprawki programu, pomoc przy algorytmie liczącym wartości w tabelach \n'\
    'Jan: Wszystko czego nie widać, struktura tabel, algorytm liczący, funkcje zapisu/odczytu danych \n'
        )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('menu główne, tutaj jest nasze menu główne:\n'\
        '1.samouczek <- tu się znajdujemy\n'\
        '2.tabele <- tu można zobaczyć tabele w naszym programie\n'\
        '3.Przelicz wszystko <- tym można przeliczyć wartości w tabelach np. po odczytaniu danych z pliku\n'\
        '4.zapisz wszystko <- tym można zapisać plik z wszystkimi tabelami do wybranego miejsca na dysku\n'\
        '5.odczytaj wszystko <- tym można odczytać plik wybrany z dysku\n'\
        '6.ustawienia <- tutaj można zmienić ustawienia(w tym wyłączyć ten samouczek)\n'\
        '7.Zamknij <- ta opcja zamyka program\n'
        )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('2.tabele - wyświetla liste tabel:\n'\
        'opcja.[poziom BOM]nazwa_tabeli(rodzic/GHP)\n'\
        '1.[0]zeszyt(GHP)<- tabela Głównego Harmonogramu Produkcji \n'\
        '2.[1]papier(zeszyt) <- tabela MRP 1 poziomu BOM\n'\
        '3.[1]okładka(zeszyt)\n'\
        '4.[2]skóra(okładka)\n'\
        '5.wróć do menu <- opcja wrócenia do menu głównego\n'
        )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('tak wygląda przykładowa tabela\n'\
        'nazwa_tabeli\n'
        '                                 1     2     3     4     5     6     7    8    9 <- numer tygodnia\n'\
        'Całkowite zapotrzebowanie        0     0  1280  1920     0     0  1280    0    0\n'\
        'Planowane przyjęcia              0     0     0     0     0     0     0    0    0\n'\
        'Przewidywane na stanie        1024  1024  1744  -176  1824  1824   544  544  544\n'\
        'Zapotrzebowanie netto            0     0   256   176   176     0     0    0    0\n'\
        'Planowane zamówienia          2000     0  2000     0     0     0     0    0    0\n'\
        'Planowane przyjęcie zamówień     0     0  2000     0  2000     0     0    0    0\n'\
        'Czas realizacji                  2\n'\
        'Wielkość partii               2000\n'\
        'Na stanie                     1024 \n'\
        'Poziom BOM                       1\n'\
        'Ilość w BOM                   64\n'\
        '1.edytuj<- można edytować dane\n'\
        '2.przelicz <- można przeliczyć dane w tabeli\n'\
        '3.zapisz <- można zapisać tylko przeglądaną tabelę do pliku\n'\
        '4.odczytaj <- można odczytać tabelę z pliku\n'\
        '5.Zmień Tryb edycji (obecnie: 1 - szczegółowy(wiersz,kolumna)) <- można zmienić tryb edytowania tabeli\n'\
        '6.wróć do tabel < można wrócić do poprzedniego menu wyboru tabel\n'
    )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('tryby edycji są do siebie bardzo podobne więc pokazany będzie tylko pierwszy(szczegółowy)\n\n'\
          'nazwa_tabeli\n'\
          '*wartości tabeli*\n'\
          'Planowane przyjęcia              0     0     0     0     0     0     0    0    0\n'\
          '*wartości tabeli*\n'\
          'opcja.wiersz_tabeli\n'\
          '1.Planowane przyjęcia<- wiersz tabeli\n'\
          '2.Czas realizacji <- właściwości tabeli\n'\
          '3.Wielkość partii <\n'\
          '4.Na stanie       <\n'\
          '5.Ilość w BOM     <\n'\
          'wprowadź numer wiersza(1-5): <- należy wybrać który wiersz lub właściwość tabeli chcemy zmienić\n\n'\

          'wprowadź numer tygodnia(1-9): <- jeżeli wybierzesz wiersz tabeli, to należy dobrać tydzień w którym chcesz zmienić wartość\n\n'\
          
          'wprowadź wartość liczbową: <-następnie należy wpisać jaka ma być nowa wartość\n\n'\
          'po edycji wracasz do poprzedniego menu tabeli\n'
        )
    input('Naciśnij enter aby kontynuować')
    if not logi==1:clear_console()
    print('6.ustawienia:\n'\
        'opcja.ustawienie(obecny_tryb)'
        '1.Zmień Tryb edycji (obecnie: 1 - szczegółowy(wiersz,kolumna))\n'\
        ' 1 - szczegółowy(wiersz,kolumna),\n'\
        ' 2 - cały wiersz,\n'\
        ' 3 - cały tydzień\n'\
        '2.Logi (obecnie: wyłączone)<-czyszczenie konsoli/ekranu oraz wyświetlanie bonusowych komunikatów\n'\
        '3.Samouczek (obecnie: włączone)<-wyświetlanie opcji samouczka w menu głównym\n'\
        '4.wróć  <- opcja powrotu do menu głównego\n'
        )
    if not logi==1:clear_console()
    print('I to wszystko z naszego samouczka, miłej pracy!')
    input('Naciśnij enter aby wrócić do menu głównego')

def main(logi=0,samouczek=1):
    if logi==1:print("wczytywanie wartości domyślnych GHP")
    
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
    
    if logi==1:print("wczytywanie wartości domyślnych papier")
    papier = component(
        name='papier',
        production_time=2,
        batch_size=4000,
        BOM_level=1,
        stock=1024,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.product_info.loc['Produkcja'].tolist(),
        weeks=weeks,
        req_amount=64
    )
    
    if logi==1: print("wczytywanie wartości domyślnych okladka")
    okladka = component(
        name='okladka',
        production_time=1,
        batch_size=30,
        BOM_level=1,
        stock=5,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.product_info.loc['Produkcja'].tolist(),
        weeks=weeks
    )
    
    if logi==1:print("wczytywanie wartości domyślnych skora")
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
    tryb_edycji=0
    
    if logi==1:print("wczytywanie list menu")
    if logi==1:print("start programu")

    run=1
    while run==1:
        #menu główne
        if not logi==1:clear_console()
        if saymessage:
            print(message)
            saymessage=False
        if samouczek==1:
            lista1=['samouczek','tabele','Przelicz wszystko','zapisz wszystko','odczytaj wszystko','ustawienia','Zamknij']
            wybor1=menu(lista1)
            wybor1-=1
        else:
            lista1=['tabele','Przelicz wszystko','zapisz wszystko','odczytaj wszystko','ustawienia','Zamknij']
            wybor1=menu(lista1)
        
        match (wybor1):
            case 0:
                samouczekf(logi)
            case 1:#tabele
                tabele=True
                while tabele:
                    if not logi==1:clear_console()
                    match(menu(listatest)):
                        case 1:#GHP
                            menu_tabela(zeszyt,tryb_edycji,logi,True)
                        case 2:#papier
                            menu_tabela(papier,tryb_edycji,logi,parent_demand=zeszyt.product_info.loc['Produkcja'].tolist())
                        case 3:#okladka
                            menu_tabela(okladka,tryb_edycji,logi,parent_demand=zeszyt.product_info.loc['Produkcja'].tolist())
                        case 4:#skora
                            menu_tabela(skora,tryb_edycji,logi,parent_demand=okladka.product_info.loc['Planowane zamówienia'].tolist())
                        case 5:#bye
                            tabele=False  
                if logi==1:print("przeliczanie wartości w tabelach")
                if logi==1:print("przeliczanie wartości w GHP")                 
                zeszyt.calculate()
                
                if logi==1:print("przeliczanie wartości w papier")
                papier.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                papier.calculate()      
                
                if logi==1:print("przeliczanie wartości w okladka")
                okladka.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                okladka.calculate()  

                if logi==1:print("przeliczanie wartości w skora")
                skora.getTotalDemand(okladka.product_info.loc['Planowane zamówienia'].tolist())
                skora.calculate()      
            case 2:#przeliczanie
                if logi==1:print("przeliczanie wartości w tabelach")
                if logi==1:print("przeliczanie wartości w GHP")                 
                zeszyt.calculate()
                
                if logi==1:print("przeliczanie wartości w papier")
                papier.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                papier.calculate()      
                
                if logi==1:print("przeliczanie wartości w okladka")
                okladka.getTotalDemand(zeszyt.product_info.loc['Produkcja'].tolist())
                okladka.calculate()  

                if logi==1:print("przeliczanie wartości w skora")
                skora.getTotalDemand(okladka.product_info.loc['Planowane zamówienia'].tolist())
                skora.calculate()
                saymessage=True
                message='Przeliczone'
            case 3:#zapis
                try:
                    path = browse_file('data',True)
                    zeszyt.saveToXLS(path)
                    papier.saveToXLS(path)
                    okladka.saveToXLS(path)
                    skora.saveToXLS(path)
                    saymessage=True
                    message='zapisano do pliku xlsx'
                except:
                    saymessage=True
                    message='NIE zapisano do pliku xlsx!'
            case 4:#odczyt
                path = browse_file()
                saymessage=True
                message=''
                try:
                    zeszyt.readXLS(path)
                    message+='odczytano tabele "zeszyt" z pliku xlsx\n'
                except:
                    message+='NIE odczytano tabeli "zeszyt" z pliku xlsx!\n'
                try:
                    papier.readXLS(path)
                    message+='odczytano tabele "papier" z pliku xlsx\n'
                except:
                    message+='NIE odczytano tabeli "papier" z pliku xlsx!\n'
                try:
                    okladka.readXLS(path)
                    message+='odczytano tabele "okladka" z pliku xlsx\n'
                except:
                    message+='NIE odczytano tabeli "okladka" z pliku xlsx!\n'
                try:
                    skora.readXLS(path)
                    message+='odczytano tabele "skora" z pliku xlsx\n'
                except:
                    message+='NIE odczytano tabeli "skora" z pliku xlsx!\n'
            case 5:#ustawienia
                [tryb_edycji,logi,samouczek]=zmien_tryb_edycji(tryb_edycji,logi,samouczek)      
            case 6:#bye bye
                print('Do zobaczenia!')
                run=0
                return 0
    return 1

if __name__ == "__main__":
    run=main()
