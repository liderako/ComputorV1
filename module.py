import sys

def putstr(string):
    sys.stdout.write(string)
def printf(format, *args):
    sys.stdout.write(format % args)

def   main_input():
  putstr("Input: ")
  try:
      answer = raw_input()
      return answer
  except:
      print "\nError input"
      sys.exit(0)

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    return True