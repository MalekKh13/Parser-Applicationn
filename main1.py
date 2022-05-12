import sys

# GLOBAL VARIABLES
global error            # ERROR Variable
global next_token       # NEXT_TOKEN variable
global input_content    # The content of the input variable
global current_index    # The current index of the lexer
error = False
next_token = None
input_content =""
current_index = -1


# Main Entry of the Program
def main1():
    global input_content

    # Check if the arguments contain input filename
    if len(sys.argv) <2:
        print("Please provide input filename")
        return

    # Open the input file 
    file = open(sys.argv[1],'r')

    # read input from file
    input_content = file.read()

    # Start the parsing process
    Grammer()

# lexical analysis function
def lex():
    global current_index
    global next_token

    # get the next character from the file and places it inside next_token.
    current_index += 1
    next_token = input_content[current_index]

    # SKIP WHITE SPACE
    while next_token in [' ','\n','\t','\r']:
        lex()

# return the remaining input in the file.
def unconsumed_input():
    return input_content[current_index:]

# G-> E
def Grammer():
    global error
    global next_token

    lex()
    print("G->E")
    Expression()
    if next_token == '$' and not error:
        print("SUCCESS")
    else:
        print("FAILURE: uncomposed input ",unconsumed_input())

def Expression():
    global error
    global next_token
    if error:
        return
    print("E->TR")
    Terminal()
    RRecursion()

def RRecursion():
    global error
    global next_token
    if error:
        return
    if next_token =='+':
        print("R->+TR")
        lex()
        Terminal()
        RRecursion()

    elif next_token == '-':
        print("R->-TR")
        lex()
        Terminal()
        RRecursion()
    else:
        print("R->e")

def Terminal():
    global error
    global next_token
    if error:
        return
    print("T->FS")
    Factor()
    SRecursion()

def SRecursion():
    global error
    global next_token
    if error:
        return
    if next_token == '*':
        print("S->*FS")
        lex()
        Factor()
        SRecursion()
    elif next_token == '/':
        print("S->/FS")
        lex()
        Factor()
        SRecursion()
    else:
        print("S->e")


def Factor():
    global error
    global next_token
    if error:
        return
    if next_token=='(':
        print("F->(E)")
        lex()
        Expression()
        if next_token == ')':
            lex()
        else:
            error = True
            print("Error: unexpected token ",next_token)
            print("unconsumed input ",unconsumed_input())
    elif next_token.isdigit():
        print("F->N")
        Number()
    else:
        error = True
        print("NError: unexpected token ",next_token)
        print("unconsumed input ",unconsumed_input())

def Number():
    global error
    global next_token
    if error:
        return
    if next_token.isdigit():
        print("N->",next_token)
        lex()
    else:
        error = True
        print("Error: unexpected token ",next_token)
        print("unconsumed input ",unconsumed_input())


if __name__ == '__main__':
    main1()
