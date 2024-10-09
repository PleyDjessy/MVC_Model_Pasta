from Pasta_Model import PastaModel
from Pasta_Controller import PastaController

spaghetti = PastaModel("spaghetti", ["pasta", "tomatoes", "chicken", "souse", "green"], 200.0, 1.0, ["more_green!!!"])
c_spaghetti = PastaController(spaghetti)

print(spaghetti.get_ingredients())

spaghetti.add_custom_ingredients()
print(spaghetti.get_ingredients())

print(spaghetti.client_own_pasta(["pasta","MANY MANY GREEEEEEEN!!!"], 5.0), "\n")


print(c_spaghetti.get_data())
print(c_spaghetti.change_data("user", "name", "SEfsfwewfsffF"))
c_spaghetti.change_data("admin", "weight", 1.4)
print(c_spaghetti.get_data())

print(c_spaghetti.client_own_pasta("customer", ["entire chicken filled with pasta inside", "some green outside"], 7.999))