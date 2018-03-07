import sys

def putstr(string):
    sys.stdout.write(string)
def printf(format, *args):
    sys.stdout.write(format % args)
def     Error(string):
    print string
    sys.exit(1)

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    return True