# https://www.youtube.com/playlist?list=PLFyAEmibWSQCCoJmW0hpBMSlM8NMoMtWg

class Car():
    tax = 1   # Thuế
    car_number = 0
    def __init__(self, brand, model, found_year, price):
        self.brand = brand
        self.model = model
        self.found_year = found_year
        self.price = price
        self.car_number += 1          
        #Car.car_number += 1             
    
    #regular method
    def brandFunction(self):
        return self.brand
    
    def getValue(self):
        return int(self.price * self.tax)

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

    @property
    def fullname(self):
        return f"{self.brand} {self.model}" 
    
    @fullname.setter
    def fullname(self, namestr):
        brand, model = namestr.split(' ')
        self.brand = brand
        self.model = model

    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None
        print(f"Deleted fullname!")

if __name__ == '__main__':
    # print(Car.car_number)       # output 0
    vin = Car("Vinfast", "LuxA", "2017", 1000)
    bmw = Car("BMW", "new", 2000, 700)
    print(Car.car_number, vin.car_number, bmw.car_number)         # ouput 0 1 1

    bmw.tax = 2 # Biến tax dùng cho instance 2

    print(f"Price of {vin.brand} and {bmw.brand} are {vin.getValue()} and {bmw.getValue()}")
    tmp = "Toyota-Camry-1900-2014"
    car = Car.carStr(tmp)
    print(car.brand)
    print(Car.__dict__)   # Xem thuộc tính

    car = Car("Mercedes", "MQH", 2005, 50005000)
    print(car.fullname)

    car.fullname = "Rollroyces i20"
    print(f"{car.brand}-{car.model}")

    del car.fullname
    print(car.brand, car.model)