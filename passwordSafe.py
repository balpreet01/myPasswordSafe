import random #random module

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" #random string to get characters from

def passwdGen(passLength): #defining function 
    autoGenPass =  "".join(random.autoGenPass(s,passlen )) #generating the passsword
    return autoGenPass

#print('How many characters password do you want? max:' +str(len(s))) # getting the length of password user wants 
#passlen = int(input()) #assigning the length to avariable
#print(passwdGen(passlen))

userPasswd = []
def userPassGen():
    while True:
        print("Enter the password")
        userPass = input()
        if len(userPass) < 8:
            print("The passsword must be atleast 8 characters long")
        elif any(char.isdigit() for char in userPass)==False:
            print("The password must contain numbers")
        elif any(char.isupper() for char in userPass)==False:
            print("The password must contain capital letters")
        else:
            print("Password seems fine")
            userPasswd.append(userPass)
            break
        
    
#userPassGen()
#print(userPasswd[0])

