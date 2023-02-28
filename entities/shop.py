from typing import Dict

from entities.reps.base_storage import BaseStorage
from exceptions import TooManyDifferentProduct


class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int = 20, goods_limit: int = 5):
        super().__init__(items, capacity)
        self._goods_limit = goods_limit

    def add(self, title: str, quantity: int):
        if self.get_unique_items_count() >= self._goods_limit:
            raise TooManyDifferentProduct
        super().add(title, quantity)


if __name__ == '__main__':
    import pytest

    st = Shop({'toy': 10, 'backpack': 1})

    assert st.get_unique_items_count() == 2
    assert isinstance(st.get_items(), dict)
    assert st.get_free_space() == 9

    st.add('car', 5)
    assert st.get_unique_items_count() == 3
    assert st.get_free_space() == 4

    st.add('das', 1)
    assert st.get_unique_items_count() == 4
    assert st.get_free_space() == 3

    st.add('asd', 3)
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 0

    with pytest.raises(TooManyDifferentProduct):
        st.add('addxx', 1)
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 0

    st.remove('asd', 3)
    assert st.get_unique_items_count() == 4
    assert st.get_free_space() == 3
