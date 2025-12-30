import random as rdm
import string as st

def generatePassword(length):
    passStr = "" + st.ascii_lowercase
    askUppercase = input("Do u want your password to contain uppercase letters (A-Z)? Type Y/N: ")

    while askUppercase == "Y".lower() or askUppercase == "N".lower():
        if askUppercase == "Y".lower():
            passStr += st.ascii_uppercase
            break
        elif askUppercase == "N".lower():
            break
        else:
            askUppercase = input("Invalid character please add Y/N: ")
            continue
    
    askDigits = input("Do u want your password to contain digits (0-1)? Type Y/N: ")
    while askDigits == "Y".lower() or askDigits == "N".lower():
        if askDigits == "Y".lower():
            passStr += st.digits
            break
        elif askDigits == "N".lower():
            break
        else:
            askDigits = input("Invalid character please add Y/N: ")
            continue
    
    askSpecialCharacters = input("Do u want your password to contain Special Characters (#@%^ etc)? Type Y/N: ")
    while askSpecialCharacters == "Y".lower() or askSpecialCharacters == "N".lower():
        if askSpecialCharacters == "Y".lower():
            passStr += st.punctuation
            break
        elif askSpecialCharacters == "N".lower():
            break
        else:
            askSpecialCharacters = input("Invalid character please add Y/N: ")
            continue

    password = "".join(rdm.choices(passStr, k=length))
    return password

while(True):
    length = int(input("Enter the length of your password: "))
    password = generatePassword(length)
    print("Your generated password: ", password)
    again = input("Do you want to continue? Y/N: ")
    if again == "Y".lower():
        continue
    elif again == "N".lower():
        break
    else: 
        again = input("Invalid Character!!! Please input a valid character (Y/N): ")
        if again == "Y".lower():
            continue
        elif again == "N".lower():
            break


