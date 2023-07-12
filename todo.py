import pickle
from sys import argv, exit
from todo_object import WorkPlace


def error_msg():
    print("Type 'help' to get commands")


def start():
    try:
        with open(WorkPlace.PATH, "rb") as file:
            ph_workplace = pickle.load(file)
            if not ph_workplace:
                return WorkPlace()
            else:
                return ph_workplace
    except:
        return WorkPlace()


def save(wp):
    with open(WorkPlace.PATH, "wb") as file:
        pickle.dump(wp, file)


commands = {
    "help": "Gives the list of commands",
    "reset": "Delete every Todo list",
    "list": "Gives the list of todo lists",
    "create": "Create a Todo list with 'create {name of todo}'",
    "delete": "Delete a Todo list with 'delete {name of todo}'",
    "add": "Add task in a Todo list with 'add {name of todo}'",
    "remove": "Remove a task from Todo list with 'remove {name of todo}'",
    "show": "Get the list of Tasks of a Todo list with 'show {name of todo}'",
}

user_input = argv[1:]

if __name__ == "__main__":
    work_place = start()

    if len(user_input) > 2 or len(user_input) < 1:
        error_msg()

    else:
        command = user_input[0]

        if command not in commands:
            print(f"No command named '{command}'")
            error_msg()

        elif command == "help":
            for command_name, information in commands.items():
                print(f"{command_name} : {information}")

        elif command == "list":
            work_place.load()

        elif command == "reset":
            save([])
            print("Reset complete")
            exit()

        elif len(user_input) < 2:
            print("Missing argument")
            error_msg()

        else:
            name = user_input[1]

            if command == "create":
                work_place.create(name)

            elif command == "delete":
                work_place.delete(name)

            elif command == "add":
                todo = work_place.get_todo(name)
                if todo:
                    todo.add()

            elif command == "remove":
                todo = work_place.get_todo(name)
                if todo:
                    todo.remove()

            elif command == "show":
                todo = work_place.get_todo(name)
                if todo:
                    todo.show()

            else:
                error_msg()

        save(work_place)
