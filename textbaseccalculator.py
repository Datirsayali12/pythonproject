import math
print('*'*130)
print("                                                 TEXT BASED CALCULATOR                                     ")
print("*"*130)
print(""" 
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

""")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    return a/b
def square(a):
    return a**2
def cube(a):
    return a**3
def squareroot(a):
    return math.sqrt(a)
def fact(a):
    return math.factorial(a)

flag=False
while not flag:
    n1=eval(input("Enter number one:"))
    op=int(input("""Type number of operations:
                    1.+
                    2.-
                    3.*
                    4./
                    5.square
                    6.cube
                    7.squareroot
                    8.factorial
                \n"""))
    if op!=5 and op!=6 and op!=7 and op!=8:
        n2=eval(input("Enter number two:"))

    if op==1:
        print(f"Addition of {n1}+{n2} :",add(n1,n2))
    elif op==2:
        print(f"substraction of {n1}-{n2} :",sub(n1,n2))
    elif op==3:
        print(f"multiplication of {n1}*{n2} :",mul(n1,n2))
    elif op==4:
        print(f"Division of {n1}/{n2} :",division(n1,n2))
    elif op==5:
        print(f"square of {n1}:",square(n1))
    elif op==6:
        print(f"cube of {n1}:",cube(n1))
    elif op==7:
        print(f"Cuberoot of {n1}:",squareroot(n1))
    elif op==7:
        print(f"Factorial of {n1}:",fact(n1))
    yn=input("Do you want to continue?yes/no")
    if yn=="no":
        flag=True
