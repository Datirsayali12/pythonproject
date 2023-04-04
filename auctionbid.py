
print('''------------------------------------------AUCTION BIDDING-----------------------------------------
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
--------------------------------------------------------------------------------------------------------''')
print("------------------------------------------START BIDDING--------------------------------------------")
def bid1(n,v):
    d[n]=v

name=input("Enter your name: ")
bid=int(input("Enter your bid: "))
d={}
d[name]=bid

flag=False
while not flag: 
    op=input("Are any other bidder-yes/no type: \n")
    if op=="no":
        break
    n=input("Enter name: \n")
    v=int(input("Enter bid: \n"))
    if op=="yes":
        bid1(n,v)
   
max1=0
for i in d:
    if d[i]> max1:
        max1=d[i]
#print("$",max1)
for j in d:
    if d[j]==max1:
        print(f"Congrats {j} !!!!!! you are winner with maximum bid {max1}")




