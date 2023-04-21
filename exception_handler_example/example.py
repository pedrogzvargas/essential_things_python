def raise_exception(must_raise):
    if must_raise:
        raise ValueError("value error")


def try_exception(must_raise):
    try:
        raise_exception(must_raise)
    except ValueError:
        print("exception handled")
    else: # Cuando no hay exception
        print("else")
    finally: # Siempre
        print("Always")


if __name__ == '__main__':
    try_exception(True)
