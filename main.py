from entities.courier import Courier
from entities.store import Store
from entities.shop import Shop
from entities.request import Request
from exceptions import IncorrectRequest, BaseError

store_1 = Store(
    items={
        'мишка': 40,
        'машинка': 5,
        'футболка': 15,
        'кольцо': 10
    }
)

shop_1 = Shop(
    items={
        'мишка': 7,
        'машинка': 1,
        'футболка': 2
    }
)

storages = {
    'склад': store_1,
    'магазин': shop_1
}


def main():
    print('Добро пожаловать!')

    while True:
        for name, store in storages.items():
            print(f'Доступные товары ({name}):',
                  *[f'{item} - {quantity}'
                    for item, quantity in store.get_items().items()],
                  sep='\n')

        try:
            user_request = input(
                'Если вы желаете остановить программу введите "stop/стоп"\n'
                'Введите свой запрос в соответствии с данным форматом\n'
                '"<Наименование товара> <количество> <названия склада> <название магазина>"\n>>>'
            )
        except BaseError as exc:
            print(exc.message)
            continue

        if user_request in ('stop', 'стоп'):
            print('Всего доброго!')
            break

        try:
            request = Request(request=user_request)
        except IncorrectRequest as exc:
            print(exc.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as exc:
            print(exc.message)
            courier.cancel()


if __name__ == '__main__':
    main()
