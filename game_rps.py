# Day 3
"""
Make a game of rock, paper scissors against the computer. 
Algorithm
    Tell user to enter either rock,paper or scissors
    Get the response
    Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
    Compare user selection and computer selection
    Display who wins.

Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    Make an enumerated variable type to store choices.
"""

#initializing Scores & Game Choices
pc_score=0
user_score=0
game_choices=[]
#Asking User to set number of times he/she would like to play
set_ip = (input("Enter How many times would you like to play : "))
#Validating User Entry
while set_ip.isdigit() is False:
    print('Please enter a Valid Entry')
    set_ip = input("Enter How many times would you like to play : ")
#type-casting user entry to integer
set = int(set_ip)
"""
Rules of Game:
rock(1)>scissor(3)
paper(2)>rock(1)
scissor(3)>paper(2)
"""
#defining the function to print Scoreboard
def score(a,b):
    print('{:^20s}'.format('Score Board'))
    print('{:^10s}:{:^10d}'.format("PC",a))
    print('{:^10s}:{:^10d}'.format("You",b))
#defining game function to use it for multiple times
def game():
    from random import randint
    ip_dict = {"ROCK":1,
                "PAPER":2,
                "SCISSOR":3}#dictinary to understarnd input 
    #Asking User Input & Validating it
    ip  = input('Enter any one "ROCK" or "PAPER" or "SCISSOR": ').upper()
    while(True):
        if ip not in ip_dict.keys():
            print('Please enter a Valid Entry')
            ip  = input('Enter any one "ROCK" or "PAPER" or "SCISSOR": ').upper()
        else:
            break
    cmp  = randint(1,3)#random draw from 1 to 3
    pc_score=0
    user_score=0
    def kvcmp():#defining function to get key of what pc randomly drew
        for k, v in ip_dict.items():
            if v == cmp:
                return k
    kmp = kvcmp()#getting key of what pc randomly drew
    
    if ip_dict[ip] == cmp:#draw condition
        print('Both PC and Player drew {:s}\nso it\'s a draw.'.format(ip))
        pc_score+=1
        user_score+=1
    elif ip_dict[ip] == 1:
        if cmp==2:#rock vs paper
            print('PC drew {:s}\nso you Lose.'.format(kmp))
            pc_score+=1
        elif cmp==3:#rock vs scissor
            print('PC drew {:s}\nso you Win.'.format(kmp))
            user_score+=1
    elif ip_dict[ip] == 2:
        if cmp==3:#paper vs scissor
            print('PC drew {:s}\nso you Lose.'.format(kmp))
            pc_score+=1
        elif cmp==1:#paper vs rock
            print('PC drew {:s}\nso you Win.'.format(kmp))
            user_score+=1
    elif ip_dict[ip] == 3:
         if cmp==1:#scissor vs rock
             print('PC drew {:s}\nso you Lose.'.format(kmp))
             pc_score+=1
         elif cmp==2:#scissor vs paper
             print('PC drew {:s}\nso you Win.'.format(kmp))
             user_score+=1
    print('\n{:^20s}'.format('Current Score'))
    #returning score-board and user& PC draws
    return (pc_score,user_score,(ip,kmp))
#to play game multiple times
for x in range(set):
    scores = game()
    #making game board consistent
    pc_score+=scores[0]
    user_score+=scores[1]
    #saving user & PC draws into a list
    game_choices.append(scores[2])
    score(pc_score,user_score)
#Final Score
print('\n\n{:^20s}'.format('Final Score'))
score(pc_score,user_score)
#Final Winner Announcemnent
if pc_score>user_score:
    print('Final Result\nPC Won')
elif user_score>pc_score:
    print('Final Result\nYou Won')
else:
    print('Final Result\nIt\'s a Draw')
#printing all User & input Draws
print('Below are all the Draws that \nuser & PC drew while in Game')
print('_'*35)
print('|{:^7s}|{:^12s}|{:^12s}|'.format("Choice","User Draw","PC Draw"))
for x,y in enumerate(game_choices):
    print('|{:<7d}|{:^12s}|{:^12s}|'.format(x,y[0],y[1]))