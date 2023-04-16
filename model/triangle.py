class Triangle:
    def __init__(self,
                 color: str,
                 ax: int = 450, ay: int = 100,
                 bx: int = 350, by: int = 350,
                 cx: int = 550, cy: int = 350
                 ):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.color = color

    def __repr__(self):
        return {'class': 'Triangle', 'color': self.color,
                'ax': self.ax, 'ay': self.ay, 'bx': self.bx, 'by': self.by, 'cx': self.cx, 'cy': self.cy}

    @staticmethod
    def draw(color):
        triangle = Triangle(color=color)
        text = f'Drawing Triangle with vertices ' \
               f'({triangle.ax}, {triangle.ay}), ({triangle.bx}, {triangle.by}), ({triangle.cx}, {triangle.cy})'
        if triangle.color is None:
            print(text)
            return triangle, text
        else:
            text_with_color = f'{text} and with color "{triangle.color}"'
            print(text_with_color)
            return triangle, text_with_color
