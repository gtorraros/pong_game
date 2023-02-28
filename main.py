#How would I breakdown the pong game?

# 1. Screen & Separation.
# 2. Scoreboard.
# 3. Ball.
# 4. Racket.
# 5. Ball behaviour when getting to top or bottom wall.
# 6. Ball behaviour when getting to racket.
# 7. Ball behaviour when getting to right or left wall.

#How would Angela breakdown the pong game?
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move.
# 5. Detect collision with wall and bounce.
# 6. Detect collision with paddle.
# 7. Detect when paddle misses.
# 8. Keep score.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

















screen.exitonclick()