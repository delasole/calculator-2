"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

user_input = input("Enter your equation >> ")
output = ""

def process(user_input):
    while True:
        token = user_input.split(' ')
        if(token[0]== 'q'):
            print("You have left")
            break
        else:
            if(token[0] == '+'):
                output = add(float(token[1]),float(token[2]))
            if(token[0] == '-'):
                output = subtract(float(token[1]),float(token[2]))
            if(token[0] == '*'):
                output = multiply(float(token[1]),float(token[2]))
            if(token[0] == '/'):
                output = divide(token[1],float(token[2]))
            if(token[0] == 'square'):
                output = square(float(token[1]))
            if(token[0] == 'cube'):
                output = cube(float(token[1]))
            if(token[0] == 'pow'):
                output = power(float(token[1]),float(token[2]))
            if(token[0] == 'mod'):
                output = mod(float(token[1]),float(token[2]))
            if(token[0] == 'quit'):
                print("You have left")
                break
        return output

print(process(user_input))
