import pywhatkit as kit # module to connect to whatsapp
import random #random module
import datetime #datetime module

#string from which password is choosed
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" #random string to get characters from

def passwdGen(passLength): #defining function 
    autoGenPass = "".join(random.sample(s, passLength )) #generating the passsword
    return autoGenPass

secPass = passwdGen(12)#random password created

print("What is you phone number") #ask user for phone number
userPhone = input() #users input

userPhoneNo = "+1"+userPhone #adding country code in front of phone number 
messData = f"Secure password requested is: {secPass}" #formatted string 


kit.sendwhatmsg(userPhoneNo, messData, 20, 58) #sending message to whatsapp at 20:58
