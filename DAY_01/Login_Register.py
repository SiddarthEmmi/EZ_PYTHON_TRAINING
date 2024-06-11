
#DAY-01
'''
Write a program to build login system using functions.The function name should be login_register
1)It should ask user to enter the details for registers and out of all details only username and password should be stored
2)Now this function should ask user to enter username and password.If these match with the registered details login successfull 
otherwise repeat this login process by saying that invalid creditionals until they are right.
'''
def login_register():
    d={}
    print("Welcome to registration")
    u_name=input("Enter your username:")
    u_pd=input("Enter your password:")
    input("Enter name:")
    input("Enter phone number:")
    
    d[u_name]=u_pd
    while True:
        print("Welcome to login")
        lname=input("Enter login username:")
        lpassd=input("Enter login password:")
        #if user exist or not
        if lname in d:
            if d[lname]==lpassd:
                print("Login success")
                break
            else:
                print("Invalid credentials")
        else:
            print("User not found")
login_register()


