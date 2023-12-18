import random
class DevineLeNumbre:
    def __init__(self) :
        self.nombre_a_deviner=random.randint(1,100)
        self.nombre_max_dessais=3
        self.indication=''
class player:
    def __init__(self) :
        self.name=''
        self.age=''
        self.entrer=''
        self.nombre_de_win=0
        
def main():
    
    for i in range (3):
        print('do you want to start a new parti?')
        answer=input()
        if answer=='yes':
            player1=player()
            jeux=DevineLeNumbre()
            print('enter your name')
            player1.name=input()
            print('enter your age')
            player1.age=int(input())
            print(player1.name,'enter a number')
            player1.entrer=int(input())
            jeux.entrer=player1.entrer
            if jeux.nombre_a_deviner==player1.entrer:
                print('the number you entered is correct')
                jeux.indication='zero error'
                jeux.nombre_max_dessais=jeux.nombre_max_dessais
            elif jeux.nombre_a_deviner!=player1.entrer:
                print('the number you entered is incorrect')
                if player1.entrer>jeux.nombre_a_deviner:
                    jeux.indication='the number is less'
                    print(jeux.indication)
                    if jeux.indication=='the number is less':
                        jeux.nombre_max_dessais-=1
                        print(jeux.nombre_max_dessais)
                elif player1.entrer<jeux.nombre_a_deviner:
                    jeux.indication='the number is greath'
                    print(jeux.indication)
                    if jeux.indication=='the number is greath':
                        jeux.nombre_max_dessais-=1
                        print(jeux.nombre_max_dessais)
            if jeux.nombre_max_dessais==0:
                print('your party is finished')
        elif answer=='no':
            pass
    i+=1
main()