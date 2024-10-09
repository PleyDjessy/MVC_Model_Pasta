class PastaModel:
    def __init__(self, name: str, ingredients: list, price: float, weight: float, custom_ingredients: list=None):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.weight = weight
        if custom_ingredients is not None:
            self.custom_ingredients = custom_ingredients
        else:
            self.custom_ingredients = []

