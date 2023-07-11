from json import load, dump

DEFAULT_FORMAT = {"list": []}


class TODO:
    def __init__(self, path):
        self.path = path
        self._create()
        self.to_do_list = self._get_list()

    def add(self):
        task = input("Task: ")
        self.to_do_list.append(task)
        self._update_list()

    def load(self):
        for index, todo in enumerate(self.to_do_list):
            print(f"{index+1}: {todo}")

    def remove(self):
        self.load()
        print("Input the slot number. ('BACK' to exit)")
        while True:
            input_value = input("Which task to remove : ")
            if input_value.upper() == "BACK":
                break
            try:
                remove_index = int(input_value) - 1
                if remove_index < len(self.to_do_list):
                    del self.to_do_list[remove_index]
                    self._update_list()
                    break
                else:
                    print(f"There is no text in the {remove_index + 1} slot.")
            except:
                print("Invalid input")
                continue

    def _get_list(self):
        with open(self.path, "r") as file:
            return load(file)["list"]

    def _update_list(self):
        with open(self.path, "w") as file:
            todo_dict = {"list": self.to_do_list}
            dump(todo_dict, file)

    def _create(self):
        with open(self.path, "w") as file:
            dump(DEFAULT_FORMAT, file)