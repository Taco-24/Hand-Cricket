import random

def toss():
    coin = ['H', 'T']
    while True:
        user_choice=input("Select H (heads) or T (tails): ")
        if user_choice.upper() not in coin:
            print("Invalid choice. Please choose H or T.")
        else:
            break
    coin_toss=random.choice(coin)
    if coin_toss==user_choice.upper():
        return True
    else:
        return False

def player_bat(c_score=0,second_inn=False):
    shot=[1,2,3,4,5,6]
    player_score=0
    while True:
        batsman_shot=int(input("Enter the shot number(1-6): "))
        if batsman_shot in shot:
            break
        else:
            print(f"Invalid choice ({batsman_shot}), Please choose between 1-6.")
    bowler_shot=random.choice(shot)
    print(f"Computer chose {bowler_shot}")
    while (batsman_shot!=bowler_shot):
        player_score+=batsman_shot
        if second_inn:
            if player_score>c_score:
                return player_score
        while True:
            batsman_shot = int(input("Enter the shot number(1-6): "))
            if batsman_shot in shot:
                break
            else:
                print(f"Invalid selection ({batsman_shot}), select a shot between 1-6.")
        bowler_shot = random.choice(shot)
        print(f"Computer chose {bowler_shot}")
    print(f"OUTT!\nThe score is {player_score}")
    return player_score

def computer_bat(p_score=0,second_inn=False):
    shot=[1,2,3,4,5,6]
    computer_score=0
    batsman_shot=random.choice(shot)
    while True:
        bowler_shot=int(input("Enter the shot number(1-6): "))
        if bowler_shot in shot:
            break
        else:
            print(f"Invalid choice ({bowler_shot}), Please choose between 1-6.")
    print(f"Computer chose {batsman_shot}")
    while (batsman_shot!=bowler_shot):
        computer_score+=batsman_shot
        if second_inn:
            if computer_score>p_score:
                return computer_score
        batsman_shot = random.choice(shot)
        while True:
            bowler_shot = int(input("Enter the shot number(1-6): "))
            if bowler_shot in shot:
                break
            else:
                print(f"Invalid selection ({bowler_shot}), select a shot between 1-6.")
        print(f"Computer chose {batsman_shot}")
    print(f"OUTT!\nThe score is {computer_score}")
    return computer_score

def result(player_score,computer_score):
    if player_score>computer_score:
        print(f"Congratulations, You WON!!!\nYour score: {p_score}, Computer's score: {c_score}")
    elif player_score==computer_score:
        print("Looks like its tie.")
    else:
        print(f"Oops, you LOST\nYour score: {p_score}, Computer's score: {c_score}\nBetter luck next time.")

game_status=input("Press any key to play or 0 to exit: ")
while (game_status!='0'):
    toss_result=toss()
    if toss_result:
        play_decision=input("Congrats!!,You won the toss\nDo you want to Bat or Bowl: ")
        if play_decision.lower()=='bat':
            print("You chose Batting, All the Best!!")
            p_score=player_bat()
            print("Time for Computer to bat.")
            c_score=computer_bat(p_score,True)
            result(p_score,c_score)
            game_status = input("Press any key to play again or 0 to exit: ")
            continue
        elif play_decision.lower()=='bowl':
            print("You chose Bowling, All the Best!!")
            c_score=computer_bat()
            print("Time for You to bat.")
            p_score = player_bat(c_score,True)
            result(p_score, c_score)
            game_status = input("Press any key to play again or 0 to exit: ")
            continue
    else:
        play_decision=random.choice(['bat','bowl'])
        if play_decision.lower()=='bowl':
            print("The computer chose Bowling, All the Best!!")
            p_score=player_bat()
            print("Time for Computer to bat.")
            c_score=computer_bat(p_score,True)
            result(p_score,c_score)
            game_status = input("Press any key to play again or 0 to exit: ")
            continue
        elif play_decision.lower()=='bat':
            print("The computer chose Batting, All the Best!!")
            c_score=computer_bat()
            print("Time for You to bat.")
            p_score = player_bat(c_score,True)
            result(p_score, c_score)
            game_status = input("Press any key to play again or 0 to exit: ")
            continue
input("Thank You for Playing\nPress Enter to Exit now.")


