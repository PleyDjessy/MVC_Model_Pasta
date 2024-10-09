class PastaModel:
    def __init__(self, name: str, ingredients: list, price: float, weight: float, custom_ingredients: list=None):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__weight = weight
        if custom_ingredients is not None:
            self.__custom_ingredients = custom_ingredients
        else:
            self.__custom_ingredients = []

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_custom_ingredients(self):
        return self.__custom_ingredients

    def set_name(self, data):
        self.__name = data

    def set_ingredients(self, data):
        if type(data) is list:
            self.__ingredients.clear()
            self.__ingredients.extend(data)
        else:
            return "Error"

    def set_price(self, data):
        self.__price = data

    def set_weight(self, data):
        self.__weight = data

    def set_custom_ingredients(self, data):
        if type(data) is list:
            self.__custom_ingredients.clear()
            self.__custom_ingredients.extend(data)
        else:
            return "Error"
