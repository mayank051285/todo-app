password = input("Enter a password ")
test = "false"
if len(password) >= 8:
    for i in password:
        if i.isdigit():
            for j in password:
                if j.isupper():
                    test = "True"
                    break
                # else:
                #     print(f"{password} is not contain upper case")
                #     break

        # else:
        #     print(f"{password} is not contain digit")
        #     break
if test == "True":
    print("Strong password")
else:
    print("Weak Password")
