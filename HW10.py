#Name:Tristan long
#Class: 6th Hour
#Assignment: HW10

#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi= True
login=False
admin=False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
admin_login_cnunt= 8
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
wifi = True
login = True
admin = True
counter = 0

if wifi:
    if login:
        if admin:
            print("#welcome message")
            counter += 1
        else:
            print("Error: Missing admin privileges.")
    else:
        print("Error: Missing login credentials.")
else:
    print("Error: Missing wifi connection.")

print(f"Current counter value: {counter}")