
#DAY-01
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


