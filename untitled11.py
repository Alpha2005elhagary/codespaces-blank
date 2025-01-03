#violate
# from abc import ABC,abstractmethod
# class motor_and_four_wheels(ABC):
#     @abstractmethod
#     def has_a_motor():
#         pass
#     @abstractmethod
#     def has_four_wheels():
#         pass
# class motor_and_two_wheels(ABC):
#     @abstractmethod
#     def has_a_motor():
#         pass
#     @abstractmethod
#     def has_two_wheels():
#         pass
# class two_wheels_only(ABC):
#     @abstractmethod
#     def has_two_wheels():
#         pass
# class motor_and_three_wheels(ABC):
#     @abstractmethod
#     def has_a_motor():
#         pass
#     @abstractmethod
#     def has_three_wheels():
#         pass
# class car(motor_and_four_wheels):
#     def has_a_motor(self):
#         return "car has a motor"
#     def has_four_wheels(self):
#         return "car has four wheels"
# class vehicle(motor_and_four_wheels):
#     def has_a_motor(self):
#         return "vehicle has a motor"
#     def has_four_wheels(self):
#         return "vehicle has four wheels"
# class toktok(motor_and_three_wheels):
#     def has_a_motor(self):
#         return "toktok has a motor"
#     def has_three_wheels(self):
#         return "toktok has three wheels"
# class motorcycle(motor_and_two_wheels):
#     def has_a_motor(self):
#      return "motorcycle has a motor"
#     def has_two_wheels(self):
#      return "motorcycle has two wheels"
# class bike(two_wheels_only):
#     def has_two_wheels(self):
#         return "bike has two wheels"
# cll=car()
# print(cll.has_a_motor())
# print(cll.has_four_wheels())
# cll2=vehicle()
# print(cll2.has_a_motor())
# print(cll2.has_four_wheels())
# cll3=toktok()
# print(cll3.has_a_motor())
# print(cll3.has_three_wheels())
# cll4=motorcycle()
# print(cll4.has_a_motor())
# print(cll4.has_two_wheels())
# cll5=bike()
# print(cll5.has_two_wheels())
#true
from abc import ABC,abstractmethod
class has_a_motor(ABC):
    @abstractmethod
    def has_a_motor():
        pass
class has_wheels(ABC):
    @abstractmethod
    def has_wheels():
        pass
class car(has_a_motor,has_wheels):
    def has_a_motor(self):
        return "car has a motor"
    def has_wheels(self):
        return "car has four wheels"
class vehicle(has_a_motor,has_wheels):
    def has_a_motor(self):
        return "vehicle has a motor"
    def has_wheels(self):
        return "vehicle has four wheels"
class toktok(has_a_motor,has_wheels):
    def has_a_motor(self):
        return "toktok has a motor"
    def has_wheels(self):
        return "toktok has three wheels"
class motorcycle(has_a_motor,has_wheels):
    def has_a_motor(self):
        return "motorcycle has a motor"
    def has_wheels(self):
        return "motorcycle has two wheels"
class bike(has_wheels):
    def has_wheels(self):
        return "bike has two wheels"
cll=car()
print(cll.has_a_motor())
print(cll.has_wheels())
cll2=vehicle()
print(cll2.has_a_motor())
print(cll2.has_wheels())
cll3=toktok()
print(cll3.has_a_motor())
print(cll3.has_wheels())
cll4=motorcycle()
print(cll4.has_a_motor())
print(cll4.has_wheels())
cll5=bike()
print(cll5.has_wheels())