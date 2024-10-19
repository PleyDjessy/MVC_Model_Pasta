from Pasta_Model import PastaModel
from Pasta_Controller import PastaController
from Pasta_View import PastaView
import time

spaghetti = PastaModel("spaghetti", ["pasta", "tomatoes", "chicken", "souse", "green"], 200.0, 1.0, ["more_green!!!"], "Pasta.jpg")
c_spaghetti = PastaController(spaghetti)
show_me_that_tasty_spaghetti = PastaView(c_spaghetti)

"""Ниже указана часть для удобной проверки написанного кода"""
#print(spaghetti.get_ingredients())

#spaghetti.add_custom_ingredients()
#print(spaghetti.get_ingredients())

#print(spaghetti.client_own_pasta(["pasta","MANY MANY GREEEEEEEN!!!"], 5.0))


#print(c_spaghetti.get_data())
#print(c_spaghetti.change_data("user", "name", "SEfsfwewfsffF"))
#c_spaghetti.change_data("admin", "weight", 1.4)
#print(c_spaghetti.get_data())

#print(c_spaghetti.client_own_pasta("customer", ["entire chicken filled with pasta inside", "some green outside"], 7.999))

if __name__ == "__main__":

    show_me_that_tasty_spaghetti.print_data()

    print(show_me_that_tasty_spaghetti.change_data("customer", "price", 0))
    print(show_me_that_tasty_spaghetti.change_data("admin", "name", "Bolognese pasta"))
    show_me_that_tasty_spaghetti.print_menu()

    show_me_that_tasty_spaghetti.client_own_pasta("admin", ["tomatoes", "tomato_pasta", "green from tomatoes", "dried tomato roots"], 2.1)

    json_file = f"{round(time.time(), 2)}_Bolognese pasta.json"
    show_me_that_tasty_spaghetti.save_order_to_json("Bolognese pasta")
    show_me_that_tasty_spaghetti.get_data_from_json(json_file, "admin")
