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
    password = input("Password: ")
    name = input("Name: ")
    #call insert user function 
    insertUser(username, password, name)

#main
print("Welcome to AccountPy! \nPlease enter your choice for next action")
print("1. Register")
print("2. Login")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Thank you for visiting AccountPy. Have a nice day!")
    conn.close()
