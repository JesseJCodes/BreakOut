from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.ball_life = 4
        self.level = 1
        # self.update_scoreboard()
        # self.update_lifeboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 0)
        self.write(self.player_score, align="right", font=("Courier", 40, "normal"))
    def update_lifeboard(self):
        self.clear()
        self.write(f"Balls left:{self.ball_life}", align="center", font=("Courier", 40, "normal"))
        self.goto(100, 0)


    def end_game(self):
        self.goto(0, 100)
        self.clear()
        with open('score.txt',"r") as file:
            lev = file.readlines()
        self.write(f"Highest Level reached:{lev[0]}\n"
                   f"High Score:{lev[1]}", align="center", font=("Courier", 40, "normal"))
    def reset_score(self):
        self.clear()
        self.player_score = 0

    def reset_lifes(self):
        self.clear()
        self.ball_life = 4

    def point(self):
        self.player_score += 1
        self.update_scoreboard()

    def loose_life(self):
        self.ball_life -= 1
        self.update_lifeboard()


