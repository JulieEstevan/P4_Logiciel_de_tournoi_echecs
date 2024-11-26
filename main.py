from controllers.PlayerController import PlayerController

def main():
    controller = PlayerController()

    while True:
        print("\n1. Create Player\n2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            controller.create_player()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()