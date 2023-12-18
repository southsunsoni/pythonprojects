import random

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
    def Move_to_coordinates(self):
        pass
        
class point():
    def __init__(self,x_coordinate,y_coordinate) -> None:
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
    
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
            Player.Navigate_player()
            if Player.x_coordinate==Point.x_coordinate and Player.y_coordinate==Point.y_coordinate:
                print('hi')
main()