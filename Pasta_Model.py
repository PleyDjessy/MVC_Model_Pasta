class PastaModel:
    def __init__(self, name: str, ingredients: list, price: float, weight: float, custom_ingredients: list = None, image: str = None):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__weight = weight
        if custom_ingredients is not None:
            self.__custom_ingredients = custom_ingredients
        else:
            self.__custom_ingredients = []

        if image is not None:
            self.__image = image
        else:
            self.__image = ""

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

    def get_image(self):
        return self.__image

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

    def set_image(self, data):
        self.__image = data


    def add_custom_ingredients(self):
        self.__ingredients.extend(self.__custom_ingredients)

    def change_data(self, type_of_data, data):
        if type_of_data == "name":
            self.set_name(data)
        elif type_of_data == "ingredients":
            self.set_ingredients(data)
        elif type_of_data == "price":
            self.set_price(data)
        elif type_of_data == "weight":
            self.set_weight(data)
        elif type_of_data == "custom_ingredients":
            self.set_custom_ingredients(data)
        elif type_of_data == "image":
            self.set_image(data)
        else:
            return "Error"
    @staticmethod
    def client_own_pasta(client_ingredients: list, client_weight: float):
        return f"Особая паста по рецептуре клиента: с составом:{client_ingredients} и весом {client_weight}. Цену рассчитайте сами."
