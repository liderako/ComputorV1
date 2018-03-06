import sys

# def putstr(string):
#     sys.stdout.write(string)

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
        print "Len ", len(self.inputParam) ### need delete

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
    def     convert(self):
        res = self.valid()
        tmpD = 0.0
        tmpO = '0'
        tmpX = -1
        flagTwoPart = 0
        i = 0
        j = 0
        for c in self.inputParam:
            if ((isfloat(c)) == True):
                tmpD = isfloat(c)
                tmpString = self.inputParam[j + 2]
                tmpX = int(tmpString[2])
                if (tmpX == '0')
                    # self.a = tmpD
                elif (tmpX == '1')

                elif (tmpX == '2')

                # tmpX = self.inputParam[j + 2]
            j += 1
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