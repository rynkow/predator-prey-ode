import numpy as np
import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

matplotlib.use('Qt5Agg')


prey_0 = 5
predator_0 = 5
prey_birth_rate = 0.5
prey_death_rate = 0.5
predator_birth_rate = 0.25
predator_death_rate = 0.25
t_max = 50


def f(u):
    pred = u[0]
    prey = u[1]

    dPred_dt = (predator_birth_rate*prey_death_rate*prey - predator_death_rate)*pred
    dPrey_dt = (prey_birth_rate - prey_death_rate*pred)*prey

    return np.array([dPred_dt, dPrey_dt])


def F(u, h):
    # 4th order Runge Kutta method - worse results than 2nd order
    # k1 = f(u)
    # k2 = f(u+(1/2*h)*k1)
    # k3 = f(u+1/2*h*k2)
    # k4 = f(u + h*k3)
    #
    # return h/6*(k1 + 2*k2 + 2*k3 + k4)

    # 1th order Runge Kutta method - not effective
    # return f(u)

    # 4th order Runge Kutta method
    k1 = f(u)
    k2 = f(u + h*k1)

    return 1/2*(k1 + k2)


def u_k_plus_1(u_k, h):
    return u_k + h*F(u_k, h)


def simulate():
    u0 = np.array([predator_0, prey_0])
    h = 0.1
    t = np.arange(0, t_max, h)
    u_k = u0
    prey_stats = np.zeros(t.size)
    predator_stats = np.zeros(t.size)
    prey_stats[0] = prey_0
    predator_stats[0] = predator_0

    for i in range(1,t.size):
        u_k = u_k_plus_1(u_k, h)
        predator_stats[i] = u_k[0]
        prey_stats[i] = u_k[1]

    return t, predator_stats, prey_stats


class Plot(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Plot, self).__init__(fig)

    def clear(self):
        self.axes.cla()

    def update_plot(self):
        t, P, N = simulate()
        self.clear()
        self.axes.plot(t, P, 'r', label="drapieżnicy")
        self.axes.plot(t, N, 'b', label="ofiary")
        self.axes.legend()
        self.draw()


def make_slider(min, max, initial, f):
    slider = QSlider(Qt.Horizontal)
    slider.setMinimum(min)
    slider.setMaximum(max)
    slider.setValue(initial)
    slider.valueChanged.connect(f)
    return slider


class SlidersFrame(QFrame):

    def update_slider_vals(self):
        global prey_0, predator_0, prey_birth_rate, prey_death_rate, predator_birth_rate, predator_death_rate, t_max
        prey_0 = self.prey_0_slider.value()
        predator_0 = self.predator_0_slider.value()
        prey_birth_rate = self.prey_birth_rate_slider.value()/100
        prey_death_rate = self.prey_death_rate_slider.value()/100
        predator_birth_rate = self.predator_birth_rate_slider.value()/100
        predator_death_rate = self.predator_death_rate_slider.value()/100
        t_max = self.t_max_slider.value()

        self.plot.update_plot()

    def __init__(self, plot, *args, **kwargs):
        super(SlidersFrame, self).__init__(*args, **kwargs)

        self.plot = plot

        self.prey_0_slider = make_slider(0, 10, 5, self.update_slider_vals)
        self.predator_0_slider = make_slider(0, 10, 5, self.update_slider_vals)
        self.prey_birth_rate_slider = make_slider(0, 100, 50, self.update_slider_vals)
        self.prey_death_rate_slider = make_slider(0, 100, 50, self.update_slider_vals)
        self.predator_birth_rate_slider = make_slider(0, 100, 25, self.update_slider_vals)
        self.predator_death_rate_slider = make_slider(0, 100, 25, self.update_slider_vals)
        self.t_max_slider = make_slider(0, 1000, 50, self.update_slider_vals)

        self.sliderBox = QVBoxLayout()
        self.sliderBox.addWidget(QLabel("Początkowa populocja ofiar"))
        self.sliderBox.addWidget(self.prey_0_slider)
        self.sliderBox.addWidget(QLabel("Początkowa populocja drapieżników"))
        self.sliderBox.addWidget(self.predator_0_slider)
        self.sliderBox.addWidget(QLabel("współczynnik narodzin ofiar"))
        self.sliderBox.addWidget(self.prey_birth_rate_slider)
        self.sliderBox.addWidget(QLabel("Współczynnik zabijania ofiar"))
        self.sliderBox.addWidget(self.prey_death_rate_slider)
        self.sliderBox.addWidget(QLabel("Współczynnik wzrostu populacji drapieżników"))
        self.sliderBox.addWidget(self.predator_birth_rate_slider)
        self.sliderBox.addWidget(QLabel("Współczynnik śmiertelności drapieżników"))
        self.sliderBox.addWidget(self.predator_death_rate_slider)
        self.sliderBox.addWidget(QLabel("Maksymalny czas symulacji"))
        self.sliderBox.addWidget(self.t_max_slider)
        self.setMaximumWidth(300)

        self.setLayout(self.sliderBox)


if __name__ == '__main__':

    app = QApplication([])
    window = QWidget()
    pl = Plot()
    sl = SlidersFrame(pl)
    pl.update_plot()

    layout = QHBoxLayout()
    layout.addWidget(pl)
    layout.addWidget(sl)
    window.setLayout(layout)

    window.showMaximized()
    app.exec()










