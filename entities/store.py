from entities.reps.base_storage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)


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
    assert st.get_unique_items_count() == 5
    assert st.get_free_space() == 3
