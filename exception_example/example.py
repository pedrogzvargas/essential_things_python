from exception_example.not_animal_exception import NotAnimalException


def add_number_to_my_counter(number):
    if not isinstance(number, int):
        raise ValueError(f"{number} is not instance of int")


def set_animal(animal):
    if animal not in ["perro", "gato"]:
        raise NotAnimalException


if __name__ == '__main__':
    # add_number_to_my_counter("89")
    set_animal("otro")


