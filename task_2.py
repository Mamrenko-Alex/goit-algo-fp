import turtle
import math


def draw_pythagoras_tree(t, length, depth, angle=45):
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    # Намалювати стовбур
    t.forward(length)

    # Зберегти поточну позицію та напрямок
    x, y = t.pos()
    heading = t.heading()

    # Намалювати ліву гілку
    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1, angle)

    # Відновити позицію та напрямок
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()

    # Намалювати праву гілку
    t.right(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1, angle)

    # Повернутися до основи стовбура
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


def main():
    depth = int(input("Введіть глибину дерева: "))

    try:
        if depth < 0:
            raise ValueError("Глибина повинна бути невід'ємною.")
    except ValueError as e:
        print(f"Помилка: {e}")

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.color("red")

    draw_pythagoras_tree(t, length=100, depth=depth if depth > 0 else 0)

    screen.mainloop()


if __name__ == "__main__":
    main()
