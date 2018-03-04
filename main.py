# class Person:
#     __name = 'NULL'
#     __age = 0
#
#     def __init__(self, name="NULL", age = 0):
#         self.__name = name
#         self.__age = age
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self, age):
#         return self.__age
#
# class Man(Person):
#     __pol = "NULL"
#
#     def __init__(self, pol, name, age):
#         __pol = pol
#         Person.__init__(self)
#         # super(Man, self, name, age).__init__()
#
#     def setPoll(self, pol):
#         self.__pol = pol
#     def getPoll(self):
#         return self.__pol
#
# anton = Man("man", "anton", 10)
import sys

def main(argv):
    x = "anton"
    print len(argv)

main(sys.argv)
