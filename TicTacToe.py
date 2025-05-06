import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ' '
    
    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please enter a valid name.")


class Menu:
    def display_menu(self):
        print("Welcome to Tic Tac Toe!")
        print("Choose your game mode:")
        print("1. Start game")
        print("2. quit game")
        choice = input("Enter your choice (1 or 2): ")
        
        while choice!= '1' and choice!= '2':
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice (1 or 2): ")
        
        return choice
    

    def display_end_game(self):
        print("Game Over!")
        print("Do you want to play again?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice (1 or 2): ")
        
        while choice!= '1' and choice!= '2':
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice (1 or 2): ")
        
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print("-"*17)
        for i in range(0, 9, 3):
            print(f" {self.board[i:i+3]}")
            if i < 6:
                print("-"*17)
        print("-"*17)
        
    
    def update_board(self, position, symbol):
        if 1 <= position <= 9:
            if self.board[position - 1].isdigit():
                self.board[position - 1] = symbol
                return True
        return False

    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.menu = Menu()
        self.board = Board()
        self.current_player = self.player1
    
    def start_game(self):
        choice = self.menu.display_menu()

        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.end_game()

    def setup_players(self):
        clear_screen()
        print("player 1, please choose your name and symbol.")
        self.player1.choose_name()
        self.player1.symbol = 'X'
        clear_screen()
        print("\nplayer 2, please choose your name and symbol.")
        self.player2.choose_name()
        self.player2.symbol = 'O'

    def play_game(self):
        while True:
            clear_screen()
            self.board.display_board()
            self.play_turn()
            if self.check_winner() or self.check_draw():
                choice = self.menu.display_end_game()
                if choice == '1':
                    self.restart_game()
                else:
                    self.end_game()
                    break
    

    def play_turn(self):
        Player = self.current_player
        print(f"\n{Player.name} ( {Player.symbol} ) , it's your turn. Choose a position (1-9): ")
        while True:
            try:
                position = int(input("choice a position (1 : 9):  "))
                if self.board.update_board(position, Player.symbol):
                  self.current_player = self.player1 if self.current_player == self.player2 else self.player2
                  break
                else:
                    print("Invalid position. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
    
    def check_winner(self):
        winning_combinations = [
          (0, 1, 2), (3, 4, 5), (6, 7, 8),  
          (0, 3, 6), (1, 4, 7), (2, 5, 8),  
          (0, 4, 8), (2, 4, 6) 
        ]
    
        for a, b, c in winning_combinations:
           if self.board.board[a] == self.board.board[b] == self.board.board[c]:  
              winner = self.player1 if self.board.board[a] == self.player1.symbol else self.player2
              print(f"\n🎉 {winner.name} ({winner.symbol}) wins! 🎉")  
              return True  

        return False  




    def check_draw(self):
        if all(not cell.isdigit() for cell in self.board.board):
            print("\nIt's a draw!")
            return True
    
    def restart_game(self):
        self.board.reset_board()
        self.current_player = self.player1
        clear_screen()
        print("Game restarted!")
        self.play_game()
    
    def end_game(self):
        print("Thank you for playing Tic Tac Toe!")


game = Game()
game.start_game()