#from functions import get_todos,write_todo
import functions

""" The get todos and write todo is written into functions.py file
"""
prompt = "Enter a option : Add, Show, Replace, Complete, Exit "
import time

now = time.strftime("%d %m,%Y %H:%M:%S")
print("It is", now)
while True:
    user_input = input(prompt).title()

    if user_input.startswith("Add"):
        todos = functions.get_todos()
        todo = user_input[4:] + "\n"
        todos.append(todo)
        functions.write_todo(todos)

    elif user_input.startswith("Show"):
        todos = functions.get_todos()
        new_todos = [item.strip("\n") for item in todos]
        for index, items in enumerate(new_todos):
            row = f"{index + 1}.{items}"
            print(row)

    elif user_input.startswith("Complete"):
        todos = functions.get_todos()
        if len(todos) == 0:
            print("No more todos")
        else:
            option = int(user_input[9:]) - 1
            todos.pop(option)
            functions.write_todo(todos)

    elif user_input.startswith("Replace"):
        todos = functions.get_todos()
        new_todos = [item.strip("\n") for item in todos]
        if len(new_todos) == 0:
            print("No more todos")
        else:
            try:
                option = int(user_input[8:]) - 1
                newItem = input("Enter new item ")
                todos[option] = newItem + "\n"
                functions.write_todo(todos)
            except ValueError:
                print(f"your command {user_input} is not valid")

    elif user_input.startswith("Exit"):
        print("Thank you, have a nice day")
        break
    else:
        print(f"{user_input} is not valid")
