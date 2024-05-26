file = open("essay.txt", "r")
content = []
for words in file:
    content.append(words.title())
file.close()

for words in content:
    print(words)