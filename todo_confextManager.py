prompt = "Enter a option : Add, Show, Replace, Complete, Exit "
todos = []
while True:
    user_input = input(prompt).title()
    match user_input:
        case "Add":
            # file = open('todo.txt' , 'r')
            # todos = file.readlines()
            # file.close()
            # Replacing file operations to with context manager
            with open("todo.txt", "r") as file:
                todos = file.readlines()

            todo = input("Enter a TODO: ").title() + "\n"
            todos.append(todo)

            # file = open('todo.txt' , 'w')
            # file.writelines(todos)
            # file.close()
            # Replacing file operations to with context manager
            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        case "Show":
            #
            # file = open("todo.txt" , "r")
            # todos = file.readlines()
            # adding with context
            # trying to file discriptior to remove /n
            with open("todo.txt" , "r") as files:
                todos = files.readlines()
            new_todos = [item.strip("\n") for item in todos]
            # new_todos = []
            # for item in todos:
            #    new_item = item.strip("\n")
            #    new_todos.append(new_item)
            for index , items in enumerate(new_todos):
                row = f"{index + 1}.{items}"
                print(row)
        case "Complete":
            # file = open('todo.txt' , 'r')
            # todos = file.readlines()
            # file.close()
            with open('todo.txt' , 'r') as file:
                todos = file.readlines()
                if len(todos) != 0:
                    for index , items in enumerate(todos):
                        print(f"{index + 1}.{items}")
                    option = int(input("Enter the item number to delete "))

                    todos.pop(option)
                    # file = open('todo.txt' , 'w')
                    # file.writelines(todos)
                    # file.close()
                    with open("todo.txt", "w") as file:
                        file.writelines(todos)
                else:
                    print("No item to delete")

        case "Replace":
            with open("todo.txt" , "r") as file:
                todos = file.readlines()
                new_todos = [item.strip("\n") for item in todos]

            if len(new_todos) != 0:
                for index , items in enumerate(new_todos):
                    print(f"{index + 1}.{items}")

                option = int(input("Enter the item number to be replace ")) - 1
                newItem = input("Enter new item ")
                todos[option] = newItem + "\n"
                with open("todo.txt" , "w") as file:
                    todos = file.writelines(todos)
            else:
                print("No item to edit")

        case "Exit":
            print("Thank you, have a nice day")
            break
