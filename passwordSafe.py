
import random #random module
import mysql.connector #mysql connector

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" #random string to get characters from

def passwdGen(passLength): #defining function 
    autoGenPass = "".join(random.sample(s, passlen )) #generating the passsword
    return autoGenPass

#print('How many characters password do you want? max:' +str(len(s))) # getting the length of password user wants 
#passlen = int(input()) #assigning the length to avariable
#print(passwdGen(passlen))

userPasswd = [] #empty array to store user defined password
def userPassGen(): #defining function
    while True: #while loop with true condition to validate password
        print("Enter the password") #asking user for password
        userPass = input() #capturing user input to a variable
        if len(userPass) < 8: #checking if length of password is less than 8 characters
            print("The passsword must be atleast 8 characters long") #asking user to input again and explaining what the issue is
        elif any(char.isdigit() for char in userPass)==False: #checking if password contains numbers
            print("The password must contain numbers")
        elif any(char.isupper() for char in userPass)==False: #checking if password contains capital letters
            print("The password must contain capital letters")
        elif any(char.islower() for char in userPass)==False: #checking if password contains smallletters
            print("The password must contain small letters")
        else:
            print("Password seems fine") #letting user know that the password is fine
            userPasswd.append(userPass) #appending the password to the list
            break #breaking the loop
        
    
#userPassGen()
#print(userPasswd[0])

def baseTable(): #defining function to create table 
    #below is the connection to the database
    cnx = mysql.connector.connect(user='testuser',#username 
                              password='1qw2@WQ!',#password
                              host='localhost',#database server
                              database='test', #database name
                              auth_plugin='mysql_native_password') #mysql authentication plugin
    
    mycursor = cnx.cursor() #creating cursor object
    mycursor.execute("CREATE TABLE IF NOT EXISTS passwordDb (SNo int NOT NULL AUTO_INCREMENT, UserName varchar(255) NOT NULL, Website varchar(255) NOT NULL, Password varchar(255), DateTime datetime, PRIMARY KEY (SNo));") #executing the query
    cnx.close() #closing the connection
    
#baseTable()

