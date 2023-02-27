from reps.storage_rep import Storage


class Store(Storage):

    def __init__(self, items: dict, capacity: int = 100):
        self._items: dict = items
        self._capacity: int = capacity - sum(self._items.values())

    def add(self, title, quantity):
        if self._capacity == 0:
            return False
        if not self._capacity - quantity > 0:
            quantity = self._capacity

        self._capacity -= quantity
        self._items[title] = self._items.get(title, 0) + quantity
        return True

    def remove(self, title, quantity):
        if quantity <= 0:
            return False
        current_quantity = self._items[title]
        if quantity > current_quantity:
            quantity = current_quantity
        self._items[title] -= quantity
        self._capacity += quantity
        return True

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)


if __name__ == '__main__':
    st = Store({'toy': 89, 'raat': 1})

    assert st.get_unique_items_count() == 2
    assert isinstance(st.get_items(), dict)
    assert st.get_free_space() == 10

    assert st.add('car', 5)
    assert st.get_unique_items_count() == 3
    assert st.get_free_space() == 5

    assert st.add('das', 1)
    assert st.get_unique_items_count() == 4
    assert st.get_free_space() == 4

    assert st.add('asd', 3)
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 1

    assert st.add('addxx', 1)
    assert st.get_unique_items_count() == 6
    assert st.get_free_space() == 0

    assert not st.add('addxx', 4)
    assert st.get_unique_items_count() == 6
    assert st.get_free_space() == 0

    assert st.remove('asd', 3)
    assert st.get_unique_items_count() == 6
    assert st.get_free_space() == 3

