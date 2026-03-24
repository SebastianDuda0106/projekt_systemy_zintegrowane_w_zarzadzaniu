#Autorzy: Sebastian Duda, Jan Bielecki
from src.product import product
from src.component import component
def main():
    weeks=7

    zeszyt = product(
        production_time=1,
        stock=20,
        req_amount=[0,0,20,10,50,0,0],
        production_amount=[0,0,20,0,0,30,0],
        weeks=weeks
    )
    zeszyt.info()
    noga = component(
        production_time=2,
        batch_size=50,
        BOM_level=1,
        stock=50,
        parent_assembly_time=zeszyt.getProductionTime(),
        parent_demand=zeszyt.getProduction(),
        weeks=weeks

    )
    noga.info()

def hello(name):
    print(f'Hello {name}!')

if __name__ == "__main__":
    main()
