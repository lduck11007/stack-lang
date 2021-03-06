import sys

def invalidCommand(a = None):
    if a:
        print "Invalid command '{}'".format(a)
    else:
        print "Invalid Command"
    sys.exit()

def stackArgumentLenError(a = None):
    if a:
        print "invalid stack length for operation '{}'".format(a)
    else:
        print "invalid stack length for operation"
    sys.exit()

def syntaxError():
    print "Invalid Syntax"
    sys.exit()

def valueError():
    print "valueError"
    sys.exit()

def opError(a = None):
    print "Invalid types for operation"
    sys.exit()

def noClosingStatement(a = None):
    print "No closing statement for conditional/loop"
    sys.exit()

def reserved():
    print "Error: Cannot assign to reserved"
    sys.exit()

def preprocess(a = None):
    if a:
        print a
    else:
        print "Error scanning preprocessing statement"

def indexError(a = None):
    if a:
        print "IndexError: {}".format(a)
    else:
        print "IndexError"
    sys.exit()

def conversionError(a = None):
    if a:
        print "Conversion error: {}".format(a)
    else:
        print "Conversion error"
    sys.exit()

def error(a):
    print a
    sys.exit()
