import turtle

# Setup the game window
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Stops automatic window updates

# Paddle 1 (Left)
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=6, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2 (Right)
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=6, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball movement speed (x-axis)
ball.dy = -0.2  # Ball movement speed (y-axis)

# Paddle Movement Functions
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        paddle_1.sety(y + 20)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -240:
        paddle_1.sety(y - 20)

def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        paddle_2.sety(y + 20)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > -240:
        paddle_2.sety(y - 20)

# Keyboard Controls
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# Main Game Loop
while True:
    win.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Collision with Walls
    if ball.ycor() > 290:  # Top Wall
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    if ball.ycor() < -290:  # Bottom Wall
        ball.sety(-290)
        ball.dy *= -1  # Reverse direction

    # Ball Collision with Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Reverse direction

    # Ball Collision with Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Reverse direction

    # Ball Out of Bounds (Reset)
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  # Reset ball direction
