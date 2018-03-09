import sys
import math
import numpy as np
from module import *

class   Matrix:
    def     __init__(self, size):
        self.matrixA = np.zeros(size)
        self.matrixB = np.zeros(size)
        self.matrixC = np.zeros(size)

    def     convertMatrix(self, string):
        old = '-1'
        x = 0
        A = 0
        B = 0
        C = 0
        for c in string:
            size = len(c)
            if ((isfloat(c)) == True):
                digital = float(c)
                if (old == '-'):
                    digital *= -1
                tmpX = string[x + 2]
                xLvl = tmpX[2]
                old = 'd'
                if xLvl == '0':
                    self.matrixC[C] = digital
                    C += 1
                elif xLvl == '1':
                    self.matrixB[B] = digital
                    B += 1
                elif xLvl == '2':
                    self.matrixA[B] = digital
                    B += 1
            elif size == 1 and c[0] == '-':
                old = '-'
            x += 1
    def     printMatrix(self, string): # need delete this function
        print string
        print "A",self.matrixA
        print "B",self.matrixB
        print "C",self.matrixC

    def     mathMatrix(self, matrix, operator='+'):
        x = 0.0
        i = 0
        while i < len(matrix):
            if operator == '+':
                x += matrix[i]
            else:
                x -= matrix[i]
            i += 1
        return x

class Polynomial:
    a = 0
    b = 0
    c = 0
    t0 = 0.0
    t1 = 0.0
    t1s = ''
    t0s = ''
    d = 0
    countDigital = 0
    countOperator = 0
    countOperatorRavno = 0
    countOperatorX = 0
    countX = 0
    lvlDegree = 0
    s = 0

    def     __init__(self, argv):
        self.inputParam = argv.split(" ")

    def     convert(self):
        self.valid()
        string = self.join()
        partOne = self.parsString(string[0])
        partTwo = self.parsString(string[1])
        self.reduce(partOne, partTwo)
        self.findLvlDegree()

        # print "a ", self.a # need delete
        # print "b ", self.b # need delete
        # print "c ", self.c # need delete
        # print "Lvl degree", self.lvlDegree
        # sys.exit(1)
    
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

    def     reduce(self, partOne, partTwo):
        oneM = Matrix(self.countDigital)
        twoM = Matrix(self.countDigital)
        oneM.convertMatrix(partOne)
        twoM.convertMatrix(partTwo)
        self.c = oneM.mathMatrix(oneM.matrixC)
        self.b = oneM.mathMatrix(oneM.matrixB)
        self.a = oneM.mathMatrix(oneM.matrixA)
        self.c = self.c + oneM.mathMatrix(twoM.matrixC, '-')
        self.b = self.b + oneM.mathMatrix(twoM.matrixB, '-')
        self.a = self.a + oneM.mathMatrix(twoM.matrixA, '-')

    def     findLvlDegree(self):
        if (self.a != 0):
            self.lvlDegree = 2
        elif self.b != 0:
            self.lvlDegree = 1
        else:
            self.lvlDegree = 0

    def     printResult(self):
        self.printReduce()
        print "Polynomial degree:", self.lvlDegree
        self.printSolution()

    def     printReduce(self):
        string = self.createStringReduce()
        print string

    def     createStringReduce(self):
        string = "Reduced form: "
        if (self.c != 0):
            string = string + str(self.c) + " * X^0"
        if (self.b != 0):
            string = string + self.checkStringB()
        if (self.a != 0):
            string = string + self.checkStringA()
        string = string + " = 0"
        return string

    def     checkStringB(self):
        string = ""
        flag = 0
        if (self.c != 0):
            flag = 1
        if flag == 1:
            if self.b < 0:
                tmpB = self.b * -1
                string = string + " - " + str(tmpB)
            else:
                string = string + " + " + str(self.b)
        else:
            string = string + str(self.b)
        string = string + " * X^1"
        return string

    def     checkStringA(self):
        string = ""
        flag = 0
        if (self.b != 0 or self.c):
            flag = 1
        if flag == 1:
            if self.a < 0:
                tmpA = self.a * -1
                string = string + " - " + str(tmpA)
            else:
                string = string + " + " + str(self.a)
        else:
            string = string + str(self.a)
        string = string + " * X^2"
        return string

    def     printSolution(self):
        if self.lvlDegree == 2:
            if self.d > 0:
                print "Discriminant is strictly positive, the two solutions are:"
                print self.t0
                print self.t1
            elif self.d == 0:
                print "The discriminant is zero solution one:"
                print self.t0
            elif self.d < 0:
                print "Its discriminant is strictly negative, so it has exactly two complex solutions:"
                print str(self.t0s)
                print str(self.t1s)
        elif self.lvlDegree == 1:
            print "Equation with one unknown, the one solutions are:"
            print self.t0
        elif self.lvlDegree == 0:
            print "All the real numbers are solution..."

    def     decideEquation(self):
        if (self.a != 0):
            self.doubleEquation()
        else:
            self.linealEquation()

    def     doubleEquation(self):
        d = self.b * self.b - 4 * self.a * self.c
        res = 0
        i = -1
        if d < 0:
            s = int(-d) ** 0.5
            tmpA = (2 * self.a)
            tmpB = (-self.b / tmpA)
            tmpS = i * (s / tmpA)
            self.t0s = str(tmpB) + ' + i * ' + str(tmpS)
            self.t1s = str(tmpB) + ' - i * ' + str(tmpS) 
        if d == 0:
            sd = d ** 0.5
            self.t0 = (-self.b + sd) / (2 * self.a);
        elif d > 0:
            sd = d ** 0.5
            self.t0 = (-self.b + sd) / (2 * self.a);
            self.t1 = (-self.b - sd) / (2 * self.a);
        self.d = d

    def     linealEquation(self):
        self.c *= -1
        self.t0 = self.c / self.b

def main(argc, argv):
    if (argc != 2):
        print "Error: size argc != 2"
        sys.exit(1)
    answer = argv[1]
    argv = answer.upper()
    p = Polynomial(argv)
    p.convert()
    p.decideEquation()
    p.printResult()
main(len(sys.argv), sys.argv)