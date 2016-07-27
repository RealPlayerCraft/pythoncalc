#Calculator by RealStudios
#www.realstudiosen.tumblr.com
#Written in Python 3.5.1
#Adds num1, num2
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

#Function that allows to re-use the calculator and view the result   
def end():
    end=input ('Press any key to re-use the calculator')
    main()
    

#Function that does all the job   
def main():
    operation = input("What do you want to do?(+, -, x, /): ")
    #Checks for a valid operation
    if(operation != "+" and operation != "-" and operation != "x" and operation != "/"):
        print("You must enter a valid operation.")
        main()
    else:
        var1 = int(input("Input the first number: "))
        var2 = int(input("Input the second number: "))
        if(operation == '+'):
            print(add(var1, var2))
            end()
        elif(operation == '-'):
            print(subtract(var1, var2))
            end()
        elif(operation =='x'):
            print(multiply(var1, var2))
            end()
        else:
            print(divide(var1, var2))
            end()
creator = 'Made by Real from RealStudios'
ver = 'Version: Alpha 0.1'
print(creator)
print(ver)
main()
