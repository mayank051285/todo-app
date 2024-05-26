def get_todos(filename="todo.txt"):
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_local, filename="todo.txt"):
    with open(filename, "w") as file_local:
        file_local.writelines(todos_local)


prompt = "Enter a option : Add, Show, Replace, Complete, Exit "

while True:
    user_input = input(prompt).title()

    if user_input.startswith("Add"):
        todos = get_todos("todo.txt")
        todo = user_input[4:] + "\n"
        todos.append(todo)
        write_todo(todos)

    elif user_input.startswith("Show"):
        todos = get_todos("todo.txt")
        new_todos = [item.strip("\n") for item in todos]
        for index, items in enumerate(new_todos):
            row = f"{index + 1}.{items}"
            print(row)

    elif user_input.startswith("Complete"):
        todos = get_todos("todo.txt")
        if len(todos) == 0:
            print("No more todos")
        else:
            option = int(user_input[9:]) - 1
            todos.pop(option)
            write_todo("todo.txt", todos)

    elif user_input.startswith("Replace"):
        todos = get_todos("todo.txt")
        new_todos = [item.strip("\n") for item in todos]
        if len(new_todos) == 0:
            print("No more todos")
        else:
            try:
                option = int(user_input[8:]) - 1
                newItem = input("Enter new item ")
                todos[option] = newItem + "\n"
                write_todo("todo.txt", todos)
            except ValueError:
                print(f"your command {user_input} is not valid")

    elif user_input.startswith("Exit"):
        print("Thank you, have a nice day")
        break
    else:
        print(f"{user_input} is not valid")
