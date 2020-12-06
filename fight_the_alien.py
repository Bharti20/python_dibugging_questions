from random import randint
alive = True
stamina = 10
def report(stamina):
    if stamina>8:
        print ("The alien is strong! It resists your pathetic attack!--")
    elif stamina>5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina>3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina>0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def fight(stam): # stamina
    while stam>0:
        response = input("Enter a move 1.Hit 2.Attack 3.Fight 4.Run--")
        if "Hit" in response or "Attack" in response:
            less = randint(0, stam)
            stam -= less
            report(stam)
        elif "Fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "Run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
    return False
print ("A threatening alien wants to fight you!.\n")
alive = fight(stamina)

if alive:
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n") 
