import random

money = 100

#function that simulates flipping a coin:
def flip_coin(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
 
    print("Let's start the game! Your guess is: + guess")
    num = random.randint(1, 2)
    if num == 1:
        return "Heads!"
    return "Tails!"

    if guess == flip:
        print("You won £" + str(bet))
        return bet
    print("Sorry, you lost £" + str(bet))
    return -bet

  
#function that simulates playing the game Cho-Han:
def cho_han(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    is_even = result % 2 == 0
    if is_even and guess == "Even":
        print("You won £" + str(bet))
        return bet
    elif not is_even and guess == "Odd":
        print("You won £" + str(bet))
        return bet
    else :   
        print("Sorry, you lost £" + str(bet))
        return -bet

#function that simulates two players picking a card randomly from a deck of cards:
def deck_of_cards(bet):
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0

    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4
    card_a = random.choice(cards)
    cards.remove(card_a)
    card_b = random.choice(cards)
    if card_a > card_b:
        print("You won £" + str(bet))
        return bet
    if card_a < card_b:
        print("Sorry, you lost £" + str(bet))
        return -bet
    if card_a == card_b:
        print("It is a tie!")
        return 0


#function that simulates some of the rules of Roulette:
def roulette(bet, guess):
    if bet <= 0:
        print("Your bet should be above 0.")
        return 0
        
    wheel_options = [str(x) for x in range(0, 37)] + ["00"]
    number = random.choice(wheel_options)
    is_even = int(number) % 2 == 0
    is_odd = not is_even
    
    print("The Roulette wheel will land on: " + number)

    if number == "00" or number == "0":
        print("Sorry, you lost £" + str(bet))
        return -bet
    if is_even and guess == "Even":
        print("You won £"  + str(bet))
        return bet
    if is_odd and guess == "Odd":
        print("You won £"  + str(bet))
        return bet
    if number == guess:
        print("You won big: £"  + str(bet))
        return bet * 36
    print("Sorry, you lost £" + str(bet))
    return -bet    
    


    
