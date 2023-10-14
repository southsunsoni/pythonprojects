import random
def Game(playername):
        randomnumber=random.randrange(0,2)
        print('enter a number between 0 and 2')
        userentry=int(input())
        if(randomnumber==0):
           entry1='rock'
           if(userentry==0):
               entry2='rock'
               print(entry1+''+'='+''+entry2)
               print('no winner')
               Game(playername)
           elif(userentry==1):
               entry2='paper'
               print(entry1+''+'<'+''+entry2)
               print('the winner is '+''+playername)
               Game(playername)
           elif(userentry==2):
                entry2='sisors'
                print(entry1+''+'>'+''+entry2)
                print('the winner is valdez')
                Game(playername)
        if(randomnumber==1):
           entry1='paper'
           if(userentry==0):
               entry2='rock'
               print(entry1+''+'>'+''+entry2)
               print('the winner is valdez')
               Game(playername)
               
           elif(userentry==1):
               entry2='paper'
               print(entry1+''+'='+''+entry2)
               print('no winner')
               Game(playername)
           elif(userentry==2):
                entry2='sisors'
                print(entry1+''+'<'+''+entry2)
                print('the winner is valdez')
        if(randomnumber==2):
           entry1='sisors'
           if(userentry==0):
               entry2='rock'
               print(entry1+''+'<'+''+entry2)
               print('the winner is '+''+playername)
               Game(playername)
               
           elif(userentry==1):
               entry2='paper'
               print(entry1+''+'>'+''+entry2)
               print('the winner is valdez')
               Game(playername)
           elif(userentry==2):
                entry2='sisors'
                print(entry1+''+'='+''+entry2)
                print('no winner')

def Start():
    print('enter your name')
    playername=input()
    Game(playername)
    print('do you want to start a new game?')
    new=input()
    if(new=='y'):
            Start()
    elif(new=='n'):
        Game(playername)
    else:
            return 0
Start()
                
    