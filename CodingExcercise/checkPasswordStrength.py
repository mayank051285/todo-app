def strength(password):
    uppercheck = 0
    digitcheck = 0
    if len(password) > 8:
        for i in password:
            if i.isupper():
                uppercheck = 1

            if i.isdigit():
                digitcheck = 1

    if uppercheck == 1 and digitcheck == 1:
        return "Strong Password"

    else:
        return "Weak Password"


passw = input("Enter the password ")
print(strength(passw))
