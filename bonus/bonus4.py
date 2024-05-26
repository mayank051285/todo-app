filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    print(filename)
    filename = filename.replace('.', '-', 1)
    print(filename)
