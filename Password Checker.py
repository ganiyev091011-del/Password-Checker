import time
import os

os.system("cls" if os.name == "nt" else "clear")


# foundation (veriables)

print("✅ Creating a New Account")
timeOf = 1.5
symbols = ['!', '@', '#', '$', '^', '&', '*', '/', '|', '_', '-', '()', '(', ')']
numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lowerLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperLetter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

createdAccounts = []

username = str(input("Username: "))
while True:
    print()
    password = str(input("Password: "))
    print()
    
    a = "-" * 40
    print(a)

    print("🔍 Checking the password")
    time.sleep(timeOf)
    if password in createdAccounts:
        print("This password is already created!\n Please create another account!")
        continue
    else:
        print("This password never used before.")
        print("✅ Password is accepted")
        print(a, "\n")

    # Does it have 8+ character
    minLength = 8
    print("🔍 Cheking the number of password...")
    time.sleep(timeOf)
    if len(password) < minLength:
        print("❌ Write 8+ characters for password! ")
        continue
        
    else:
        print("✅ Accepted\n")
        print(a, "\n")

    print("🔍 Checking if there is any numbers in the password...")
    time.sleep(timeOf)
    if any(char in numberList for char in password):
        print("✅ Accepted\n")

        print(a, "\n")

    else:
        print("❌ Add at least one number to password! ")
        continue
        
    print("🔍 Cheking symbols on the password...")
    time.sleep(timeOf)
    if any(char in symbols for char in password):
        print("✅ Accepted\n")
        print(a, "\n")

    else:
        print("❌ Add at least one symbol to password! ")
        continue


    print("🔍 Cheking if there is any lower-case letter...")
    time.sleep(timeOf)
    if any(char in lowerLetter for char in password):
        print("✅ Accepted\n")
        print(a, "\n")
    else:
        print("❌ Add at least one lower-case letter!")
        continue


    print("🔍 Cheking if there is any upper-case letter...")
    time.sleep(timeOf)
    if any(char in upperLetter for char in password):
        print("✅ Accepted\n")
        print(a, "\n")
    else:
        print("❌ Add at least one upper-case letter!")
        continue


    print("🔍 Cheking if there is any spaces in the password...")
    time.sleep(timeOf)
    if " " not in password:
        print("✅ Accepted\n")
       
    else:
        print("❌ There should not be any spaces in the password!")
        continue



    print("⏰ PLease wait a few second, Your account is being ready...\n")
    time.sleep(3)

    print("-" * 75, "\n")
    print("✅ Account Created Successfully.\n")
    createdAccounts.append(password)

    break

