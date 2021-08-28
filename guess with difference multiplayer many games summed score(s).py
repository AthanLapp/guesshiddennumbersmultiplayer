import random
RANGE = int(input("give me the Supremum of the hidden number"))
GAMES = int(input("number of games"))
TOTALGAMES = GAMES
PLAYERS = int(input("Give me the number of players"))
FINALSCORE =[]
player = 1
for player in range(1, PLAYERS+1):
    FINALSCORE.append(0)
while GAMES > 0:
    print("Game no", TOTALGAMES-GAMES+1)
    PLAYER = []
    PLAYERGUESS = []
    PLAYERSCORE = []

    KEY = random.randint(1,RANGE)
    guess = KEY
    player = 1
    for player in range(1, PLAYERS+1):
        PLAYER.append(player)
        print("Guess player")
        guess = int(input(player))
        PLAYERGUESS.append(guess)
        PLAYERSCORE.append(abs(guess-KEY))

    print("Hidden number was",KEY)
    print("PLAYERNAMES",PLAYER)
    print("PLAYERGUSES",PLAYERGUESS)
    print("PLAYERSCORE",PLAYERSCORE)
    print("WINNERSCORE",min(PLAYERSCORE))
    for player in range(0, PLAYERS):
        FINALSCORE[player] = FINALSCORE[player] + PLAYERSCORE[player]
    print("SCORE UNTIL NOW:")
    print(FINALSCORE)
    GAMES-=1
    print("Games remaining:", GAMES)
print("FINALSCORE", FINALSCORE)
print("WINNER SCORE", min(FINALSCORE))
for player in range(0, PLAYERS):
    if min(FINALSCORE)==FINALSCORE[player]:
        print("PLAYER",player+1,"WINNER!!!")
        print("@->- .. ..^^.. .. -<-@")
    else:
        print("PLAYER", player+1,"LOOSER...")
        print("  :(((((((((((((((((((((( ")
print("That's all folks!!!")
end = input("Happy to See You!!! Untill next Time : ) ")

