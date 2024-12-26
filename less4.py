class Cars:
    def __init__(self, car, years, price):
        self.__car = car
        self.__years = years
        self.__price = price


    def getter(self):
        return self.__car, self.__years, self.__price

    def setter(self):
        self.__car = 'BMW M5 F90'
        self.__years = 2011
        self.__price = '5700000сом'
        return self.__car, self.__years, self.__price

my_class = Cars('MERSEDES CLS 63 AMG',2011,'3000000сом')
print(my_class.getter())
print(my_class.setter())