#Autorzy: Sebastian Duda, Jan Bielecki
from src.product import product
from src.component import component
def main():
    #print("Hello from projekt-systemy-zintegrowane-w-zarzadzaniu!")
    #hello(str(input("what is your name?\n")))
    #x= tabela('acocieto')
    #for row in x.table:
    #    print(row)

    zeszyt = product(
        production_time=1,
        stock=20,
        req_amount=[0,0,20,10,50,0,0],
        weeks=7
    )
    zeszyt.info()
    
    #noga = component(1,1,1,1,6,4)
    #noga.info()

def hello(name):
    print(f'Hello {name}!')

if __name__ == "__main__":
    main()
