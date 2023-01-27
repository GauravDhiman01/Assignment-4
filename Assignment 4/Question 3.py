from random import randint
play=10
while play>0:
    x=randint(1,10)
    y=randint(1,10)
    print("What is ",x," multiplied by ",y)
    a=int(input("Answer:"))
    if a==x*y:
        print("Correct Answer")
    else:
        print("The entered answer is incorrect, the correct answer is ",x*y)
    play=play-1
print("Thanks for playing the Game, Hope you had fun.")