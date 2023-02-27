from store import Store
from shop import Shop
from request_entity import Request


def main():
    print('Добро пожаловать!')

    store_1 = Store(
        items={
            'toy': 40,
            'car': 5,
            'shirt': 15,
            'ring': 10
        }
    )

    shop_1 = Shop(
        items={
            'toy': 7,
            'car': 1,
            'shirt': 2
        }
    )

    while True:
        try:
            print(
                'Доступные товары на складе:',
                *[
                    f'{item} {quantity}'
                    for item, quantity in store_1.get_items().items()
                ],
                sep='\n'
            )
            user_request = input(
                'Введите свой запрос в соответствии с данным шаблоном\n'
                '"<Наименование товара> <количество> <названия склада> <название магазина>"\n>>>'
            )
        except Exception:
            print('Некорректный запрос, попробуйте еще раз')
            continue
        else:
            request = Request(request=user_request)
            product = request.product
            amount = request.amount
            to = request.to
            take_from = request.take_from

            if product not in store_1.get_items():
                print('Такой товар отсутствует на складе, попробуйте заказать другой')
                continue
            if amount > store_1.get_items()[product]:
                print('Не хватает на складе, попробуйте заказать меньше')
                continue
            if not shop_1.add(title=product, quantity=amount):
                print('В магазин недостаточно места, попробуйте что то другое')
                continue

            print('Нужное количество есть на складе')
            print(f'Курьер забрал {amount} {product} со {take_from}')
            print(f'Курьер везет {amount} {product} со {take_from} в {to}')
            print(f'Курьер доставил {amount} {product} в {to}')

            store_1.remove(title=product, quantity=amount)
            store_items = [f'{item} {count}' for item, count in store_1.get_items().items()]
            shop_items = [f'{item} {count}' for item, count in shop_1.get_items().items()]

            print(f'На складе хранится:', *store_items, sep='\n')
            print(f'В магазине хранится:', *shop_items, sep='\n')

            print('Если вы желаете остановить программу введите "stop/стоп"')


if __name__ == '__main__':
    main()
