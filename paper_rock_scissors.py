import random

playerscore = 0
cpuscore = 0
game_active = True

while game_active == True:
    if playerscore == 3:
        print(f"""===========================================
-    PLAYER WINS!                         -
-                                         -
-    Player got {playerscore} points.                 -
-    CPU got {cpuscore} points.                    -
-                                         -
-    Thanks for playing!                  -
===========================================
        """)
        game_active = False
    elif cpuscore == 3:
        print(f"""===========================================
-    CPU WINS!                            -
-                                         -
-    CPU got {cpuscore} points.                    -
-    Player got {playerscore} points.                 -
-                                         -
-    Thanks for playing!                  -
===========================================
        """)
        game_active = False
    else:
        while 1==1:
            playerchoice = input("Rock, paper or scissors? ").upper()
            if playerchoice == "ROCK":
                break
            elif playerchoice == "PAPER":
                break
            elif playerchoice == "SCISSORS":
                break
            else:
                print("Invalid input.")

        cpuchoiceid = random.randint(1,3)
        if cpuchoiceid == 1:
            cpuchoice = "ROCK"
        elif cpuchoiceid == 2:
            cpuchoice = "PAPER"
        elif cpuchoiceid == 3:
            cpuchoice = "SCISSORS"

        print("")
        print("You chose: " + playerchoice)
        print("CPU chose: " + cpuchoice)

        if (cpuchoice == "ROCK" and playerchoice == "ROCK") or (cpuchoice == "PAPER" and playerchoice == "PAPER") or (cpuchoice == "SCISSORS" and playerchoice == "SCISSORS"):
            print(f"""
            Draw! Nobody gets a point.
            
            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)

        elif (cpuchoice == "ROCK" and playerchoice == "PAPER"):
            playerscore = playerscore + 1
            print(f"""
            Paper beats rock! You got a point!
                
            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)
        elif (cpuchoice == "PAPER" and playerchoice == "ROCK"):
            cpuscore = cpuscore + 1
            print(f"""
            Paper beats rock! CPU got a point!

            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)

        elif (cpuchoice == "SCISSORS" and playerchoice == "ROCK"):
            playerscore = playerscore + 1
            print(f"""
            Rock beats scissors! You got a point!
    
            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)

        elif (cpuchoice == "ROCK" and playerchoice == "SCISSORS"):
            cpuscore = cpuscore + 1
            print(f"""
            Rock beats scissors! CPU got a point!

            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)

        elif (cpuchoice == "PAPER" and playerchoice == "SCISSORS"):
            playerscore = playerscore + 1
            print(f"""
            Scissors beats paper! You got a point!

            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)

        elif (cpuchoice == "SCISSORS" and playerchoice == "PAPER"):
            cpuscore = cpuscore + 1
            print(f"""
            Scissors beats paper! CPU got a point!

            You need {3 - playerscore} points to win.
            CPU needs {3 - cpuscore} points to win.
            """)