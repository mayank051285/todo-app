prompt = "Enter a option : Add, Show, Replace, Delete, Exit "
todos = []
while True:
    user_input = input(prompt).title()
    match user_input:
        case "Add":
            todo = input("Enter a TODO: ").title()
            todos.append(todo)
        case "Show":
            for index, items in enumerate(todos):
                row = f"{index+1}.{items}"
                print(row)
        case "Delete":
            if len(todos) != 0:
                for index, items in enumerate(todos):
                    print(f"{index}.{items}")
                option = input("Enter the item to delete").title()
                todos.remove(option)
            else:
                print("No item to delete")
        case "Replace":
            if len(todos) != 0:
                for index, items in enumerate(todos):
                    print(index, items)
                option = int(input("Enter the item number to be replace")) - 1
                newItem = input("Enter new item")
                todos[option] = newItem
        case "Exit":
            print("Thank you, have a nice day")
            break

