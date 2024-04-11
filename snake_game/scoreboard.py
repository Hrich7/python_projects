from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.update_scoreboard()
       
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()