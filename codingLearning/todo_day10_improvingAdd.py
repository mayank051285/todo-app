def get_todos():
    with open("../todo.txt" , "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


prompt = "Enter a option : Add, Show, Replace, Complete, Exit "
# todos = []
while True:
    user_input = input(prompt).title()

    # match user_input:
    # Adding ifelse ladder instead of match case
    # case "Add":
    if user_input.startswith("Add"):
        # file = open('todo.txt' , 'r')
        # todos = file.readlines()
        # file.close()
        # Replacing file operations to with context manager
        todos = get_todos()

        todo = user_input[4:] + "\n"
        todos.append(todo)

        # file = open('todo.txt' , 'w')
        # file.writelines(todos)
        # file.close()
        # Replacing file operations to with context manager
        with open('../todo.txt' , 'w') as file:
            file.writelines(todos)
    # case "Show":
    elif user_input.startswith("Show"):
        #
        # file = open("todo.txt" , "r")
        # todos = file.readlines()
        # adding with context
        # trying to file discriptior to remove /n
        todos = get_todos()
        new_todos = [item.strip("\n") for item in todos]
        # new_todos = []
        # for item in todos:
        #    new_item = item.strip("\n")
        #    new_todos.append(new_item)
        for index, items in enumerate(new_todos):
            row = f"{index + 1}.{items}"
            print(row)
    # case "Complete":
    elif user_input.startswith("Complete"):
        # file = open('todo.txt' , 'r')
        # todos = file.readlines()
        # file.close()
        todos = get_todos()
        if len(todos) == 0:
            print("No more todos")
            # new_todos = [item.strip("\n") for item in todos]
            # for index , items in enumerate(new_todos):
            #     print(f"{index + 1}.{items}")
            # option = int(input("Enter the item number to delete ")) - 1
        else:
            option = int(user_input[9:]) - 1
            todos.pop(option)
            # file = open('todo.txt' , 'w')
            # file.writelines(todos)
            # file.close()
            with open("../todo.txt" , "w") as file:
                file.writelines(todos)

    # case "Replace":
    elif user_input.startswith("Replace"):
        todos = get_todos()
        new_todos = [item.strip("\n") for item in todos]

        if len(new_todos) == 0:
            print("No more todos")

        else:
            try:
                option = int(user_input[8:]) - 1
                newItem = input("Enter new item ")
                todos[option] = newItem + "\n"
                with open("../todo.txt" , "w") as file:
                    todos = file.writelines(todos)

            except ValueError:
                print(f"your command {user_input} is not valid")

    elif user_input.startswith("Exit"):
        print("Thank you, have a nice day")
        break

    else:
        print(f"{user_input} is not valid")
