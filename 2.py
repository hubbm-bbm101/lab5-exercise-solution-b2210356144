loop = 1
while loop == 1:
    email = input("Enter a email with '@' and '.' :")
    if "@" in email :
        if "." in email:
            print(email,": is a valid email.")
            loop = 0
        else:
            print(email,": is NOT a valid email.Try again.")
    else :
        print(email, ": is NOT a valid email.Try again.")


