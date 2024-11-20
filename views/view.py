class TodoView:
    def display_todos(self, todos):
        print("Todo List:")
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo}")

    def prompt_for_todo(self):
        return input("Enter a new todo: ")

    def prompt_for_removal(self):
        return int(input("Enter the number of the todo to remove: ")) - 1