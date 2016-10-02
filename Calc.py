#Calculator by RealStudios
#www.realstudiosen.tumblr.com
#Written in Python 3.5.1
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


#Function that allows to re-use the calculator and view the result   
def end():
    print(calcDone)
    end=input ('Press enter to re-use the calculator')
    main()
    

#Function that does all the job   
def main():
    expressionArray = [ AddExpression(), SubstractExpression(), MultiplyExpression(), DivideExpression(), PowerExpression(), SquareExpression() ]

    expressionMap = dict()
    operators = ''
    for e in expressionArray:
        operators = operators + e.op() + ', '
        expressionMap.update({ e.op(): e })

    operation = input('What do you want to do?(' + operators + '): ')
    #Checks for a valid operation
    if (operation in expressionMap):
        chosenExpression = expressionMap[operation]
        chosenExpression.readArguments()
        chosenExpression.print()

    end()

creator = 'Made by Real and piotro from RealStudios'
ver = 'Version: Open Alpha 0.3.1'
calcDone = 'Operation Succeded!'
print(creator)
print(ver)
main()
