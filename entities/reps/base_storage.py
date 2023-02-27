from entities.reps.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):

    def __init__(self, items: dict, capacity: int):
        self._items: dict = items
        self._capacity: int = capacity

    def add(self, title, quantity):
        if self.get_free_space() == 0:
            return False
        if not self.get_free_space() - quantity > 0:
            quantity = self.get_free_space()

        self._items[title] = self._items.get(title, 0) + quantity
        return True

    def remove(self, title, quantity):
        if quantity <= 0:
            return False
        current_quantity = self._items[title]
        if quantity > current_quantity:
            quantity = current_quantity

        self._items[title] -= quantity
        if self._items[title] == 0:
            self._items.pop(title)
        return True

    def get_free_space(self):
        curr_space = 0
        for quantity in self._items.values():
            curr_space += quantity
        return self._capacity - curr_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
