import time
import random
import keyboard

def roll():
    return(random.randint(1,6))


def p1_name():
    return(input("enter the name of player 1:-"))
def p2_name():
    return(input("enter the name of player 2:-"))
def p3_name():
    return(input("enter the name of player 3:-"))
def p4_name():
    return(input("enter the name of player 4:-"))
player_names = set()

player_numbers=input("enter the number of players:-")
player_numbers=int(player_numbers)
if player_numbers >=2 :
    p1_name=p1_name()
    p2_name=p2_name()
    player_names.add(p1_name)
    player_names.add(p2_name)
if player_numbers >=3:
    p3_name=p3_name()
    player_names.add(p3_name)
    # print(p3_name)
if player_numbers==4:
    p4_name=p4_name()
    player_names.add(p4_name)
    # print(p4_name)
a=0
# print(p1_name,p2_name)
print("enter space bar each time to roll the dice")
while True:
    print(" ","Select your choice")
    print("1.roll dice(again)")
    print("2.exit")
    choice=int(input("enter the choice of number(1 or 2):-"))
    # print(choice,type(choice))
    if choice==1:
        print("error")
        for n in player_names:
            print(n,":- ",roll())
            
        time.sleep(3)
    if choice==2:
        break
print("The game is Over")
