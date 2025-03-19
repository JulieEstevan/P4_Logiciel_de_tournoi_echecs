from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from utils.clear import clear_terminal

class MenuController:

    def __init__(self):
        
        self.view = MenuView()

    def player_menu(self):

        controller = PlayerController()

        while True:
            self.view.display_player_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                controller.add_player()
            elif choice == "2":
                clear_terminal()
                controller.display_players_list()
            elif choice == "3":
                clear_terminal()
                break
            else:
                self.view.display_invalid_choice()

    def tournament_menu(self):

        # In developpment
        pass

    def report_menu(self):

        # In developpment
        pass
            
    def main_menu(self):

        clear_terminal()

        while True:
            self.view.display_main_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                self.player_menu()
            elif choice == "4":
                self.view.display_goodbye()
                break
            else:
                clear_terminal()
                print("En construction")