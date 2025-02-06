# https://www.youtube.com/playlist?list=PLFyAEmibWSQCCoJmW0hpBMSlM8NMoMtWg

#1: CLASS, INSTANCE, CONSTRUCTOR
class car():
    def __init__(self, xuatxu, year):     # constructor
        self.xuat_xu = xuatxu
        self.nam = year

    def sanxuat(self, x):
        return x * 2

bmw = car("USA", 2020)                    # instance
bmw.xuatxu = "Germany"
bmw.year = 1969
print(bmw.year)

vinfast = car("VN", 2018)
vinfast.year = 2018
print(vinfast.sanxuat("Vietnam"))

print(type(bmw), type(vinfast))



#2: CLASS VARIABLES
class Car():
    tax = 1   # Thuế
    car_number = 0
    def __init__(self, brand, model, found_year, price):
        self.brand = brand
        self.model = model
        self.found_year = found_year
        self.price = price
        self.car_number += 1            # instance variables
        # Car.car_number += 1             # class variables

    def brandFunction(self):
        return self.brand
    def getValue(self):
        return int(self.price * self.tax)


    # regular method              #3 CLASS METHOD
    @classmethod
    def setTax(cls):
        cls.tax = 1.5

    @classmethod
    def carStr(cls, car_str):
        brand, model, found_year, price = car_str.split('-')
        found_year = int(found_year)
        price = int(price)
        return cls(brand, model, found_year, price)
    
    @staticmethod
    def checkPrice(price):
        if price <= 1000:
            return "This is a chip car"
        else:
            return "This is a expensive car"

# print(Car.car_number)       # output 0

car1 = Car("Vinfast", "LuxA", "2017", 1000)
car2 = Car("BMW", "new", 2000, 700)

# print(Car.car_number)       # output 2
print(car1.car_number, car2.car_number)         # ouput 1 1

Car.tax = 1 # Biến tax trong Class CarCar
car2.tax = 2 # Biến tax dùng cho instance 2
print(Car.tax, car1.tax, car2.tax)

print(car1.getValue())
print(car2.getValue())

print(Car.__dict__)   # Xem thuộc tính



#3 CLASS METHOD AND STATIC METHOD
car1.setTax()
print(Car.tax)
print(car2.getValue())

car_temp = "Toyota-Camry-1900-2014"
car3 = Car.carStr(car_temp)

print(car1.checkPrice(car1.price))
print(car3.checkPrice(car3.price))
print(Car.checkPrice(car1.price))