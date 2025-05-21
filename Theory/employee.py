#4: TÍNH KẾ THỪA (INHERITANCE)

class Employee:
    co_salary = 1.04
    def __init__(self, first, last, year, pay):
        self.first = first
        self.last = last
        self.year = year
        self.mail = first + '.' + last + str(year) + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return f"Ten: {self.first} {self.last}"

    def applySalary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay
    
    # representation (Ham nay tra ve str)
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.mail}"

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, year, pay, prog_languages):
        super().__init__(first, last, year, pay)             # Ke thua tu Employee
        self.prog_languages = prog_languages

class Manager(Employee):
    co_salary = 1.5
    def __init__(self, first, last, year, pay, age, employees=None):
        super().__init__(first, last, year, pay)
        if employees == None:
            self.emplist = []
        else:
            self.emplist = employees
        self.age = age
    
    def addEmployees(self, emp):
        if emp not in self.emplist:
            self.emplist.append(emp)
    
    def removeEmployees(self, emp):
        if emp in self.emplist:
            self.emplist.remove(emp)

    def printEmp(self):
        for i in self.emplist:
            print("-->", i.fullname())

    def yearAttachment(self):
        return self.age - 25

class Secretary(Employee):
    co_salary = 1.2
    def __init__(self, first, last, year, pay, purpose):
        super().__init__(first, last, year, pay)
        self.purpose = purpose

if __name__ == '__main__':

    dev1 = Developer("Mai", "Quan", 2005, 200, "python")
    print(dev1.fullname())
    print(dev1.applySalary())


    dev1man = Developer("A", "Mai", 2003, 500, "Python")
    dev2man = Developer("B", "Mai", 2006, 400, "Java")
    sec = Secretary("Nhi", "Ngoc", 2005, 400, "Make a schedule for manager")
    man = Manager("Nguyen", "A", 1999, 400, 40, [dev1man, dev2man])

    print(man.applySalary())
    print(f"Year attachment: {man.yearAttachment()}")
    man.printEmp()

    man.removeEmployees(dev1man)
    man.addEmployees(sec)
    print("After removing dev and adding sec: ")
    man.printEmp()

    # emp = Employee("Mai", "Quan", 1000)
    # print(emp)
    # print(repr(emp))
    # print(str(emp))
    # print(len(emp))
    # print(emp.__len__())