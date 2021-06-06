import random

wCheck=False
bCheck=False
#wPegs=0
#bPegs=0
answer=""
guess2=""

# def ans():
#     x=["r","o","y","g","b","p"]
#     answer=random.sample(x,4)
#     #prints as an array
#     print(answer)
#     return answer
# return answer


# def user():
#     guess=input("What is your guess? ie:r,p,g,b:")
#     #removes commas
#     guess2=guess.split(",")
#     print(guess2)
#     return guess2
# # return gu/ess2

def bCompare(guess2,answer):
    global bPegs
    for k in range(4):
        if guess2[k]== answer[k]:
            bCheck=True
            # print(bPegs)
            bPegs = bPegs + 1
            k=k+1
    return bPegs

def wCompare(guess2,answer):
    # global answer
    # global guess2
    # global wCheck
    global wPegs
    for i in answer:
        for color in guess2:
            if i == color:
                wCheck = True
                wPegs = wPegs + 1
    return wPegs
        # if wCheck == True and bCheck == False:
        #
        # if bCheck == True and wCheck == False:
        #
        # if bCheck == True and wCheck == True:
        #     wPegs = wPegs - 1

                # print(color+str(":")+str(wCheck))

# return wPegs
win = False
def pegs():
    global bPegs
    global wPegs
    global win
    wPegs = wPegs - bPegs
    if wPegs < 0:
        wPegs = 0

    print("The amount of black pegs is:"+ str(bPegs))
    print("The amount of white pegs is:"+ str(wPegs))
    if bPegs==4:
        win=True
        # print("pegs")
        # print(win)
    # return win
# def bCompare():
    # global answer
    # global guess2
    # global bCheck



# return bPegs
#
count = 0
def start():
    global wPegs
    global bPegs
    global count
    global win
    x = ["r", "o", "y", "g", "b", "p"]
    answer = random.sample(x, 4)
    while count < 3 or win == False:
        print("start",win)
        if win == False and count<3:
            count=count+1
        wPegs = 0
        bPegs = 0
        # prints as an array
        print(answer)
        guess = input("What is your guess? ie:r,p,g,b:")
        # removes commas
        guess2 = guess.split(",")
        print(guess2)
        bCompare(guess2, answer)
        wCompare(guess2, answer)
        pegs()
        if win==True:
            print("You Win!")
            count=11
    if win == False and count < 3:
        print("You Lose!")


start()