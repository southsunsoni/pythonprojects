import random
import UI as ui
class player():
    def __init__(self,name) -> None:
        self.name=name
        self.score=0
        self.x_coordinate=0
        self.y_coordinate=0
    def Navigate_player(self):
        Anforderung_zu_nutzer=f"{self.name} enter the x-coordinate "
        print(Anforderung_zu_nutzer)
        self.x_coordinate=int(input())
        Anforderung_zu_nutzer=f"{self.name} enter the y-coordinate "
        print(Anforderung_zu_nutzer)
        self.y_coordinate=int(input()) 
class point():
    def __init__(self,x_coordinate,y_coordinate) -> None:
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
def trial():
    ui.cardre_jeux.configure(text="my name")
def screen(var):
    print(var)

    
def main():
    print("Do you want to start a party?")
    answer=input()
    if answer=='y':
        print("Enter your name")
        Player=player(input())
        while True:
            Point= point(random.randrange(1,100),random.randrange(1,100))
            cartecian_coordinates=f"x:{Point.x_coordinate},y:{Point.y_coordinate}"
            print(cartecian_coordinates)
            value=f"{Player.name}:{Player.score}"
            print(value)
            Player.Navigate_player()
            if Player.x_coordinate==Point.x_coordinate and Player.y_coordinate==Point.y_coordinate:
                Player.score+=1
                
                
            else:
                while Player.x_coordinate!=Point.x_coordinate or Player.y_coordinate!=Point.y_coordinate:
                    cartecian_coordinates=f"x:{Point.x_coordinate},y:{Point.y_coordinate}"
                    print(cartecian_coordinates)
                    print(value)
                    Player.Navigate_player()
                    if Player.x_coordinate==Point.x_coordinate and Player.y_coordinate==Point.y_coordinate:
                        Player.score+=1
            if Player.score==3:
                main()       
                    
main()