import turtle


def draw_pythagoras_tree(t, order, size, angle=45):
    """Draw Pythagoras tree fractal using recursion."""

    if order == 0:
        return

    t.forward(size)

    position = t.position()
    heading = t.heading()

    t.left(angle)
    draw_pythagoras_tree(t, order - 1, size * 0.7, angle)

    t.penup()
    t.setposition(position)
    t.setheading(heading)
    t.pendown()

    t.right(angle)
    draw_pythagoras_tree(t, order - 1, size * 0.7, angle)

    t.penup()
    t.setposition(position)
    t.setheading(heading)
    t.pendown()
    t.backward(size)


def run_pythagoras_tree(order, size=100, angle=45):
    """Setup turtle screen and draw Pythagoras tree."""

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    draw_pythagoras_tree(t, order, size, angle)

    window.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Enter recursion level: "))
        if level < 0:
            raise ValueError
        run_pythagoras_tree(level, size=120, angle=45)
    except ValueError:
        print("Invalid input.")
