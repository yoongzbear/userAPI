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
    print("User registered successfully! \nWelcome " + name + "!!")
    choice = input("Would you like to login? (Y/N): ")
    if choice.upper() == "Y":
        login() #login function
    else:
        print("Thank you for registering with us. Have a nice day!!")
        conn.close()

print ("Account Registration")
print ("Enter your details below: ")
username = input("Username: ")
password = input("Password: ")
name = input("Name: ")

insertUser(username, password, name)
