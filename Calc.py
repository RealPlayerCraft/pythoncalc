#Calculator by RealStudios
#www.him8gr8k.ueuo.com
#Written in Python 3.5.2
#For more helpcontact us on github https://github.com/RealPlayerCraft/pythoncalc
#Feel free to fork
import math

class Expression(object):
    def eval(self):
        raise NotImplementedError("Please implement this method")

    def print(self):
        print(self.eval());

    def readFloat(self, message):
        return float(input(message))

class OneArgExpression(Expression):
    def readArguments(self):
        self.arg = self.readFloat("Input the number: ")
    

class SquareExpression(OneArgExpression):
    def eval(self):
        return self.arg * self.arg

    def op(self):
        return "s"
    

class TwoArgExpression(Expression):
    left = 0.0
    right = 0.0

    def readArguments(self):
        self.left = self.readFloat("Input the first number: ")
        self.right = self.readFloat("Input the second number: ")
    
class AddExpression(TwoArgExpression):
    def eval(self):
        return self.left + self.right

    def op(self):
        return "+"

class SubstractExpression(TwoArgExpression):
    def eval(self):
        return self.left - self.right

    def op(self):
        return "-"

class MultiplyExpression(TwoArgExpression):
    def eval(self):
        return self.left * self.right

    def op(self):
        return "x"
		
		
class DivideExpression(TwoArgExpression):
    def eval(self):
        return self.left / self.right

    def op(self):
        return "/"

class PowerExpression(TwoArgExpression):
    def eval(self):
        return math.pow(self.left, self.right)

    def op(self):
        return "^"

class HelpExpression(Expression):
    def eval(self):
        return '''
        This is help for calculator:
        Choose one of available operations and follow instructions.
        If you want to exit just hit enter or type an invalid operation.
        For more help contact us on github.
        Official GitHub link https://github.com/RealPlayerCraft/pythoncalc
        '''
    def readArguments(self):
        print()

    def op(self):
        return "help"

def readOperation(operators):
    return input('Choose an operator.(' + operators + '): ')

#Function that does all the job
def main():
    #Initialize expressions array
    expressionArray = [ AddExpression(), SubstractExpression(), MultiplyExpression(), DivideExpression(),
    PowerExpression(), SquareExpression(), HelpExpression() ]

    expressionMap = dict()
    separator = ', '
    operators = ''
    for e in expressionArray:
        operators = operators + e.op() + separator
        expressionMap.update({ e.op(): e })

    operators = operators[:-len(separator)]


    operation = readOperation(operators)
    while operation in expressionMap:
        chosenExpression = expressionMap[operation]
        chosenExpression.readArguments()
        chosenExpression.print()
        print()
        operation = readOperation(operators)


    print('Thank you for using this calculator')

creators = 'Made by Real, piotro and historis from RealStudios'
ver = 'Version: Open Alpha 0.3.3'
print(creators)
print(ver)
main()

