class SuperCars():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    def run(self):
        print(f"my favorite car is {self.name} produced in {self.year}")
        
        
car1 = SuperCars("BMW X5", 2024)

print(car1.run())