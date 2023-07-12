import pickle


class TODO:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self):
        task = input("Task: ")
        self.tasks.append(task)

    def remove(self):
        self.show()
        print("Input the slot number. ('exit' to exit)")
        while True:
            input_value = input("Which task to remove : ")
            if input_value.lower() == "exit":
                break
            try:
                remove_index = int(input_value) - 1
                if remove_index < len(self.tasks):
                    del self.tasks[remove_index]
                    break
                else:
                    print(f"There is no task in the {remove_index + 1} slot.")
            except:
                print("Invalid input")
                continue

    def show(self):
        if self.tasks:
            for index, task in enumerate(self.tasks):
                print(f"{index+1}: {task}")
        else:
            print("Empty")


class WorkPlace:
    PATH = "WorkPlace.pkl"

    def __init__(self):
        self.todo_lists = []
        self._update_todo_names()

    def create(self, todo_name):
        todo = TODO(todo_name)
        self.todo_lists.append(todo)
        print(f"{todo.name} todo list has been created")
        self._update_todo_names()

    def delete(self, todo):
        ph = self.get_todo(todo)
        if ph:
            self.todo_lists.remove(ph)
            self._update_todo_names()

    def load(self):
        if self.todo_names:
            for index, todo in enumerate(self.todo_names):
                print(f"{index+1}: {todo}")
        else:
            print("Empty")

    def get_todo(self, todo):
        if todo in self.todo_names:
            i = self.todo_names.index(todo)
            return self.todo_lists[i]
        else:
            print(f"No todo list named {todo}")
            return None

    def _update_todo_names(self):
        self.todo_names = [todo.name for todo in self.todo_lists]
