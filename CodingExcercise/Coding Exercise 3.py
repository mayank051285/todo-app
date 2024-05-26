ranking = ['John', 'Sen', 'Lisa']
name = input("Enter user user name")
i = 1
for rank in ranking:
    if name == rank:
        print(rank)
        print(i)
    i = i + 1
