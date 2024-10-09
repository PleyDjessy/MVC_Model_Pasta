from Pasta_Model import PastaModel

spaghetti = PastaModel("spaghetti", ["makarons", "tomatoes", "chicken", "souse", "green"], 200.0, 1.0, ["more_green!!!"])

print(spaghetti.get_ingredients())

spaghetti.add_custom_ingredients()
print(spaghetti.get_ingredients())

print(spaghetti.client_own_pasta(["makarons","MANY MANY GREEEEEEEN!!!"], 5.0))