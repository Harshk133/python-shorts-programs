import turtle
import colorsys


def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    spiral = turtle.Turtle()
    spiral.speed(0)
    spiral.width(2)

    no_of_colors = 36
    hues = [x / no_of_colors for x in range(no_of_colors)]
    colors = [colorsys.hsv_to_rgb(h, 1.0, 1.0) for h in hues]

    for i in range(360):
        color = colors[i % no_of_colors]
        spiral.color(color)
        spiral.forward(i * 2)
        spiral.right(59)

    turtle.done()


if __name__ == "__main__":
    draw_spiral()

