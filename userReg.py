import pymysql
#connection to mysql database
conn = pymysql.connect(user='root', password='', host='localhost', database='accountpy')
cursor = conn.cursor()

#function to insert user details into database
def insertUser(username, password, name):
    insertUser = "INSERT INTO user (username, password, name) VALUES (%s, %s, %s);"
    data = (username, password, name)
    cursor.execute(insertUser, data)
    conn.commit()
    print("User registered successfully! Log in to access your account.")
    choice = input("Would you like to login? (Y/N): ")
    if choice.upper() == "Y":
        login() #login function
    else:
        print("Thank you for registering with us. Have a nice day!!")
        conn.close()

def logout():
    choice = input("Would you like to logout? (Y/N): ")
    while choice.upper() == "N":
        print("Okay, continue with your session.")
        choice = input("Would you like to logout? (Y/N): ")
    print("Thank you for visiting AccountPy. Have a nice day!")
    conn.close()

def login():
    print("-----Login-----")
    username = input("Username: ")
    password = input("Password: ")
    query = "SELECT * FROM user WHERE username = %s AND password = %s;"
    data = (username, password)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if len(result) > 0:
        print("Welcome " + result[0][3] + "!!") #print name
        logout()
    else:
        print("Invalid username or password. Please try again.")
        login()

#registration function
def register():
    print ("-----Registration-----")
    print ("Enter your details below: ")
    username = input("Username: ")
    #check if username already exists
    while True:
        check = "SELECT * FROM user WHERE username = %s;"
        cursor.execute(check, username)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Username already exists. Please try another username.")
            username = input("Username: ")
        else:
            break
    
    password = input("Password: ")
    #password length validation 
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Password: ")
    #password confirmation
    passwordConfirm = input("Confirm password: ")
    while password != passwordConfirm:
        print("Passwords do not match. Please try again.")
        password = input("Password: ")
        passwordConfirm = input("Confirm password: ")

    name = input("Name: ")
    #call insert user function 
    insertUser(username, passwordConfirm, name.title())

#main
print("Welcome to AccountPy!")
while True:
    print ("-----Main Menu-----")
    print ("Please select an option below: ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
        break
    elif choice == 2:
        login()
        break
    elif choice == 3:
        print("Thank you for visiting AccountPy. Have a nice day!")
        conn.close()
        break
    else:
        print("Invalid choice. Please enter choice 1-3.")
