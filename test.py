import turtle
from math import pi, sin, cos
import pygame # type: ignore

# Initialize Pygame and the mixer module for playing music
pygame.mixer.init()

# Load the music file with a corrected path
pygame.mixer.music.load(r"c:\Users\CLienT\Downloads\Rihanna-Kiss-It-Better-Instrumental-Prod.-By-Glass-John-Kuk-Harrell-Jeff-Bhasker.mp3")

# Set volume (optional)
pygame.mixer.music.set_volume(0.5)

# Start playing the background music
pygame.mixer.music.play(-1)  # The -1 means the music will loop indefinitely

def draw_heart(w, h, iteration=0):
    if iteration >= len(colors):
        return
    
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2.5)
    a = 0
    t.up()
    t.fillcolor(colors[iteration])
    t.begin_fill()
    while a < 2 * pi:
        x = w * (16 * sin(a) ** 3)
        y = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a))
        t.goto(x, y)
        a += 0.02
        t.down()
    t.end_fill()

    draw_heart(w - 3, h - 2, iteration + 1)

    # Draw Text 
    if iteration == len(colors) - 1:  # Only draw text in the last iteration 
        t.up()
        t.color("white")
        t.setpos(0, 0)
        t.write("dsadasdas", align="center", font=("verdana", 15, "bold"))
        t.down()

colors = ('#d90166', 'purple', 'blue') # add more colors if you want 

# Set up the screen 
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("ihhh")

# Draw heart
draw_heart(16, 16)

# Keep the window open
turtle.done()
pygame.done()
