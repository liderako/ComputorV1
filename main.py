import sys
from module import *

class Polynomial:
    a = 0
    b = 0
    c = 0
    countDigital = 0
    countOperator = 0
    countOperatorRavno = 0
    countOperatorX = 0
    countX = 0
    lvlDegree = 0

    def     __init__(self, argv):
        self.inputParam = argv.split(" ")

    def     convert(self):
        self.valid()
        string = self.join()
        partOne = self.parsString(string[0])
        partTwo = self.parsString(string[1])
        self.reducePartOne(partOne)
        
        print "a ", self.a # need delete
        print "b ", self.b # need delete
        print "c ", self.c # need delete

    def     valid(self):
        self.CheckInputParam()
        self.checkRes()

    def     CheckInputParam(self):
        old = '0' 
        for c in self.inputParam:
            size = len(c)
            if ((isfloat(c)) == True):
                if (old != '0' and old != 'o' and old != '='):
                    Error("Error: syntax error with before digital ", + c)
                tmp  = float(c)
                if (old == 'o' and tmp < 0):
                    Error("Error: math error with operator -")
                self.countDigital += 1
                old = 'd'
            elif ((c.isalpha()) == 1):
                Error("Error: syntax error in ", c)
            elif (size == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
                if (old != '*'):
                    Error("Error: math error operator " + c)
                old = 'x'
                self.countX += 1
            elif (size == 1 and c[0] == '='):
                if (old != 'x'):
                    Error("Error: math error \'=\' ")
                old = '='
                self.countOperatorRavno += 1
            elif (size == 1 and ( c[0] == '*' or c[0] == '+' or c[0] == '-')):
                if (old == 'x' and c[0] != '*'):
                    old = 'o'
                elif (old == 'd' and c[0] != '*'):
                    Error("Error: math error with * in " + c)
                elif (old == 'd' and c[0] == '*'):
                    self.countOperatorX += 1
                    old = '*'
                else:
                    Error("Error: math error with operator")
            elif (size >= 3 and 'X^' in c):
                Error("Error: Level degree too big or invalid " + c)
            elif (size > 1):
                Error("Error: syntax error in " + c)
        if (old != 'x'):
            Error("Error: syntax error in end")

    def     checkRes(self):
        if (self.countDigital != self.countX):\
            Error("Error: math error, Count digital != count X^[0-2]")
        elif self.countOperatorRavno != 1:
            Error("Error: math error, syntax error with \'=\'")
        elif (self.countDigital != self.countOperatorX):
            Error("Error: math error, count digital != count operator * and Count X^[0-2]")
    
    def     join(self):
        string = ""
        for c in self.inputParam:
                string = string + " " + c
        return string.split("=")
    
    def     parsString(self, string):
        res = string.strip()
        res = res.split(" ")
        return res

    def     reducePartOne(self, partOne):
        size = len(partOne)

    # def     reducePartOne(self, partOne):
    #     size = len(partOne)
        # digital = 0
        # operator = '0'
        # old = '0'
        # i = 0
        # for c in partOne:
        #     c_len = len(c)
        #     if ((isfloat(c)) == True):
        #         digital = float(c)
        #         tmp = partOne[i + 2]
        #         lvl = tmp[2]
        #         old = 'digital'
        #         if ((operator == '0')):
        #             self.doop(digital, lvl, '+')
        #         else:
        #             self.doop(digital, lvl, operator)
        #     elif (c_len == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
        #         old = 'X'
        #     elif c_len == 1:
        #         if old == 'X':
        #             operator = c[0]
        #     i += 1
    
    # def     doop(self, digital, lvl, operator):
    #     if (lvl == '0'):
    #         if operator == '+':
    #             self.c += digital
    #         elif operator == '-':
    #             self.c -= digital
    #         elif operator == '*':
    #             if (self.c == 0):
    #                 self.c += 1
    #             self.c *= digital
    #     elif (lvl == '1'):
    #         if operator == '+':
    #             self.b += digital
    #         elif operator == '-':
    #             self.b -= digital
    #         elif operator == '*':
    #             if (self.b == 0):
    #                 self.b += 1
    #             self.b *= digital
    #     else:
    #         if operator == '+':
    #             self.a += digital
    #         elif operator == '-':
    #             self.a -= digital
    #         elif operator == '*':
    #             if (self.a == 0):
    #                 self.a += 1
    #             self.a *= digital

def main(argc, argv):
    if (argc != 2):
        print "Error: size argc != 2"
        sys.exit(1)
    answer = argv[1]
    argv = answer.upper()
    p = Polynomial(argv)
    p.convert()
main(len(sys.argv), sys.argv)
