class Item:
    def __init__(self, price, weight):
        self.__price = price
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_price(self):
        return self.__price
