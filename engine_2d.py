import tkinter as tk
from tkinter import colorchooser
from model.circle import Circle
from model.triangle import Triangle
from model.rectangle import Rectangle
import threading


class Engine2D(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Engine2D')
        self.geometry('750x500')
        self.canvas = tk.Canvas(master=self, width=700, height=500, bg='white')
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.color = None
        self.figures = []
        self.create_frame_with_buttons()

    def create_frame_with_buttons(self):
        self.frame = tk.LabelFrame(master=self.canvas, text='Фигуры', bg='gray', foreground='white', borderwidth=0)
        self.canvas.create_window((0, 0), window=self.frame)
        self.frame.pack(anchor=tk.NW, fill=tk.Y, expand=True)
        self.shape_buttons()
        tk.Button(master=self.frame, width=10, height=2, text='Рисовать', command=self.draw).pack(pady=50)
        tk.Button(master=self.frame, width=10, height=2, text='Смена цвета', command=self.color_change).pack()

    def shape_buttons(self):
        tk.Button(master=self.frame, width=10, height=2, text='Окружность',
                  command=lambda: self.figures.append(Circle.draw(self.color)[0])).pack(pady=2)
        tk.Button(master=self.frame, width=10, height=2, text='Треугольник',
                  command=lambda: self.figures.append(Triangle.draw(self.color)[0])).pack(pady=2)
        tk.Button(master=self.frame, width=10, height=2, text='Прямоугольник',
                  command=lambda: self.figures.append(Rectangle.draw(self.color)[0])).pack(pady=2)

    def color_change(self):
        color = colorchooser.askcolor()[1]
        self.color = color

    def draw(self):
        self.draw_figures()
        threading.Thread(target=self.draw_figures).start()
        self.clear_canvas()
        threading.Thread(target=self.clear_canvas()).start()

    def draw_figures(self):
        for figure in self.figures:
            data_figure = figure.__repr__()
            if data_figure['class'] == 'Circle':
                self.draw_circle(data_figure=data_figure)
            elif data_figure['class'] == 'Triangle':
                self.draw_triangle(data_figure=data_figure)
            elif data_figure['class'] == 'Rectangle':
                self.draw_rectangle(data_figure=data_figure)
        self.canvas.after(ms=1000, func=self.draw_figures)

    def draw_circle(self, data_figure: dict):
        points = (
            (data_figure['x'], data_figure['y']),
            (data_figure['x'] + 2 * data_figure['radius'], data_figure['y'] + 2 * data_figure['radius'])
        )
        if data_figure['color'] is None:
            self.canvas.create_oval(*points, tags='Circle')
        else:
            self.canvas.create_oval(*points, fill=data_figure['color'])

    def draw_triangle(self, data_figure: dict):
        points = (
            (data_figure['ax'], data_figure['ay']),
            (data_figure['bx'], data_figure['by']),
            (data_figure['cx'], data_figure['cy'])
        )
        if data_figure['color'] is None:
            self.canvas.create_polygon(*points, fill='', outline='black')
        else:
            self.canvas.create_polygon(*points, fill=data_figure['color'])

    def draw_rectangle(self, data_figure: dict):
        points = (
            (data_figure['ax'], data_figure['ay']),
            (data_figure['dx'], data_figure['dy'])
        )
        if data_figure['color'] is None:
            self.canvas.create_rectangle(*points)
        else:
            self.canvas.create_rectangle(*points, fill=data_figure['color'])

    def clear_canvas(self):
        self.canvas.after(ms=1000, func=self.clear_canvas)
        self.canvas.delete("all")
        self.figures = []


if __name__ == '__main__':
    app = Engine2D()
    app.mainloop()
