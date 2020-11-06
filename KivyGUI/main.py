from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from math import sin
from kivy_garden.graph import Graph, MeshLinePlot
import pandas as pd


class MainWindow(BoxLayout):
    bottom_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.add_plot(self.bottom_layout)

    def do_something(self):
        self.bottom_layout.text = "hello"

    def add_plot(self, name):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)

        name.add_widget(graph)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    app = MainApp()
    app.run()
