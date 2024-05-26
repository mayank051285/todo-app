import json

with open("quize.json" , "r") as file:
    content = file.read()

#print(content)
data = json.loads(content)

#print(data)
score = 0
for question in data:
    print(question["question"])
    for index, options in enumerate(question["options"]):
        print(index + 1, "- ", options)

    answer = int(input("Enter your option: "))
    question["answer"] = answer
    if answer == question["Correct"]:
        score = score + 1


for question in data:
    print("Quesiton is ",question["question"], "Your Answer is :", question["answer"], "Correct Answer is : ", question["Correct"])
print("You have scored ", score, "out of ", len(data))
