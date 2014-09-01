#CS 260 Project 2: Infix to Postfix Converter
#Written by Matthew Leeds

from arraystack import ArrayStack
from linkedstack import LinkedStack
from scanner import Scanner
from tokens import Token

class IFtoPFConverter(object):
    def __init__(self, scanner):
        self.scanner = scanner

    def convert(self):
        operatorStack = ArrayStack() #this will hold operators and grouping symbols
        postfixExpression = "" #this will hold the final expression
        while self.scanner.hasNext():
            token_char = self.scanner.next()
            if token_char.getType() == 4: #it's an integer
                postfixExpression += str(token_char.getValue()) + " "
            elif token_char.getValue() in ['(','[']: #left parenthesis
                operatorStack.push(token_char)
            elif token_char.isOperator(): #it's an operator
                #pop off all the operators with equal or greater precedence
                while len(operatorStack) != 0 and operatorStack.peek().getPrecedence() >= token_char.getPrecedence():
                    postfixExpression += str(operatorStack.pop().getValue()) + " "
                #now we can push the new operator onto the stack
                operatorStack.push(token_char)
            elif token_char.getValue() in [')',']']: #right parenthesis
                while len(operatorStack) != 0 and operatorStack.peek().getValue() not in ['(','[']: #find the matching one
                    postfixExpression += str(operatorStack.pop().getValue()) + " "
                operatorStack.pop() #discard the left parenthesis
            elif token_char.getType() == 0 and token_char.getValue() not in ['(',')','[',']']: 
                raise Exception("Error: unknown character.") #unknown character
        #transfer over any remaining operators
        while len(operatorStack) != 0:
            postfixExpression += str(operatorStack.pop().getValue()) + " "
        return postfixExpression

def bracketsBalance(exp):
    #checks if the parentheses and brackets all match
    stk = LinkedStack()
    for l in exp: 
        if l in ['(','[']:
            stk.push(l) #push opening braces onto the stack
        elif l in [')',']']:
            if stk.isEmpty():
                return False #the list began with a closing bracket
            fromStack = stk.pop()
            if (l == '(' and fromStack != ')') or (l == '[' and fromStack != ']'):
                return False #non-matching symbols
    if stk.isEmpty(): return True #they all matched up

def main():
    try:
        while True:
            inputstring = input("Enter an infix expression: ")
            if inputstring == '':
                print("Error: empty string!")
            elif not bracketsBalance(inputstring):
                print("Error: non-matching parentheses!")
            else:
                scanner = Scanner(inputstring) #instantiate a scanner
                converter = IFtoPFConverter(scanner) #instantiate the converter
                print(converter.convert())
                if input("Enter another expression? (y/n)") in ['n','N']:
                    break
    except:
        raise

if __name__=="__main__":
    main()
