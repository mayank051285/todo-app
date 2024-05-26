file = open("member.txt", "a")
testToWrite = input("Enter the new member name")
file.writelines(testToWrite + "\n")
file.close()