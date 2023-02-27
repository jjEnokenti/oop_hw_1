from reps.base_storage import BaseStorage


class Shop(BaseStorage):

    def __init__(self, items: dict, capacity: int = 20, goods_limit: int = 5):
        super().__init__(items, capacity)
        self._goods_limit = goods_limit

    def add(self, title, quantity):
        if self.get_unique_items_count() >= self._goods_limit:
            return False
        return super().add(title, quantity)


if __name__ == '__main__':
    st = Shop({'toy': 10, 'backpack': 1})

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
