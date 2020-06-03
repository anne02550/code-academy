import random

money = 100

#Write your game of chance functions here
# num = random.randint(1, 10)

def flip_coin():
    num = random.randint(1, 2)
    if num == 1:
        return "heads"
    return "tails"

def bet_on_coin_flip(guess, bet):
    flip = flip_coin()
    if guess == flip:
        return bet
    return -bet

def roll_dice(Odd, Even):
    pass   
#Call your game of chance functions here
def cho_han(guess, bet):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    is_even = result % 2 == 0
    if is_even and guess == "Even":
        return bet
    elif not is_even and guess == "Odd":
        return bet
    else :   
        return -bet

def deck_of_cards(bet):
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4
    card_a = random.choice(cards)
    cards.remove(card_a)
    card_b = random.choice(cards)
    if card_a > card_b:
        return bet
    if card_a < card_b:
        return -bet
    if card_a == card_b:
        return 0

def roulette(bet, guess):
    wheel_options = [str(x) for x in range(0, 37)] + ["00"]
    number = random.choice(wheel_options)
    is_even = int(number) % 2 == 0
    is_odd = not is_even
    
    print("the Roulette wheel will land on " + number)

    if number == "00" or number == "0":
        print("Sorry, you lose")
        return -bet
    if is_even and guess == "Even":
        print("you win")
        return bet
    if is_odd and guess == "Odd":
        print("you win")
        return bet
    if number == guess:
        print("you win big")
        return bet * 36
    print("Sorry, you lose")
    return -bet    
    


    
