# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name1.lower()
name2.lower()
#Write your code below this line 👇
t=name1.count("t")+name2.count("t")
r=name1.count("r")+name2.count("r")
u=name1.count("u")+name2.count("u")
e=name1.count("e")+name2.count("e")
totalT=t+r+u+e
l=name1.count("l")+name2.count("l")
o=name1.count("o")+name2.count("o")
v=name1.count("v")+name2.count("v")
e=name1.count("e")+name2.count("e")
totalL=l+o+v+e

number=10*totalT+totalL
print(number)

if number <10 or number>90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number>40 and number <50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"your score is {number}")










