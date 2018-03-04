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

class Polynomial:
	a = 0.0
	b = 0.0
	c = 0.0
	def 	__init__(self, argv):
		self.__input_s = argv

	def 	valid(self, string):
		return "NULL"
	def 	convert(self):
		s_split = self.__input_s.split(" ")
		print "test ",s_split
		res = self.valid(s_split)
		return (res)
		# print ()
def main(argc, argv):
	if (argc != 2):
		print "Error: size argc != 2"
		return (-1) # need found exit
	p = Polynomial(argv[1])
	p.convert()
main(len(sys.argv), sys.argv)
