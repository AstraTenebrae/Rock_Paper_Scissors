import random

class ScoreBoard:
    def __init__(self):
        self.player_wins = 0
        self.bot_wins = 0
        self.draws = 0
    def upd(self, result):
        if result == 'You win':
            self.player_wins += 1
        elif result == 'I win':
            self.bot_wins += 1
        else:
            self.draws += 1
    def show(self):
        print(f"Let me remind you. I won {self.bot_wins} times and you won {self.player_wins} times. We had a draw {self.draws} times.")

    def save(self, filename = 'ScoreBoard.txt'):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f'Player has won {self.player_wins} times \n')
                file.write(f'Bot has won {self.bot_wins} times \n')
                file.write(f'Draws were recorded {self.draws} times \n')
        except IOError as e:
            print(f'Error was registered while saving a scoreboard file: {e}')

    def load(self, filename = 'ScoreBoard.txt'):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                arr = [file.readline().split()[3] for _ in range(3)]
                self.player_wins = int(arr[0])
                self.bot_wins = int(arr[1])
                self.draws = int(arr[2])
        except FileNotFoundError:
            pass

def bot_choice():
    choice = random.randint(1,3)
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    else:
        return 'scissors'
        
def player_choice():
    choice = input('Make a choice: "rock", "paper" or "scissors"? \n')
    if choice.lower() == 'exit':
        return 'exit'
    elif choice.lower() == 'show':
        return 'show'
    elif not choice.lower() in ('rock', 'paper', 'scissors'):
        print('Unknown answer. Please, try again.')
        return player_choice()
    else:
        return choice.lower()
        
def duel(bot, player):
    choices = ('rock', 'paper', 'scissors')              # Все возможные варианты выбора 
    counters = ('paper', 'scissors', 'rock')             # То, что может победить соответствующие вышеуказанные выборы
    if player == 'show':
        return 'show'
    elif player == 'exit':
        return 'exit'
    elif bot == player:
        return 'Draw'
    elif choices.index(bot) == counters.index(player):
        return 'You win'
    else:
        return 'I win'

        
def game():
    print("Hello, old friend! Let's play a game, shall we? If you don't want to, just say 'exit' any time.")
    scr = ScoreBoard()
    scr.load()
    while True:
        result = duel(bot_choice(), player_choice())
        if result == 'exit':
            print("I see, It's a shame... Well... Then, I'll see you next time.")
            scr.save()
            break
        elif result == 'show':
            scr.show()
        else:
            print(result)
            scr.upd(result)
    
    
    
game()