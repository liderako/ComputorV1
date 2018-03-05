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


import sys

def putstr(string):
    sys.stdout.write(string)

class Polynomial:
	a = 0.0
	b = 0.0
	c = 0.0
	def 	__init__(self, argv):
		self.__input_param = argv.split(" ")

	def 	valid(self):
		return -1

	def 	convert(self):
		# s_split = self.__input_s.split(" ")
		res = self.__input_param.valid()
		return (res)

def main():
	putstr("Input: ")
	answer = raw_input()
	argv = answer.upper()
	p = Polynomial(argv)
	res = p.convert()
	if (res == -1):
		print ("Error: syntax error")
		return (1)
main()
