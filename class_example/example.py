class LenovoComputer:
    """
    LenovoComputer
    """

    BRAND = "Lenovo"
    resolution = ""
    processor = ""
    __price = 0

    def __init__(self, resolution, processor, price):
        self.resolution = resolution
        self.processor = processor
        self.__price = price

    def get_brand(self):
        return self.BRAND

    def get_screen_resolution(self):
        return self.resolution

    def get_processor(self):
        return self.processor

    def get_price(self):
        return self.__price


if __name__ == '__main__':
    lenovo_computer = LenovoComputer(resolution="1360 X 1080", processor="Intel Core i7", price=10_500)
    print(lenovo_computer.get_brand())
    print(lenovo_computer.get_screen_resolution())
    print(lenovo_computer.get_processor())
    print(lenovo_computer.get_price())
