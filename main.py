import sys

def putstr(string):
    sys.stdout.write(string)
def printf(format, *args):
    sys.stdout.write(format % args)


# def   main_input():
#   putstr("Input: ")
#   try:
#       answer = raw_input()
#       return answer
#   except:
#       print "\nError input"
#       sys.exit(0)

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
    countOperatorX = 0
    countOperatorAll = 0
    countX = 0
    lvlDegree = 0

    def     __init__(self, argv):
        self.inputParam = argv.split(" ")

    def     CheckInputParam(self):
        old = '0' 
        for c in self.inputParam:
            size = len(c)
            if ((isfloat(c)) == True): # CHECK input
                if (old != '0' and old != 'o' and old != '='):
                    print "Error: syntax error with before digital", c
                    sys.exit(1)
                self.countDigital += 1
                old = 'd'
            elif ((c.isalpha()) == 1): # CHECK ERROR
                print "Error: syntax error in ", c
                sys.exit(1)
            elif (size == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
                self.countX += 1
                if (old != '*'):
                    print "Error: math error operator", c
                    sys.exit(1)
                old = 'x'
            elif (size == 1 and c[0] == '='):
                self.countOperatorRavno += 1
                if (old != 'x'):
                    print "Error: math error \'=\'"
                    sys.exit(1)
                old = '='
            elif (size == 1 and (c[0] == '*' or c[0] == '+' or c[0] == '-')):
                if (old == 'x'):
                    old = 'o'
                    self.countOperatorAll += 1
                elif (old == 'd' and c[0] != '*'): # ERROR CHECK
                    print "Error: math error with * in ", c
                    sys.exit(1)
                elif (old == 'd' and c[0] == '*'):
                    self.countOperatorX += 1
                    old = '*'
                else:
                    print "Error: math error with operator"
                    sys.exit(1)
            elif (size >= 3 and 'X^' in c):
                print "Error: Level degree too big or invalid", c
                sys.exit(1)
            elif (size > 1):
                print "Error: syntax error in ", c
                sys.exit(1)
        if (old != 'x'):
            print "Error: syntax error in end"
            sys.exit(1)

    def     valid(self):
        print self.inputParam ### need delete
        # print "Len ", len(self.inputParam) ### need delete

        self.CheckInputParam()

       # print "Count Digital", self.countDigital ## need delete
       # print "Count X ", self.countX ## need delete
       # print "countOperator ", self.countOperator # need delete
        self.checkRes()
        # here all valid
        return 1

    def     checkRes(self):
        if (self.countDigital != self.countX):
            print "Error: math error, Count digital != count X^[0-2]"
            sys.exit(1)
        elif self.countOperatorRavno != 1:
            print "Error: math error, syntax error with \'=\'"
            sys.exit(1)
        elif (self.countDigital != self.countOperatorX):
            print "Error: math error, count digital != count operator * and Count X^[0-2]"
            sys.exit(1)
    
    def     join(self):
        string = ""
        for c in self.inputParam:
                string = string + " " + c
        return string.split("=")
    
    def     parsString(self, string):
        res = string.strip()
        res = res.split(" ")
        return res

    def     doop(self, digital, lvl, operator):
        if (operator == '0'):
            print "ERROR"
            sys.exit(1)

        if (lvl == '0'):
            if operator == '+':
                self.c += digital
            elif operator == '-':
                self.c -= digital
            elif operator == '*':
                if (self.c == 0):
                    self.c += 1
                self.c *= digital
        elif (lvl == '1'):
            if operator == '+':
                self.b += digital
            elif operator == '-':
                self.b -= digital
            elif operator == '*':
                if (self.b == 0):
                    self.b += 1
                self.b *= digital
        else:
            if operator == '+':
                self.a += digital
            elif operator == '-':
                self.a -= digital
            elif operator == '*':
                if (self.a == 0):
                    self.a += 1
                self.a *= digital



import sys

def putstr(string):
    sys.stdout.write(string)

# def   main_input():
#   putstr("Input: ")
#   try:
#       answer = raw_input()
#       return answer
#   except:
#       print "\nError input"
#       sys.exit(0)

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
    countOperatorX = 0
    countOperatorAll = 0
    countX = 0
    lvlDegree = 0

    def     __init__(self, argv):
        self.inputParam = argv.split(" ")

    def     CheckInputParam(self):
        old = '0' 
        for c in self.inputParam:
            size = len(c)
            if ((isfloat(c)) == True): # CHECK input
                if (old != '0' and old != 'o' and old != '='):
                    print "Error: syntax error with before digital", c
                    sys.exit(1)
                self.countDigital += 1
                old = 'd'
            elif ((c.isalpha()) == 1): # CHECK ERROR
                print "Error: syntax error in ", c
                sys.exit(1)
            elif (size == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
                self.countX += 1
                if (old != '*'):
                    print "Error: math error operator", c
                    sys.exit(1)
                old = 'x'
            elif (size == 1 and c[0] == '='):
                self.countOperatorRavno += 1
                if (old != 'x'):
                    print "Error: math error \'=\'"
                    sys.exit(1)
                old = '='
            elif (size == 1 and (c[0] == '*' or c[0] == '+' or c[0] == '-')):
                if (old == 'x'):
                    old = 'o'
                    self.countOperatorAll += 1
                elif (old == 'd' and c[0] != '*'): # ERROR CHECK
                    print "Error: math error with * in ", c
                    sys.exit(1)
                elif (old == 'd' and c[0] == '*'):
                    self.countOperatorX += 1
                    old = '*'
                else:
                    print "Error: math error with operator"
                    sys.exit(1)
            elif (size >= 3 and 'X^' in c):
                print "Error: Level degree too big or invalid", c
                sys.exit(1)
            elif (size > 1):
                print "Error: syntax error in ", c
                sys.exit(1)
        if (old != 'x'):
            print "Error: syntax error in end"
            sys.exit(1)

    def     valid(self):
        print self.inputParam ### need delete
        # print "Len ", len(self.inputParam) ### need delete

        self.CheckInputParam()

       # print "Count Digital", self.countDigital ## need delete
       # print "Count X ", self.countX ## need delete
       # print "countOperator ", self.countOperator # need delete
        self.checkRes()
        # here all valid
        return 1

    def     checkRes(self):
        if (self.countDigital != self.countX):
            print "Error: math error, Count digital != count X^[0-2]"
            sys.exit(1)
        elif self.countOperatorRavno != 1:
            print "Error: math error, syntax error with \'=\'"
            sys.exit(1)
        elif (self.countDigital != self.countOperatorX):
            print "Error: math error, count digital != count operator * and Count X^[0-2]"
            sys.exit(1)
    
    def     join(self):
        string = ""
        for c in self.inputParam:
                string = string + " " + c
        return string.split("=")
    
    def     parsString(self, string):
        res = string.strip()
        res = res.split(" ")
        return res

    def     doop(self, digital, lvl, operator):
        if (lvl == '0'):
            if operator == '+':
                self.c += digital
            elif operator == '-':
                self.c -= digital
            elif operator == '*':
                if (self.c == 0):
                    self.c += 1
                self.c *= digital
        elif (lvl == '1'):
            if operator == '+':
                self.b += digital
            elif operator == '-':
                self.b -= digital
            elif operator == '*':
                if (self.b == 0):
                    self.b += 1
                self.b *= digital
        else:
            if operator == '+':
                self.a += digital
            elif operator == '-':
                self.a -= digital
            elif operator == '*':
                if (self.a == 0):
                    self.a += 1
                self.a *= digital

    def     reducePartOne(self, partOne):
        size = len(partOne)
        digital = 0
        operator = '0'
        old = '0'
        i = 0
        for c in partOne:
            c_len = len(c)
            if ((isfloat(c)) == True):
                digital = float(c)
                tmp = partOne[i + 2]
                lvl = tmp[2]
                old = 'digital'
                if ((operator == '0')):
                    self.doop(digital, lvl, '+')
                else:
                    self.doop(digital, lvl, operator)
            elif (c_len == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
                old = 'X'
            elif c_len == 1:
                if old == 'X':
                    operator = c[0]
            i += 1

    def     reducePartTwo(self, partOne):
        size = len(partOne)
        digital = 0
        operator = '0'
        old = '0'
        i = 0
        for c in partOne:
            c_len = len(c)
            if ((isfloat(c)) == True):
                digital = float(c)
                tmp = partOne[i + 2]
                lvl = tmp[2]
                old = 'digital'
                if (operator == '0' and digital > 0):
                    self.doop(digital, lvl, '-')
                elif operator == '0' and digital < 0:
                    self.doop(digital, lvl, '+') 
                # if ((operator == '0')):
                #     self.doop(digital, lvl, '+')
                # else:
                #     self.doop(digital, lvl, operator)
            elif (c_len == 3 and (('X^1' in c) or ('X^0' in c) or ('X^2' in c))):
                old = 'X'
            elif c_len == 1:
                if old == 'X':
                    operator = c[0]
            i += 1

    
    def     findLvl(self):
        if self.a != 0:
            self.lvlDegree = 2
        elif self.b != 0:
            self.lvlDegree = 1
        elif self.c != 0:
            self.lvlDegree = 0

    # def     printLvl0(self):
    #     if self.c == 0:
    #         print "Reduced form: 0 = 0"
    #     else:    
    #         print "Reduced form:", self.c, "* X^0", "= 0"
    
    # def     printLvl1(self):
    #     tmp = 0
    #     c = self.c
    #     b = self.b
        
    #     if b < 0:
    #         tmp2 = '-'
    #         b *= -1
    #     else:
    #         tmp2 = '+'
        
    #     putstr("Reduced form:")
    #     if (c != 0):
    #         tmp = 1
    #         printf(" %f * X^0", c)
    #     if (b != 0 and tmp == 1):
    #         printf(" %c %f * X^1 = 0", tmp2, b)
    #     elif (b != 0 and tmp == 0):
    #         printf(" %f * X^1 = 0", b)
    #     putstr("\n")
    
    # def     printLvl2(self):
    #     a = self.a
    #     b = self.b
    #     c = self.c

    #     tmpC = 0
    #     tmpB = 0
    #     if b < 0:
    #         tmp2 = '-'
    #         b *= -1
    #     else:
    #         tmp2 = '+'
    #     if a < 0:
    #         a *= -1
    #         tmp3 = '-'
    #     else:
    #         tmp3 = '+'        
    #     putstr("Reduced form:")
    #     if (c != 0):
    #         tmpC = 1
    #         printf(" %f * X^0", c)

    #     if (b != 0 and tmpC== 1):
    #         tmpB = 1
    #         printf(" %c %f * X^1", tmp2, b)
    #     elif (b != 0 and tmpC == 0):
    #         tmpB = 1
    #         printf(" %f * X^1", b)

    #     if (a != 0 and tmpB == 1):
    #         printf(" %c %f * X^2 = 0", tmp3, a) ## error

    #     putstr("\n")

    def     printOnePartOutput(self):
        tmp2 = ""
        if (self.lvlDegree == 0):
            self.printLvl0()
        elif self.lvlDegree == 1:
            self.printLvl1()
        elif self.lvlDegree == 2:
            self.printLvl2()
        print "Polynomial degree: ", self.lvlDegree
    
    def     convert(self):
        res = self.valid()
        string = self.join()
        partOne = self.parsString(string[0])
        partTwo = self.parsString(string[1])
        # print "PartOne ", partOne
        self.reducePartOne(partOne)
        self.reducePartTwo(partTwo)
        
        print "a ", self.a # need delete
        print "b ", self.b # need delete
        print "c ", self.c # need delete
        print "KO"
        # self.findLvl()
        # self.printOnePartOutput()
        # print "Reduced form: ", c, " * X^0 ", 
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
    # print "OK"
    # return (1)
main(len(sys.argv), sys.argv)