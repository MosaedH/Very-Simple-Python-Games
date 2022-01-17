import random
def play():
    user = input("What is you choisce?\n 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return f'It\'s a tie, Computer choice a \'{computer}\''

    # r > s, s > p, p > r
    if is_win(user, computer):
        return f'You won!, Computer choice a \'{computer}\''
    return f'You lost!, Computer choice a \'{computer}\''

def is_win(player, opponent):
    # return ture if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True
print(play())
