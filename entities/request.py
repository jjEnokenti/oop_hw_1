class Request:

    def __init__(self, request: str):
        self._request = request.split()
        self.take_from = self._request[2]
        self.to = self._request[3]
        self.amount = int(self._request[1])
        self.product = self._request[0]


if __name__ == '__main__':
    req = Request('печенья 3 склад магазин')
    print(req)
