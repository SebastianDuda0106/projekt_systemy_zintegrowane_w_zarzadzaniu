def menu(lista,indents=0,message=0):
    if message == 0:
        message=f'enter number from 1 to {len(lista)}\n'
    max=len(lista)
    user_input='start'
    while not(isinstance(user_input,int) and (user_input in range(0+1,max+1))):
        for i in range(0,max):
            print(f'{i+1}.{lista[i]}')    
        try:
            user_input=int(input(message))
        except:
            print('enter correct input')
    print("entered: ",user_input)
    return user_input

if __name__=="__main__":
    #menu główne
    lista1=['Wyświetl','Edytuj','Zamknij']
    #wyswietlanie
    lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
    lista1_1_2=['[1]papier','[1]okładka','[2]skóra']

    #edytowanie
    lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']

    lista2_1_t=['']#tutaj wpisać listę z numerami tygodni
    
    #listy dla GHP
    lista2_1_1_r=['Przewidywany popyt',
                  'Produkcja',
                  'Dostępne',
                  'Czas realizacji',
                  'Na stanie']

    #listy dla MRP
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

    menu(lista1)