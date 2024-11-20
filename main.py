from models.model import TodoModel
from views.view import TodoView
from controllers.controller import TodoController

def main():
    model = TodoModel()
    view = TodoView()
    controller = TodoController(model, view)

    while True:
        print("\n1. Add Todo\n2. Remove Todo\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            controller.add_todo_item()
        elif choice == '2':
            controller.remove_todo_item()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()