def addition(number_one, number_two):
    return number_one + number_two


def complex_addition(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


if __name__ == '__main__':
    values_as_dict = {
        "number_one": 10,
        "number_two": 10,
    }
    values_as_list = [1, 2, 3, 4, 5]
    addition = addition(**values_as_dict)
    sum = complex_addition(*values_as_list)
    print(addition)
    print(sum)
