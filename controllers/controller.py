class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_todo_item(self):
        todo = self.view.prompt_for_todo()
        self.model.add_todo(todo)
        self.view.display_todos(self.model.get_todos())

    def remove_todo_item(self):
        index = self.view.prompt_for_removal()
        self.model.remove_todo(index)
        self.view.display_todos(self.model.get_todos())