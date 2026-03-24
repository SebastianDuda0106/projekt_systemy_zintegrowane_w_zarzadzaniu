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
