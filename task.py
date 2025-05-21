

class Machine:
    def __init__(self, productivity, cost, part_price):
        self.productivity = productivity
        self.cost = cost
        self.part_price = part_price

    def payback_units(self):
        number = self.cost / self.part_price
        return number
    
    def time(self):
        # Time to produce 1 part
        time_per = 1 / self.productivity
        time = self.payback_units() * time_per
        return time
    def __str__(self):
        return f"Machine: Productivity = {self.productivity}, Cost = {self.cost}, Part_price = {self.part_price}"
    
    def __add__(self, other):
        new_productivity = self.productivity + other.productivity
        new_cost = self.cost + other.cost
        new_price = (self.part_price + other.part_price) / 2
        return Machine(new_productivity, new_cost, new_price)
    

class Machine_CNC(Machine):
    def __init__(self, productivity, cost, part_price, specifications):
        super().__init__(productivity, cost, part_price)
        self.specifications = specifications

    def __str__(self):
        return f"CNC Machine: Productivity = {self.productivity}, Cost = {self.cost}, Part_price = {self.part_price}"


class Milling_machine(Machine):
    def __init__(self, productivity, cost, part_price, specifications):
        super().__init__(productivity, cost, part_price)
        self.specifications = specifications

    def __str__(self):
        return f"Milling Machine: Productivity = {self.productivity}, Cost = {self.cost}, Part_price = {self.part_price}"
    


if __name__ == '__main__':
    
    general_machine = Machine(2, 1000, 20)
    mil_machine = Milling_machine(3, 500, 10, 5)
    cnc_machine = Machine_CNC(5, 1500, 10, 2)
    combined_machine =  mil_machine + cnc_machine

    print(general_machine)
    print(f"   -Number of products that we need to produce for payback (general machine): {general_machine.payback_units()}")
    print(f"   -Payback time at a fixed price of a part (general machine): {general_machine.time()}")

    print(cnc_machine)
    print(f"   -Number of products that we need to produce for payback (general machine): {cnc_machine.payback_units()}")
    print(f"   -Payback time at a fixed price of a part (general machine): {cnc_machine.time()}")

    print(mil_machine)
    print(f"   -Number of products that we need to produce for payback (general machine): {mil_machine.payback_units()}")
    print(f"   -Payback time at a fixed price of a part (general machine): {mil_machine.time()}")    
    
    print(combined_machine)
    print(f"   -Number of products that we need to produce for payback (general machine): {combined_machine.payback_units()}")
    print(f"   -Payback time at a fixed price of a part (general machine): {combined_machine.time()}") 
