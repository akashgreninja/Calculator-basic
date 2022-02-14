import art

from art import logo
print(logo)
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operand={
    "+": add,
    "-": sub,
    "/": divide,
    "*": multiply,

}

def calc():
    a=float(input("whats no 1 ? \n"))

    end_of_game=False
    while end_of_game==False:
        for num in operand:
            print(num)
        c=input("input an operand from above ")
        d=float(input("whats no 2 ? \n"))


        z=operand[c]
        y=z(a,d)
        print(f"{a}{c}{d} = {z(a,d)}")

        w=input("do you want to continue y or n to start a new calc ")

        if w == "n":
            end_of_game=True
            calc()

        else:
            a=y
calc()