class SuperCars():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    def run(self):
        print(f"my favorite car is {self.name} produced in {self.year}")
        
        
car1 = SuperCars("BMW X5", 2024)
car2 = SuperCars("BMW X6",2025)

car1.run()
car2.run()
print(car1.name,car1.year)
print(car2.name,car2.year)