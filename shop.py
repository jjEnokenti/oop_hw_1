from reps.storage_rep import Storage


class Shop(Storage):

    def __init__(self, items: dict, capacity: int = 20, goods_limit: int = 5):
        self._goods_limit = goods_limit
        self._items: dict = items
        self._capacity: int = capacity

    def add(self, title, quantity):
        if self.get_free_space() == 0:
            return False
        if title not in self._items and len(self._items) == self._goods_limit:
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


if __name__ == '__main__':
    st = Shop({'toy': 10, 'raat': 1})

    assert st.get_unique_items_count() == 2
    assert isinstance(st.get_items(), dict)
    assert st.get_free_space() == 9

    assert st.add('car', 5)
    assert st.get_unique_items_count() == 3
    assert st.get_free_space() == 4

    assert st.add('das', 1)
    assert st.get_unique_items_count() == 4
    assert st.get_free_space() == 3

    assert st.add('asd', 3)
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 0

    assert not st.add('addxx', 1)
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 0

    assert st.remove('asd', 3)
    assert st.get_unique_items_count() == 4
    assert st.get_free_space() == 3

