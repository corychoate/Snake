import turtle
import time
import random

# Time delay for game speed
game_speed = 0.1

# Score tracking
current_points = 0
top_score = 0

# Set up the game screen
game_window = turtle.Screen()
game_window.title("Snake Game by @CodeArt")
game_window.bgcolor("black")  # Changed background color to dark gray
game_window.setup(width=600, height=600)
game_window.tracer(0)  # Turn off screen updates

# Snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("blue")  # Changed snake head color to blue
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# Snake food
snake_food_list = []
for _ in range(10):  # Changed to generate 10 apples
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)
    snake_food_list.append(food)

snake_segments = []

# Pen for score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, -280)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to handle snake movement
def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# Keyboard bindings for movement
game_window.listen()
game_window.onkeypress(move_up, "w")
game_window.onkeypress(move_down, "s")
game_window.onkeypress(move_left, "a")
game_window.onkeypress(move_right, "d")

# Main game loop
while True:
    game_window.update()

    # Check for collision with the game border
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"

        # Hide the segments
        for segment in snake_segments:
            segment.goto(1000, 1000)

        snake_segments.clear()

        # Reset the score and delay
        current_points = 0
        game_speed = 0.1

        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(current_points, top_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    for food in snake_food_list:
        if snake_head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")  # Changed snake segment color to white
            new_segment.penup()
            snake_segments.append(new_segment)

            game_speed -= 0.001

            current_points += 10

            if current_points > top_score:
                top_score = current_points

            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(current_points, top_score), align="center", font=("Courier", 24, "normal"))

    # Move the snake segments
    for index in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[index - 1].xcor()
        y = snake_segments[index - 1].ycor()
        snake_segments[index].goto(x, y)

    if len(snake_segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_segments[0].goto(x, y)

    move()

    # Check for collision with the snake body
    for segment in snake_segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"

            for segment in snake_segments:
                segment.goto(1000, 1000)

            snake_segments.clear()

            current_points = 0
            game_speed = 0.1

            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(current_points, top_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(game_speed)

game_window.mainloop()
