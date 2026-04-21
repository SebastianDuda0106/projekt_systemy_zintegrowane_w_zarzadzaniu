try:
    import tkinter
    tkinter_import=True
except:
    tkinter_import=False
from tkinter import filedialog
import os

def browse_file(filename='data',zapis=False):
    if tkinter_import:
        root = tkinter.Tk()
        root.withdraw()
        currdir = os.getcwd()
        #odczyt
        fname=currdir
        if not zapis:
            fname = filedialog.askopenfilename(title='odczyt',parent=root, initialdir=currdir, filetypes = (("excel files", "*.xlsx"),("All files", "*") ))
        #zapis
        else:
            fname = filedialog.asksaveasfilename(defaultextension=".xlsx",title='zapisz',initialfile=filename, filetypes=[("excel files", "*.xlsx"), ("All files", "*.*")])
    else:
        fname='data.xlsx'

    return fname

def menu(lista,message=0):
    if message == 0:
        message=f'wprowadź liczbę od 1 do {len(lista)}\n'
    max=len(lista)
    user_input='start'
    while not(isinstance(user_input,int) and (user_input in range(0+1,max+1))):
        for i in range(0,max):
            print(f'{i+1}.{lista[i]}')    
        try:
            user_input=int(input(message))
        except:
            print('wprowadź poprawną liczbę')
    return user_input
def menup(lista,message=0):
    if message == 0:
        message=f'wprowadź liczbę od 1 do {len(lista)}\n'
    max=len(lista)
    user_input='start'
    while not(isinstance(user_input,int) and (user_input in range(0+1,max+1))):   
        try:
            user_input=int(input(message))
        except:
            print('wprowadź poprawną liczbę')
    return user_input

lista1=['tabele','Przelicz wszystko','zapisz wszystko','odczytaj wszystko','ustawienia','Zamknij']
lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
lista1_1_2=['[1]papier','[1]okładka','[2]skóra']
lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']
lista2_1_1_r=['Przewidywany popyt','Produkcja','Dostępne','Czas realizacji','Na stanie']
lista2_1_1_tyg=['Wartości w tygodniu','Czas realizacji','Na stanie']
lista2_1_2=['[1]papier','[1]okładka','[2]skóra']
lista2_1_2_r=['Całkowite zapotrzebowanie','Planowane przyjęcia','Przewidywane na stanie','Zapotrzebowanie netto',
                'Planowane zamówienia','Planowane przyjęcie zamówień','Czas realizacji','Wielkość partii','Na stanie','Ilość w BOM']
lista2_1_2_tyg=['Wartości w tygodniu','Czas realizacji','Wielkość partii','Na stanie','Ilość w BOM']
lista6_1_t=['szczegółowy(wiersz,kolumna)','cały wiersz','cały tydzień']

listatest=['Główny Harmonogram Produkcji','[1]papier','[1]okładka','[2]skóra','wróć do menu']
listatest_1=['edytuj','przelicz','zapisz','odczytaj','zmień tryb edycji','wróć do tabel']