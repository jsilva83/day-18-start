# from turtle import Turtle
# from turtle import Screen
import turtle as tu
import random as rnd
import walker as wlk

cursor = tu.Turtle()
# timmy_the_turtle.shape('turtle')
cursor.color('DarkOliveGreen4')
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# timmy_the_turtle.left(90)
# for n in range(1, 101):
#     if n % 2 == 0:
#         timmy_the_turtle.penup()
#     else:
#         timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(5)

pen_colors = ['red', 'green', 'blue', 'bisque3', 'DarkSeaGreen', 'DarkSlateGray', 'DeepPink', 'firebrick']
tu.colormode(255)


def draw_10_poligons():
    for n in range(3, 11):
        angle = 360 / n
        # tpl_color = tuple([rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)])
        # tpl_color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
        # cursor.pencolor(tpl_color)
        cursor.pencolor((rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)))
        for _ in range(n):
            cursor.forward(100)
            cursor.right(angle)
    return


def random_walk():
    cursor.pensize(5)
    person = wlk.Walker()
    for _ in range(1000):
        cursor.pencolor((rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)))
        next_direction = person.chose_direction()
        next_nr_steps = person.chose_nr_steps()
        cursor.setheading(next_direction)
        cursor.forward(next_nr_steps)
    return


def draw_spirograph() -> None:
    cursor.speed('fastest')
    for n in range(0, 360, 5):
        cursor.pencolor((rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)))
        cursor.setheading(n)
        cursor.circle(100)
    return


# draw_10_polygons()
# random_walk()
draw_spirograph()
my_screen = tu.Screen()
my_screen.exitonclick()
