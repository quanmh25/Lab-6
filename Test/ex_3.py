#5: CÁC METHOD ĐẶC BIỆT TRONG CLASS (SPECIAL METHODS)

class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return f"Ten {self.first} {self.last}"

    def applySalary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay

    # representation (Ham nay tra ve str)
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.mail}"

emp = Employee("Mai", "Quan", 1000)
print(emp)      # Nếu để như vậy thì chỉ in ra mỗi tên và mail, vì class chỉ ưu tiên lấy __str__

print(repr(emp))
print(str(emp))


# Example to understand __repr__ and __str__
print()
import datetime
today = datetime.datetime.now()
print(str(today))           # print readable format for datetime object
print(repr(today))          # print the official format of datetime object
