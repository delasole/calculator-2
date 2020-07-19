"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

user_input = input("Enter your equation >> ")
output = ""

print(f"You entered {user_input}")

def process(user_input):
    while user_input != " ":
        token = user_input.split(' ')
        if(token[0]== 'q'):
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
        return output

print(process(user_input))
