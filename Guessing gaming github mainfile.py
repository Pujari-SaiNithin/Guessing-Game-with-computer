import random
while True:
    print("*** WELCOME TO THE GAME ***")
    start_num=int(input(" *** PRESS 0 THE GAME : "))
    if start_num==0:
        print("***YOU ARE READY TO START THE GAME***")
        a=1
        score=0
        while a<=3:
            guess_number=int(input("ENTER A NUMBER YOU GUESSED: "))
            computer_number=random.randint(1,9)
            print("THE NUMBER GUESSED BY THE COMPUTER ",computer_number)
            if guess_number==computer_number:
                print("YOU HAVE ENTERED A CORRECT NUMBER")
                score=score+1
                break
            elif a<3:
                print("YOU HAVE ANOTHER CHANCE")
            else:
                print("YOU HAVE REACHED THE MAXIMUM CHANCE LIMIT: ")
            a=a+1
        print("THE TOTAL SCORE YOU HAVE SCORED IS: ",score)
    else:
        print("CHECK THE STRING YOU HAVE ENTERED: ")
    
