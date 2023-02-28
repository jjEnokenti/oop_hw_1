from typing import Dict

from entities.reps.abstract_storage import AbstractStorage
from entities.request import Request
from exceptions import ProductNotExistent, OutOfStock


class Courier:

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self._request = request
        self._storages = storages

        if self._request.take_from in self._storages:
            self._take_from = self._storages[self._request.take_from]
            self._shot_take_from = self._take_from

        if self._request.to in self._storages:
            self._to = self._storages[self._request.to]
            self._shot_to = self._to

    def check_product_exist(self):
        if self._request.product not in self._take_from.get_items():
            raise ProductNotExistent

    def check_quantity_product(self):
        if self._request.amount > self._take_from.get_items()[self._request.product]:
            raise OutOfStock

    def move(self):
        self.check_product_exist()
        self.check_quantity_product()

        print('Нужное количество есть на складе')

        self._to.add(self._request.product, self._request.amount)
        print(f'Курьер доставил {self._request.amount} {self._request.product} в {self._request.to}')

        self._take_from.remove(self._request.product, self._request.amount)

    def cancel(self):
        self._take_from = self._shot_take_from
        self._to = self._shot_to
