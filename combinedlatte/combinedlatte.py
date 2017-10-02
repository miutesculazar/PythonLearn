from coffee.coffee import Coffee
from cafelatte.cafelatte import Cafelatte


if __name__ == "__main__":
    cafea_simpla = Coffee(2, 10, 100)
    cafea_latte = Cafelatte(2, 10, 100, 15)

    print('Cantitatea de cafea simpla: ', cafea_simpla.prepare_coffee())
    cafea_simpla.prepare_time_coffee()

    print('Cantitatea de cafea latte: ', cafea_latte.prepare_coffee())
    energia = cafea_latte.energy()
    print('Energia din cafea latte este: ', energia)
    cafea_latte.prepare_time_coffee()
