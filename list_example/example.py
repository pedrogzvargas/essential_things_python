# Creacion
computers = ["Lenovo", "Apple"]

# append (Añade x al final de la lista)
computers.append("Acer")

# insert (Inserta x en el índice i de la lista)
computers.insert(0, 'Sony')

# remove (Elimina la primera ocurrencia de x en la lista)
computers.remove('Lenovo')

# reverse (Invierte la lista)
computers.reverse()

# pop (Elimina el elemento en el índice i y lo devuelve como resultado del método)
value = computers.pop(0)

# extend (Añade todos los elementos de 1 a la lista)
computers.extend(["Toshiba", "Samsung"])

# count (Devuelve la cantidad de veces que x aparece en la lista)
members = computers.count("Samsung")

# index (Devuelve el índice de la primera ocurrencia de x en la lista)
index = computers.index("Samsung")

# Slices
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice_one = numbers_list[0:2]
slice_two = numbers_list[:2]
slice_three = numbers_list[2:]
slice_four = numbers_list[2:8:2]
slice_five = numbers_list[::]
slice_six = numbers_list[::-1]
numbers_list[0:1] = [0, 1]
del numbers_list[0]


def print_list(numbers: list):
    for number in numbers:
        print(number)


if __name__ == '__main__':
    print_list(computers)
