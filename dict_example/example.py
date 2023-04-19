# Creacion
lenovo = {"id": "1", "name": "Lenovo", "price": 30000.00, "x": "x"}

# items (Devuelve una lista de los elementos del diccionario. Pares llave, valor)
items = lenovo.items()

# keys (Devuelve una lista con las llaves del diccionario)
keys = lenovo.keys()

# values (Devuelve una lista con los valores del diccionario)
values = lenovo.values()

# get (Devuelve el valor que corresponde a la llave k del diccionario. Si la llave no existe devuelve None)
id_value = lenovo.get("id")
weight_value = lenovo.get("weight")
description_value = lenovo.get("description", "N/A")

# popitem (Elimina el ultimo elemento del diccionario y lo devuelve como resultado)
popitem = lenovo.popitem()

# pop (ELimina un valor con la llave pasada como parametro, y recibe un default)
pop = lenovo.pop("x", "N/E")

del lenovo["id"]

lenovo.update({"id": "1"})

if __name__ == '__main__':
    for items in lenovo.items():
        print(f"llave: {items[0]}, valor: {items[1]}")

    for key in lenovo.keys():
        print(f"llave {key}, valor {lenovo[key]}")

    for value in lenovo.values():
        print(value)
