import sys

# def putstr(string):
#     sys.stdout.write(string)

# def 	main_input():
# 	putstr("Input: ")
# 	try:
# 		answer = raw_input()
# 		return answer
# 	except:
# 		print "\nError input"
# 		sys.exit(0)
def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
		return False
    return True


class Polynomial:
	a = 0
	b = 0
	c = 0
	countDigital = 0
	countOperator = 0
	countOperatorRavno = 0
	countX = 0
	lvlDegree = 0

	def 	__init__(self, argv):
		self.inputParam = argv.split(" ")

	def 	CheckInputParam(self):
		for c in self.inputParam:
			size = len(c)
			# print "size ", size
			if ((isfloat(c)) == True):
				self.countDigital += 1
			# elif (size > 1 and c[0] == '-'):
				# self.checkDigitalNegativ(size, c)
			elif ((c.isalpha()) == 1):
				print "Error: syntax error in ", c
				sys.exit(1)
			elif (size == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
				self.countX += 1
			elif (size == 1 and c[0] == '='):
				self.countOperatorRavno += 1
			elif (size == 1 and (c[0] == '*' or c[0] == '+' or c[0] == '-')):
				self.countOperator += 1
			elif (size >= 3 and 'X^' in c):
				print "Error: Level degree too big or invalid", c
				sys.exit(1)
			elif (size > 1):
				print "Error: syntax error in ", c
				sys.exit(1)

	def 	valid(self):
		print self.inputParam ### need delete
		print "Len ", len(self.inputParam) ### need delete

		self.CheckInputParam()

		print "Count Digital", self.countDigital ## need delete
		print "Count X ", self.countX ## need delete

		self.checkRes()
		return -1

	def 	checkRes(self):
		if (self.countDigital != self.countX):
			print "Error: math error, Count digital != count X^[0-2]"
			sys.exit(1)
		elif self.countOperatorRavno != 1:
			print "Error: math error, syntax error with \'=\'"
			sys.exit(1)
		elif self.countOperator != self.countDigital:
			print "Error: math error with countMathOperator"
			sys.exit(1)

	def 	convert(self):
		res = self.valid()
		return (res)

def main(argc, argv):
	# answer = main_input()
	if (argc != 2):
		print "Error: size argc != 2"
		sys.exit(1) # need found exit
	answer = argv[1]
	argv = answer.upper()
	p = Polynomial(argv)
	res = p.convert()
	print "OK"
	return (1)
main(len(sys.argv), sys.argv)
