#Simple Calculator

#This function adds two numbers
def plus(x, y):
    return x + y

#This function subtracts two numbers
def minus(x, y):
    return x - y

#This function multiplies two numbers
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    return x / y

#This function uses the modulus operator
def modulus(x, y):
    return x % y

def default(x, y):
    return "Incorrect day"

switcher = {
    1: plus,
    2: minus,
    3: multiply,
    4: divide,
    5: modulus
    }

def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)

#Shows the user the options
print("""Select operation:
1 = Add
2 = Subtract
3 = Multiply
4 = Divide
5 = Modulus""")
print('')

# Take input from user
uInput = int(input("Select operation from 1,2,3,4,5 : "))
print('')

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print('')

print('ANSWER:')
print (switch(uInput, x, y))
