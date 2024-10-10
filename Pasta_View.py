import webbrowser
import os

class PastaView:

    def __init__(self, controller):
        self.__controller = controller

    def print_data(self):
        print(*self.__controller.get_data(), sep=", ")
        if self.__controller.get_image() != "":
            image = os.path.abspath(self.__controller.get_image())
            os.startfile(image)

    def print_menu(self):
        print(*self.__controller.get_data(), sep="\n")
        if self.__controller.get_image() != "":
            image = os.path.abspath(self.__controller.get_image())
            os.startfile(image)

    def change_data(self, user_rights, type_of_data, data):
        if user_rights == "admin":
            self.__controller.change_data(user_rights, type_of_data, data)
            return "Успешно"
        else:
            return "Ошибка: нет доступа"

    def add_custom_ingredients(self, user_rights):
        if user_rights == "admin":
            self.__controller.add_custom_ingredients(user_rights)
        else:
            return "Ошибка: нет доступа"

    def client_own_pasta(self, user_rights, client_ingredients: list, client_weight: float):
        if user_rights in ("admin", "customer"):
            print(self.__controller.client_own_pasta(user_rights, client_ingredients, client_weight))
        else:
            return "Ошибка: нет доступа"


