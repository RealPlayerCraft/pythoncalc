#Calculator by RealStudios
#www.realstudiosen.tumblr.com
#Written in Python 3.5.1
#Adds num1, num2
import math

def add(num1, num2):
    return num1 + num2

#Subtracts num1, num2
def subtract(num1, num2):
    return num1 - num2

#Multiplies num1, num2     
def multiply(num1, num2):
    return num1 * num2

#Divides num1, num2     
def divide(num1, num2):
    return num1 / num2

#Power num1, num2     
def power(num1, num2):
    return math.pow(num1, num2)


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
            print(add(var1, var2))
            end()
        elif(operation == '-'):
            print(subtract(var1, var2))
            end()
        elif(operation =='x'):
            print(multiply(var1, var2))
            end()
        elif(operation =='^'):
            print(power(var1, var2))
            end()
        else:
            if(var2 == 0.0):
                print('Hey! What the heck you think you are doing!? Dividing by 0?')
            else: 
                print(divide(var1, var2))
            end()
creator = 'Made by Real and piotro from RealStudios'
ver = 'Version: Open Alpha 0.2'
print(creator)
print(ver)
main()
