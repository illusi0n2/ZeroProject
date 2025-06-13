class Store():
    def __init__(self, name, adress, items = {}):
        self._name = name
        self._adress = adress
        self._items = items

    def add_item(self, item, price):
        self._items[item] = price

    def remove_item(self, item):
        try:
            del self._items[item]
        except KeyError:
            print('Такого товара нет в магазине')

    def check_price(self, item):
        try:
            return self._items[item]
        except KeyError:
            return None

    def update_price(self, item, price):
        try:
            self._items[item] = price
        except KeyError:
            print('Такого товара нет в магазине')

store1 = Store('Магазин 1', 'ул. Пушкина, 1', {'Яблоко': 5.5, 'Банан': 5.4, 'Апельсин': 6})
store2 = Store('Магазин 2', 'ул. Ленина, 2', {'Кокос': 10.1, 'Ананас': 11.4, 'Киви': 7})
store3 = Store('Магазин 3', 'ул. Гагарина, 3', {'Груша': 9.2, 'Персик': 15.5, 'Слива': 7.3})

store1.add_item('Груша', 8.8)
store1.remove_item('Банан')
store1.remove_item('Дыня')
store1.update_price('Яблоко', 5.2)
print(store1.check_price('Яблоко'))

