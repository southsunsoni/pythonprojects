import random
class player:
    def __init__(self,name):
        self.name=name
        elements=['rock','paper','sisors']
        self.elements=elements
def start():
    print('do you want to start a game?')
    start=input()
    if(start=='y'):
        print('enter the name of player1')
        player1=player(input())
        print('enter the name of player2')
        player2=player(input())
    #asking the players to play
    for  i in range(1,6):
        print('Round'+''+str(i))
        player1_play=random.sample(player1.elements,1)
        player2_play=random.sample(player2.elements,1)
        #print(player1.name+'   '+player2.name)
        print(str(player1_play)+''+str(player2_play))
        if(str(player1_play)==str(player2_play)):
            print('no winner play again')
        if(str(player1_play)!=str(player2_play)):
            if(str(player1_play)==['rock'] and str(player2_play)==['sisors']):
                   print(player1.name+''+'winn '+'round'+''+str(i))
            if(str(player2_play)==['rock'] and str(player1_play)==['sisors']):
                   print(player2.name+''+'winn '+'round'+''+str(i))
            if(str(player1_play)==['rock'] and str(player2_play)==['paper']):
                   print(player2.name+''+'winn '+'round'+''+str(i))
            elif(str(player2_play)=='rock' and str(player1_play)=='paper'):
                   print(player1.name+''+'winn '+'round'+''+str(i))
            elif(str(player1_play)=='sisors' and str(player2_play)=='paper'):
                   print(player1.name+''+'winn '+'round'+''+str(i))
            elif(str(player2_play)=='sisors' and str(player1_play)=='paper'):
                   print(player2.name+''+'winn '+'round'+''+str(i))    
             
            
            
    
    
start()  