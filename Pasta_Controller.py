class PastaController:
    def __init__(self,model):
        self.__model = model

    def get_data(self):
        return [f"Название: {self.__model.get_name()}", f"Ингредиенты: {self.__model.get_ingredients()}", f"Цена: {self.__model.get_price()}", f"Вес: {self.__model.get_weight()}"]

    def change_data(self, user_rights, type_of_data, data):
        if user_rights == "admin":
            self.__model.change_data(type_of_data, data)
            return "Успешно"
        else:
            return "Ошибка: нет доступа"

    def add_custom_ingredients(self, user_rights):
        if user_rights == "admin":
            self.__model.add_custom_ingredients()
        else:
            return "Ошибка: нет доступа"

    def client_own_pasta(self, user_rights, client_ingredients: list, client_weight: float):
        if user_rights in ("admin", "customer"):
            return self.__model.client_own_pasta(client_ingredients, client_weight)
        else:
            return "Ошибка: нет доступа"

