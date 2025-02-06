#4: TÍNH KẾ THỪA (INHERITANCE)

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

# Khi sử dụng tính kế thừa trong OOP, lớp con sẽ kế thừa tất cả các thuộc tính và phương thức của lớp cha
class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, pay, prog_languages):
        super().__init__(first, last, pay)             # Ke thua tu Employee
        self.prog_languages = prog_languages

class Manager(Employee):
    co_salary = 1.5
    def __init__(self, first, last, pay, age, employees=None):
        super().__init__(first, last, pay)
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
    def __init__(self, first, last, pay, purpose):
        super().__init__(first, last, pay)
        self.purpose = purpose

dev1 = Developer("Mai", "Quan", 200, "python")
print(dev1.fullname())
print(dev1.applySalary())


dev1man = Developer("A", "Mai", 500, "Python")
dev2man = Developer("B", "Mai", 400, "Java")
sec = Secretary("Nhi", "Ngoc", 400, "Make a schedule for manager")
man = Manager("Nguyen", "A", 400, 40, [dev1man, dev2man])

print(man.applySalary())
print("Year attachment: ", man.yearAttachment())
man.printEmp()

man.removeEmployees(dev1man)
man.addEmployees(sec)
print("After removing dev and adding sec: ")
man.printEmp()