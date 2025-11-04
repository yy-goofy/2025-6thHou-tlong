import turtle
import time
import random

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake 1v1 Battle by ChatGPT")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Score
score1 = 0
score2 = 0

# Player 1 - Green
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("lime")
p1.penup()
p1.goto(-100, 0)
p1.direction = "stop"
segments1 = []

# Player 2 - Blue
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("cyan")
p2.penup()
p2.goto(100, 0)
p2.direction = "stop"
segments2 = []

# Food for each player
food1 = turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.color("green")
food1.penup()
food1.goto(random.randint(-250, 250), random.randint(-250, 250))

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("blue")
food2.penup()
food2.goto(random.randint(-250, 250), random.randint(-250, 250))

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Green: 0  Blue: 0", align="center", font=("Courier", 24, "normal"))


# Movement controls
def p1_up():
    if p1.direction != "down":
        p1.direction = "up"


def p1_down():
    if p1.direction != "up":
        p1.direction = "down"


def p1_left():
    if p1.direction != "right":
        p1.direction = "left"


def p1_right():
    if p1.direction != "left":
        p1.direction = "right"


def p2_up():
    if p2.direction != "down":
        p2.direction = "up"


def p2_down():
    if p2.direction != "up":
        p2.direction = "down"


def p2_left():
    if p2.direction != "right":
        p2.direction = "left"


def p2_right():
    if p2.direction != "left":
        p2.direction = "right"


# Move snakes
def move(snake):
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    elif snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    elif snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    elif snake.direction == "right":
        snake.setx(snake.xcor() + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(p1_up, "w")
wn.onkeypress(p1_down, "s")
wn.onkeypress(p1_left, "a")
wn.onkeypress(p1_right, "d")

wn.onkeypress(p2_up, "Up")
wn.onkeypress(p2_down, "Down")
wn.onkeypress(p2_left, "Left")
wn.onkeypress(p2_right, "Right")


# Collision detection helper
def is_collision(a, b, size=20):
    return abs(a.xcor() - b.xcor()) < size and abs(a.ycor() - b.ycor()) < size


# Reset function
def reset_game(winner):
    global score1, score2
    time.sleep(1)
    p1.goto(-100, 0)
    p1.direction = "stop"
    p2.goto(100, 0)
    p2.direction = "stop"

    for seg in segments1:
        seg.goto(1000, 1000)
    for seg in segments2:
        seg.goto(1000, 1000)
    segments1.clear()
    segments2.clear()

    pen.clear()
    pen.write(f"Green: {score1}  Blue: {score2}", align="center", font=("Courier", 24, "normal"))

    print(f"🏁 {winner} wins this round!")


# Main game loop
while True:
    wn.update()

    # Check wall collisions
    if abs(p1.xcor()) > 330 or abs(p1.ycor()) > 330:
        score2 += 1
        reset_game("Blue")
    if abs(p2.xcor()) > 330 or abs(p2.ycor()) > 330:
        score1 += 1
        reset_game("Green")

    # Check food collision (Player 1)
    if is_collision(p1, food1):
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        food1.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lime")
        new_segment.penup()
        segments1.append(new_segment)

    # Check food collision (Player 2)
    if is_collision(p2, food2):
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        food2.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("cyan")
        new_segment.penup()
        segments2.append(new_segment)

    # Move segments (Player 1)
    for index in range(len(segments1) - 1, 0, -1):
        x = segments1[index - 1].xcor()
        y = segments1[index - 1].ycor()
        segments1[index].goto(x, y)
    if len(segments1) > 0:
        segments1[0].goto(p1.xcor(), p1.ycor())

    # Move segments (Player 2)
    for index in range(len(segments2) - 1, 0, -1):
        x = segments2[index - 1].xcor()
        y = segments2[index - 1].ycor()
        segments2[index].goto(x, y)
    if len(segments2) > 0:
        segments2[0].goto(p2.xcor(), p2.ycor())

    # Move snakes
    move(p1)
    move(p2)

    # Check collision between snakes
    if is_collision(p1, p2):
        score1 += 1
        score2 += 1
        reset_game("Both (head-on!)")

    # Self-collision (P1)
    for seg in segments1:
        if is_collision(p1, seg):
            score2 += 1
            reset_game("Blue")

    # Self-collision (P2)
    for seg in segments2:
        if is_collision(p2, seg):
            score1 += 1
            reset_game("Green")

    # Cross-collision (P1 hits P2’s body)
    for seg in segments2:
        if is_collision(p1, seg):
            score2 += 1
            reset_game("Blue")

    # Cross-collision (P2 hits P1’s body)
    for seg in segments1:
        if is_collision(p2, seg):
            score1 += 1
            reset_game("Green")

    time.sleep(delay)
