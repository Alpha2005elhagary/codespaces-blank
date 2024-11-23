first_number=int(input("Enter a number ="))
second_number=int(input("Enter a number ="))
class calculation_1:
    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number
    def sum(self):
        return self.first_number+self.second_number
class calculation_2:
    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number
    def multiplication(self):
       return self.first_number*self.second_number
class calculation_3:
    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number
    def div(self):
        if self.second_number ==0:
            return "Zero division error"
        else:
            return self.first_number/self.second_number
class all_calulations(calculation_1,calculation_2,calculation_3):
    def __init__(self, first_number, second_number):
        super().__init__(first_number,second_number)
    def display(self):
        print(calculation_1.sum(self))
        print(calculation_2.multiplication(self))
        print(calculation_3.div(self))
cal=all_calulations(first_number, second_number)
cal.display()
print(cal)