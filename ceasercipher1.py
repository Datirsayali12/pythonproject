print(""" 
-------------------------------------------------------------------------------------------------          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
---------------------------------------------------------------------------------------------------------
""")

l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'
'z']

def encrypt(msg,shiftno):
    msg=msg
    str1=""
    for i in msg:
        index1=l.index(i)
        index1=index1+shiftno
        index1=index1%25
        str1=str1+l[index1] 
    print("Here is your Encrypted message:",str1)

def decrypt(msg,shiftno):
    msg=msg
    str1=""
    for i in msg:
        index1=l.index(i)
        index1=index1-shiftno
        index1=index1%25
        str1=str1+l[index1]
    print("Here is your Decrypted message: ",str1)

option1=False

while not option1:
    op=input("Do you want to continue?Type \n yes/no \n")
    if op=="yes":
        i=int(input(""" Enter number of option:
                        1.Encode.
                        2.Decode
                """))
        msg=input("Type your message to Incrypt/Decrypt: ")
        shiftno=int(input("Enter shift number: "))
        if i==1:
          encrypt(msg,shiftno)
        else:
          decrypt(msg,shiftno)
    else:
        option1=True

