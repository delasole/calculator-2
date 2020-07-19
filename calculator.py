"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

user_input = input("Enter your equation >> ")
output = ""

print(f"You entered {user_input}")

def process(user_input):
    while user_input != "q":
        token = user_input.split(' ')
        if(token[0] == '+'):
            output = add(float(token[1]),float(token[2]))
        return output

print(process(user_input))
