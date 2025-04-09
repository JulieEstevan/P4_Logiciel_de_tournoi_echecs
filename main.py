from controllers.menu_controller import MenuController
from utils.clear import clear_terminal


def main():

    menu_controller = MenuController()
    menu_controller.main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        print("\nScript interrompu par l'utilisateur.")
