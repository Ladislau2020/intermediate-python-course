
#The main fuction
def main():
    # importing the randon package to help us generating random numbers
    import random
    player = str(input('Say your name: '))
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))

    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Sucess')
        else:
            print(f'You rolled a {roll}')
    # print(f'You have rolled a total of {dice_sum}') i think i dont need this anymore
    player_total = f'{player} had  {dice_sum}'
    print(player_total)

if __name__== "__main__":
    main()












