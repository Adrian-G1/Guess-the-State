from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state_name: str):
        self.write(state_name)

    def move_state(self, x_cor: int, y_cor: int):
        self.goto(x_cor, y_cor)
