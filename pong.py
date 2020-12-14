import random
import signal
import time
from turtle import Screen, Turtle


__author__ = "knmarvel"


running = True
counter = [0, 0]


def set_up_ball(ball):
    ball.hideturtle()
    ball.penup()
    ball.shape("circle")
    ball.setpos(-280, 0)
    ball.seth(0)
    ball.color("green")
    ball.showturtle()


def set_up_paddle(paddle, player):
    paddle.hideturtle()
    paddle.penup()
    paddle.shape("square")
    if(player):
        paddle.setpos(310, 30)
    else:
        paddle.setpos(-310, -30)
    paddle.shapesize(2,5)
    paddle.right(-90)
    paddle.color("green")
    paddle.showturtle()


def set_up_score(score):
    global counter
    score.hideturtle()
    score.penup()
    score.setpos(300, 300)
    score.color("green")
    score.pendown()
    score.write(f"{counter[0]} | {counter[1]} ")


def set_up_screen(s):
    s.title("Kano's Pong")
    s.bgcolor("black")


def move_things(s, ball, paddle, p2_paddle, score):
    global running
    global counter
    s.listen()
    ball.forward(5)
    time.sleep(.01)

    if ball.position()[1] > p2_paddle.position()[1] + 20 and ball.heading() in [x for x in (1, 85)]+[x for x in (275, 355)]:
        p2_paddle.forward(10)
    
    if ball.position()[1] < p2_paddle.position()[1] + 20 and ball.heading() in [x for x in (1, 85)]+[x for x in (275, 355)]:
        p2_paddle.backward(10)

    if ball.position()[0] >= 300:
        print("""ball hit right wall should go left""")
        new_heading = random.randrange(95, 265)
        ball.seth(new_heading)
    
    if ball.distance(paddle) < 30:
        """ball hit paddle, should go right"""
        new_heading = random.choice([x for x in (1, 85)]+[x for x in (275, 355)])
        ball.seth(new_heading)

    if ball.distance(p2_paddle) < 30:
        """ball hit paddle, should go left"""
        new_heading = random.randrange(95, 265)
        ball.seth(new_heading)

    if ball.position()[1] >= 300:
        print("""ball hit top wall""")
        if ball.heading() <= 90.0:
            print("""ball heading right""")
            new_heading = random.randrange(275, 355)
            ball.seth(new_heading)

        else:
            print("""ball heading left""")
            new_heading = random.randrange(185, 265)
            ball.seth(new_heading)

    if ball.position()[1] <= -300:
        print("""ball hit bottom wall""")
        if ball.heading() >= 270.0:
            print("""ball heading right""")
            new_heading = random.randrange(5,85)
            ball.seth(new_heading)

        else:
            print("""ball heading left""")
            new_heading = random.randrange(95, 175)
            ball.seth(new_heading)

    if ball.position()[0] <= -301:
        score.clear()
        counter[1]+= 1
        score.write(f"{counter[0]} | {counter[1]} ")
        set_up_ball(ball)

    if ball.position()[0] >= 301:
        score.clear()
        counter[0]+= 1
        score.write(f"{counter[0]} | {counter[1]} ")
        set_up_ball(ball)


def main():
    global running

    print(f"HELLO. PROGRAM STARTED AT {time.ctime()}")
    ball = Turtle()
    paddle = Turtle()
    score = Turtle()
    p2_paddle = Turtle()
    s = Screen()
    set_up_ball(ball)
    set_up_paddle(paddle, 0)
    set_up_paddle(p2_paddle, 1)
    set_up_score(score)
    set_up_screen(s)

    def paddle_move_up():
        if paddle.position()[1] < 300:
            paddle.forward(40)

    def paddle_move_down():
        if paddle.position()[1] > -300:
            paddle.backward(40)

    s.onkey(paddle_move_up, "Up")
    s.onkey(paddle_move_down, "Down")

    while running:
        move_things(s, ball, paddle, p2_paddle, score)

    ball.hideturtle()        
    ball.setpos(0,0)
    ball.pendown()
    ball.write("you lose")
    s.exitonclick()


if __name__ == "__main__":
    #autorun when run as script
    main()