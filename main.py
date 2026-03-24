#Autorzy: Sebastian Duda, Jan Bielecki
from src.product import product
from src.component import component
def main():
    weeks=7

    zeszyt = product(
        name='zeszyt',
        production_time=2,
        stock=20,
        req_amount=[0,0,20,10,50,0,0],
        production_amount=[0,0,0,20,0,60,30],
        weeks=weeks
    )
    print(zeszyt.production_amount)
    papier = component(
        name='papier',
        production_time=2,
        batch_size=200,
        BOM_level=1,
        stock=60,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.production_amount,
        weeks=weeks,
        req_amount=64
    )
    print(zeszyt.production_amount)
    papier.info()
    okladka = component(
        name='okladka',
        production_time=1,
        batch_size=20,
        BOM_level=1,
        stock=5,
        parent_assembly_time=zeszyt.production_time,
        parent_demand=zeszyt.production_amount,
        weeks=weeks
    )
    okladka.info()
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
    skora.info()

if __name__ == "__main__":
    main()
