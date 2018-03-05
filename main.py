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

def 	main_input():
	putstr("Input: ")
	try:
		answer = raw_input()
		return answer
	except:
		print "\nError input"
		sys.exit(0)

class Polynomial:
	a = 0
	b = 0
	c = 0
	countDigital = 0
	countOperator = 0
	countX = 0
	lvlDegree = 0
	def 	__init__(self, argv):
		self.inputParam = argv.split(" ")

	def 	valid(self):
		print self.inputParam ### need delete
		print "Len ", len(self.inputParam) ### need delete
		for c in self.inputParam:
			# print "test ", len(c)
			size = len(c)
			if ((c.isdigit()) == 1):
				self.countDigital += 1
			elif ((c.isalpha()) == 1):
				print "Error: syntax error in ", c
				sys.exit(1)
			elif (('X^1' in c) or ('X^0' in c) or ('X^2' in c)):
				self.countX += 1
			elif (size == 3 and 'X^' in c and (c[2] != '0' or c[2] != '1' or c[2] != '2')):
				print "Error: Level degree too big", c
				sys.exit(1)
			elif (size != 1):
				print "Error: syntax error in ", c
				sys.exit(1)

		print "Count Digital", self.countDigital ## need delete
		print "Count X ", self.countX ## need delete
		return -1

	def 	convert(self):
		res = self.valid()
		return (res)

def main():
	answer = main_input()
	argv = answer.upper()
	p = Polynomial(argv)
	res = p.convert()
	if (res == -1):
		print ("Error: syntax error")
		return (1)
main()
