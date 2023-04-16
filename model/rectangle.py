class Rectangle:
    def __init__(self, color: str, ax: int = 300, ay: int = 150, dx: int = 600, dy: int = 300):
        self.ax = ax
        self.ay = ay
        self.dx = dx
        self.dy = dy
        self.color = color

    def __repr__(self):
        return {'class': 'Rectangle', 'color': self.color, 'ax': self.ax, 'ay': self.ay, 'dx': self.dx, 'dy': self.dy}

    @staticmethod
    def draw(color):
        rectangle = Rectangle(color=color)
        text = f'Drawing Rectangle with upper left corner ({rectangle.ax}, {rectangle.ay}) ' \
               f'and bottom right corner ({rectangle.dx}, {rectangle.dy})'
        if rectangle.color is None:
            print(text)
            return rectangle, text
        else:
            text_with_color = f'{text} and with color "{rectangle.color}"'
            print(text_with_color)
            return rectangle, text_with_color
