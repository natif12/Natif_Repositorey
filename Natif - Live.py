def welcome(name):
    return "Hello " + name + " and welcome to the World of Games, Here you can find many cool games to play"


def load_game():
    num_game = input(
        "Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n 2. Guess Game - guess a number and see if you chose like the computer \n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while int(num_game) < 1 or int(num_game) > 4:
        print("please enter valid game number ")
        num_game = input(
            "Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n 2. Guess Game - guess a number and see if you chose like the computer \n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    dif_game = input("Please choose game difficulty from 1 to 5:")
    while int(dif_game) < 1 or int(dif_game) > 6:
        print("please enter valid difficulty number ")
        dif_game = input("Please choose game difficulty from 1 to 5:")


