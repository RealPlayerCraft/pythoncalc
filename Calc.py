#Calculator by RealStudios
#www.realstudiosen.tumblr.com
#Written in Python 3.5.1
#Adds num1, num2
import math

class Expression(object):
    def eval(self):
        raise NotImplementedError("Please implement this method")

class Constant(Expression):
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value
    
class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left + self.right

class SubstractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left - self.right

class MultiplyExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left * self.right

class DivideExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left / self.right

class PowerExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return math.pow(self.left, self.right)


#Function that allows to re-use the calculator and view the result   
def end():
    end=input ('Press enter to re-use the calculator')
    main()
    

#Function that does all the job   
def main():
    operation = input("What do you want to do?(+, -, x, /, ^): ")
    #Checks for a valid operation
    if(operation != "+" and operation != "-" and operation != "x" and operation != "/" and operation != "^"):
        print("You must enter a valid operation.")
        main()
    else:
        var1 = float(input("Input the first number: "))
        var2 = float(input("Input the second number: "))
        if(operation == '+'):
            expr = AddExpression(var1, var2)
            print(expr.eval())
            end()
        elif(operation == '-'):
            expr = SubstractExpression(var1, var2)
            print(expr.eval())
            end()
        elif(operation =='x'):
            expr = MultiplyExpression(var1, var2)
            print(expr.eval())
            end()
        elif(operation =='^'):
            expr = PowerExpression(var1, var2)
            print(expr.eval())
            end()
        else:
            if(var2 == 0.0):
                print('Hey! What the heck you think you are doing!? Dividing by 0?')
            else: 
                expr = DivideExpression(var1, var2)
                print(expr.eval())
            end()

creator = 'Made by Real and piotro from RealStudios'
ver = 'Version: Open Alpha 0.2.1'
print(creator)
print(ver)
main()
