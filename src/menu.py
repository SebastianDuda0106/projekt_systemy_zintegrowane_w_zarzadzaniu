def menu(lista,message=0):
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
    return user_input
def menup(lista,message=0):
    if message == 0:
        message=f'enter number from 1 to {len(lista)}\n'
    max=len(lista)
    user_input='start'
    while not(isinstance(user_input,int) and (user_input in range(0+1,max+1))):   
        try:
            user_input=int(input(message))
        except:
            print('enter correct input')
    print("entered: ",user_input)
    return user_input

lista1=['Wyświetl','Edytuj','Przelicz','Zamknij']
lista1_1=['Wszystko','Główny Harmonogram Produkcji','Rekordy MRP']
lista1_1_2=['[1]papier','[1]okładka','[2]skóra']
lista2_1=['Główny Harmonogram Produkcji','Rekordy MRP']
lista2_1_1_r=['Przewidywany popyt','Produkcja','Dostępne','Czas realizacji','Na stanie']
lista2_1_2=['[1]papier','[1]okładka','[2]skóra']
lista2_1_2_r=['Całkowite zapotrzebowanie','Planowane przyjęcia','Przewidywane na stanie','Zapotrzebowanie netto',
                'Planowane zamówienia','Planowane przyjęcie zamówień','Czas realizacji','Wielkość parii','Na stanie','Ilość w BOM']
lista2_1_2_tyg=['Wartości w tygodniu','Czas realizacji','Wielkość parii','Na stanie','Ilość w BOM']