class TodoModel:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]

    def get_todos(self):
        return self.todos