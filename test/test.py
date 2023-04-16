import pytest
from model.circle import Circle
from model.triangle import Triangle
from model.rectangle import Rectangle
from engine_2d import Engine2D


def test_circle_without_color():
    circle = Circle.draw(color=None)[0]
    assert circle.color is None


def test_circle_with_color():
    circle = Circle.draw(color='#000000')[0]
    assert circle.color == '#000000'


def test_triangle_without_color():
    triangle = Triangle.draw(color=None)[0]
    assert triangle.color is None


def test_triangle_with_color():
    triangle = Triangle.draw(color='#000000')[0]
    assert triangle.color == '#000000'


def test_rectangle_without_color():
    rectangle = Rectangle.draw(color=None)[0]
    assert rectangle.color is None


def test_rectangle_with_color():
    rectangle = Rectangle.draw(color='#000000')[0]
    assert rectangle.color == '#000000'


def test_clear_canvas():
    app = Engine2D()
    app.figures = ['test', 'test2']
    app.clear_canvas()
    assert len(app.figures) == 0


def test_empty_canvas():
    app = Engine2D()
    assert len(app.canvas.find_all()) == 1


def test_draw_engine2d():
    app = Engine2D()
    app.draw()
    assert len(app.canvas.find_all()) == 0


def test_draw_circle():
    app = Engine2D()
    circle = Circle('black', 0, 0, 0)
    app.draw_circle(circle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_draw_triangle():
    app = Engine2D()
    triangle = Triangle('black', 0, 0, 0, 0, 0, 0)
    app.draw_triangle(triangle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_draw_rectangle():
    app = Engine2D()
    rectangle = Rectangle('black', 0, 0, 0, 0)
    app.draw_rectangle(rectangle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_check_circle_after_change_color():
    app = Engine2D()
    app.color = '#000000'
    circle = Circle(app.color, 0, 0, 0)
    assert circle.color == '#000000'


def test_draw_circle_after_change_color():
    app = Engine2D()
    circle = Circle(app.color)
    app.color = '#000000'
    app.draw_circle(circle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_check_triangle_after_change_color():
    app = Engine2D()
    app.color = '#000000'
    triangle = Triangle(app.color)
    assert triangle.color == '#000000'


def test_draw_triangle_after_change_color():
    app = Engine2D()
    triangle = Triangle(app.color)
    app.color = '#000000'
    app.draw_triangle(triangle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_check_rectangle_after_change_color():
    app = Engine2D()
    app.color = '#000000'
    rectangle = Rectangle(app.color)
    assert rectangle.color == '#000000'


def test_draw_rectangle_after_change_color():
    app = Engine2D()
    rectangle = Rectangle(app.color)
    app.color = '#000000'
    app.draw_rectangle(rectangle.__repr__())
    assert len(app.canvas.find_all()) == 2


def test_draw_all_figures():
    app = Engine2D()
    circle = Circle(app.color)
    triangle = Triangle(app.color)
    rectangle = Rectangle(app.color)
    app.draw_circle(circle.__repr__())
    app.draw_triangle(triangle.__repr__())
    app.draw_rectangle(rectangle.__repr__())
    assert len(app.canvas.find_all()) == 4


def test_draw_figures():
    app = Engine2D()
    app.figures.append(Circle(app.color))
    app.figures.append(Triangle(app.color))
    app.figures.append(Rectangle(app.color))
    app.draw_figures()
    assert len(app.canvas.find_all()) == 4


def test_draw_figures_after_change_color():
    app = Engine2D()
    app.color = 'white'
    app.figures.append(Circle(app.color))
    app.figures.append(Triangle(app.color))
    app.draw_figures()
    assert len(app.canvas.find_all()) == 3


def test_clear_figure_after_draw():
    app = Engine2D()
    app.figures.append(Circle(app.color))
    app.draw()
    assert len(app.canvas.find_all()) == 0


def test_clear_figure_after_change_color_and_draw():
    app = Engine2D()
    app.color = 'white'
    app.figures.append(Circle(app.color))
    app.draw()
    assert len(app.canvas.find_all()) == 0


def test_text_draw_circle():
    circle = Circle.draw(color=None)
    circle_obj = circle[0]
    circle_text = circle[1]
    assert circle_text == f'Drawing Circle: ({circle_obj.x}, {circle_obj.y}) with radius {circle_obj.radius}'


def test_text_draw_circle_after_change_color():
    app = Engine2D()
    app.color = 'white'
    circle = Circle.draw(color=app.color)
    circle_obj = circle[0]
    circle_text = circle[1]
    assert circle_text == f'Drawing Circle: ({circle_obj.x}, {circle_obj.y}) with radius {circle_obj.radius} ' \
                          f'and with color "{circle_obj.color}"'


def test_text_draw_triangle():
    triangle = Triangle.draw(color=None)
    triangle_obj = triangle[0]
    triangle_text = triangle[1]
    assert triangle_text == f'Drawing Triangle with vertices ({triangle_obj.ax}, {triangle_obj.ay}), ' \
                            f'({triangle_obj.bx}, {triangle_obj.by}), ({triangle_obj.cx}, {triangle_obj.cy})'


def test_text_draw_triangle_after_change_color():
    app = Engine2D()
    app.color = 'white'
    triangle = Triangle.draw(color=app.color)
    triangle_obj = triangle[0]
    triangle_text = triangle[1]
    assert triangle_text == f'Drawing Triangle with vertices ({triangle_obj.ax}, {triangle_obj.ay}), ' \
                            f'({triangle_obj.bx}, {triangle_obj.by}), ({triangle_obj.cx}, {triangle_obj.cy}) ' \
                            f'and with color "{triangle_obj.color}"'


def test_text_draw_rectangle():
    rectangle = Rectangle.draw(color=None)
    rectangle_obj = rectangle[0]
    rectangle_text = rectangle[1]
    assert rectangle_text == f'Drawing Rectangle with upper left corner ({rectangle_obj.ax}, {rectangle_obj.ay}) ' \
                             f'and bottom right corner ({rectangle_obj.dx}, {rectangle_obj.dy})'


def test_text_draw_rectangle_after_change_color():
    app = Engine2D()
    app.color = 'white'
    rectangle = Rectangle.draw(color=app.color)
    rectangle_obj = rectangle[0]
    rectangle_text = rectangle[1]
    assert rectangle_text == f'Drawing Rectangle with upper left corner ({rectangle_obj.ax}, {rectangle_obj.ay}) ' \
                             f'and bottom right corner ({rectangle_obj.dx}, {rectangle_obj.dy}) ' \
                             f'and with color "{rectangle_obj.color}"'
