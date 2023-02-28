class BaseError(Exception):
    message = {'detail': 'Неизвестная ошибка'}


class NotEnoughSpace(BaseError):
    message = {'detail': 'Нет свободного места на складе'}


class TooManyDifferentProduct(BaseError):
    message = {'detail': 'В магазине нет места для нового товара'}


class ProductNotExistent(BaseError):
    message = {'detail': 'Такого товара нет'}


class OutOfStock(BaseError):
    message = {'detail': 'На складе не хватает товара'}


class IncorrectRequest(BaseError):
    message = {'detail': 'Некорректный запрос'}
