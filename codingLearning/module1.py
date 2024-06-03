import glob

filename = glob.glob("files/*.txt")

for files in filename:
    with open(files, "r") as file:
        print(file.readlines())

        