import random


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
    elif not choice.lower() in ('rock', 'paper', 'scissors'):
        print('Unknown answer. Please, try again.')
        return player_choice()
    else:
        return choice.lower()
        
def duel(bot, player):
    choices = ('rock', 'paper', 'scissors')              # Все возможные варианты выбора 
    counters = ('paper', 'scissors', 'rock')             # То, что может победить соответствующие вышеуказанные выборы
    if bot == player:
        return 'Draw'
    elif choices.index(bot) == counters.index(player):
        return 'You win'
    elif player == 'exit':
        return 'exit'
    else:
        return 'I win'
        
def game():
    print("Hello, old friend! Let's play a game, shall we? If you don't want to, just say 'exit' any time.")
    while True:
        result = duel(bot_choice(), player_choice())
        if result == 'exit':
            print("I see, It's a shame... Well... Then, I'll see you next time.")
            break
        else:
            print(result)
    
    
    
game()