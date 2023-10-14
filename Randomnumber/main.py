import random
Randomenumber=random.randrange(1,100)
def update():
    return random.randrange(1,100)
def randomgen(Randomenumber):
    print('enter a number between 1 to 100')
    enteredNumber=int(input())
    if(Randomenumber==enteredNumber):
         print('you guest it write')
         print('do you want to play again?')
         answer=input()
         if(answer=='y'):
             Randomenumber=update()
             randomgen(Randomenumber)
         elif(answer=='n'):
             print('main menu')
         
    elif(Randomenumber==''):
        print('you didnt enter any value ')
        print(Randomenumber)
    elif(Randomenumber>enteredNumber):
         print('the number you entered is too big try again below')
         print(Randomenumber)
         randomgen(Randomenumber)
    else:
         print('the number you entered is too small try again above')
         print(Randomenumber)
         randomgen(Randomenumber)
randomgen(Randomenumber)
   