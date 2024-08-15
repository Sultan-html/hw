class Appliance: 
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def use(self):
        pass
    def repair(self):
        pass
class WashingMachine(Appliance):
    def use(self):
        print("\nСтиральная машина начала стирку")
    def repair(self):
        print("Ремонт стиральной машины")
class Microwave(Appliance):
    def use(self):
        print("\nМикроволновая печь разогревает еду")
    def repair(self):
        print("емонт микроволновой печи")
class Refrigerator(Appliance):
    def use(self):
        print("""\nХолодильник охлаждает продукты""")
    def repair(self):
        print("Ремонт холодильника\n")

washingmachine = WashingMachine()
washingmachine.use()
washingmachine.repair()  
microwave = Microwave()
microwave.use() 
microwave.repair() 
refrigerator = Refrigerator()
refrigerator.use()  
refrigerator.repair() 

appliance = Appliance()