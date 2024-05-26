contents = ["My name is Mayankesh", "I work for Mitel", "I am a performance expert"]
filenames = ["name.txt", "company.txt", "designation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"files/{filename}", "w")
    file.writelines(content)
    file.close()




