from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick, BRICKS
import time

X = -380
Y = 280

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT!")
screen.tracer(0)

paddle = Paddle((0, -280))


def create_bricks():
    global X, Y
    for _ in range(0,3):
        for _ in range(0, 20):
            Brick(x=X, y=Y)

            X += 40
        X = -380
        Y -= 20


score = Scoreboard()
LEVEL = score.level
game_over = False
balls_life = Scoreboard()
game_is_on = True
while game_over is False:
    create_bricks()
    brick_start = [(brick.xcor(),brick.ycor()) for brick in BRICKS]
    print(brick_start)
    ball = Ball()
    score = Scoreboard()

    while game_is_on:
        paddle.ondrag(paddle.goto)
        if paddle.ycor() > -280 or paddle.ycor() < -280:
            position = paddle.pos()
            x = position[0]
            y = position[1]
            y = -280
            paddle.goto(x,y)
        screen.update()
        ball.move()

        with open('score.txt', 'r') as game_memory:
            lines = game_memory.readlines()
            try:
                if LEVEL > int(lines[0]) or score.player_score > int(lines[1]):
                    print("testing")
                    with open('score.txt', 'w') as game_memory:
                        game_memory.write(f'{LEVEL}')
                        game_memory.write(f"\n{score.player_score}")
            except IndexError:
                with open('score.txt', 'w') as game_memory:
                    game_memory.write(f'{LEVEL}')
                    game_memory.write(f"\n{score.player_score}")
        if balls_life.ball_life == 0:
            game_over = True
        screen.listen()
        screen.onkey(paddle.move_right, "Right")
        screen.onkey(paddle.move_left, "Left")
        if balls_life.ball_life == 0:
            game_is_on = False

        #Detect collision with wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        #Detect collision with paddle
        if ball.distance(paddle) < 35:
            ball.bounce_y()
        #Detect collision with BRICKS
        for brick in BRICKS:
            if ball.distance(brick) < 30:
                ball.bounce_y()
                score.point()
                brick.goto(1000, 1000)
        #detect escape
        if ball.ycor() > 280:
            Y = 280
            create_bricks()
            LEVEL += 1
            time.sleep(5)
            score.reset_score()
            balls_life.reset_lifes()
            paddle.goto(0, -280)
            ball.reset_position()
        #detect ball out of bounds
        if ball.ycor() < -280:
            balls_life.loose_life()
            ball.reset_position()
            paddle.goto(0, -280)
            time.sleep(3)

if game_over == True:
    score.end_game()

screen.exitonclick()
