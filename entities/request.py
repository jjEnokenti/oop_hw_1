from exceptions import IncorrectRequest


class Request:

    def __init__(self, request: str):
        self._request = request.lower().split()

        if len(self._request) != 4:
            raise IncorrectRequest

        self.take_from = self._request[2]
        self.to = self._request[3]
        self.amount = int(self._request[1])
        self.product = self._request[0]


if __name__ == '__main__':
    import pytest

    req = Request('печенья 3 склад магазин')
    with pytest.raises(IncorrectRequest):
        incorrect_req = Request('dddd')
