class Circle:
    def __init__(self, color: str, x: int = 325, y: int = 125, radius: int = 125):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def __repr__(self):
        return {'class': 'Circle', 'color': self.color, 'x': self.x, 'y': self.y, 'radius': self.radius}

    @staticmethod
    def draw(color):
        circle = Circle(color=color)
        text = f'Drawing Circle: ({circle.x}, {circle.y}) with radius {circle.radius}'
        if circle.color is None:
            print(text)
            return circle, text
        else:
            text_with_color = f'{text} and with color "{circle.color}"'
            print(text_with_color)
            return circle, text_with_color
