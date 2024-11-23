name=input("Enter the name:")
formula=input("Enter the formula:")
usageoftheliquid=input("Enter the usage:")
class liquid:
    def __init__(self,name,formula):
        self.name=name
        self.formula=formula
    def info(self):
        print(self.name)
        print(self.formula)
    def property(self):
        print(usageoftheliquid)
class water(liquid):
    def __init__(self, name, formula):
        super().__init__(name, formula)
    def info(self):
        print(f"self.name={"water"}")
        print(f"self.formula={"H2O"}")
    def property(self):
        print(f"usageoftheliquid={"is to drink"}")
liq=liquid(name, formula)
liq.info()
liq.property()
liq1=water(name, formula)
liq1.info()
liq1.property()
print(liq)