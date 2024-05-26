prompt = "Enter a option : Add, Show, Replace, Delete, Exit "
todos = []
while True:
    user_input = input(prompt).title()
    match user_input:
        case "Add":
            file = open('todo.txt' , 'r')
            todos = file.readlines()
            file.close()
            todo = input("Enter a TODO: ").title() + "\n"
            todos.append(todo)
            file = open('todo.txt' , 'w')
            file.writelines(todos)
            file.close()
        case "Show":
            file = open("todo.txt" , "r")
            todos = file.readlines()
            # trying to file discriptior to remove /n
            new_todos = [item.strip("\n") for item in todos]
            # new_todos = []
            # for item in todos:
            #    new_item = item.strip("\n")
            #    new_todos.append(new_item)
            file.close()
            for index , items in enumerate(new_todos):
                row = f"{index + 1}.{items}"
                print(row)
        case "Delete":
            file = open('todo.txt' , 'r')
            todos = file.readlines()
            file.close()
            if len(todos) != 0:
                for index , items in enumerate(todos):
                    print(f"{index}.{items}")
                option = int(input("Enter the item number to delete"))
                todos.pop(option)
                file = open('todo.txt' , 'w')
                file.writelines(todos)
                file.close()
            else:
                print("No item to delete")
        case "Replace":
            if len(todos) != 0:
                for index , items in enumerate(todos):
                    print(index , items)
                option = int(input("Enter the item number to be replace")) - 1
                newItem = input("Enter new item")
                todos[option] = newItem
        case "Exit":
            print("Thank you, have a nice day")
            break
