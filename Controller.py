import numpy as np

from matplotlib.figure import Figure

from Implementation import *
from View import *


class Controller:
    def get_approximation_graphs(self):
        x0, y0, X, steps = self.gui.read_values_tab1()
        h = (X - x0) / steps
        list_x = [x0 + h * i for i in range(steps + 1)]
        try:
            euler_graph = EulerMethod.approximation_graph(x0, y0, steps + 1, h)
            improved_euler_graph = ImprovedEulerMethod.approximation_graph(x0, y0, steps + 1, h)
            runge_kutta_graph = RungeKuttaMethod.approximation_graph(x0, y0, steps + 1, h)
        except OverflowError:
            messagebox.showerror("Overflow Error",
                                 "Overflow occurred during finding approximations.\nPlease try different values")
            return [None] * 4
        return list_x, euler_graph, improved_euler_graph, runge_kutta_graph

    def get_error_graphs(self):
        x0, y0, X, steps = self.gui.read_values_tab1()
        h = (X - x0) / steps
        list_x = [x0 + h * i for i in range(steps + 1)]
        try:
            euler_error_graph = EulerMethod.error_graph(x0, y0, steps + 1, h)
            improved_euler_error_graph = ImprovedEulerMethod.error_graph(x0, y0, steps + 1, h)
            runge_kutta_error_graph = RungeKuttaMethod.error_graph(x0, y0, steps + 1, h)
        except OverflowError:
            messagebox.showerror("Overflow Error",
                                 "Overflow occurred during finding approximations.\nPlease try different values")
            return [None] * 4
        return list_x, euler_error_graph, improved_euler_error_graph, runge_kutta_error_graph

    def get_error_analysis_graphs(self):
        x0, y0, X, steps = self.gui.read_values_tab1()
        N0, N = self.gui.read_values_tab2()
        list_n = list(range(N0, N + 1))
        try:
            euler_error_analysis_graph = EulerMethod.error_analysis_graph(x0, y0, X, N0, N)
            improved_euler_error_analysis_graph = ImprovedEulerMethod.error_analysis_graph(x0, y0, X, N0, N)
            runge_kutta_error_analysis_graph = RungeKuttaMethod.error_analysis_graph(x0, y0, X, N0, N)
        except OverflowError:
            messagebox.showerror("Overflow Error",
                                 "Overflow occurred during finding approximations.\nPlease try different values")
            return [None] * 4
        return list_n, euler_error_analysis_graph, improved_euler_error_analysis_graph, runge_kutta_error_analysis_graph

    def plot_all_approximation_graphs(self):
        list_x, euler_graph, improved_euler_graph, runge_kutta_graph = self.get_approximation_graphs()
        if list_x is None:
            return
        temp_window = Tk()
        temp_window.wm_title("Approximation")
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        if self.gui.show_tab1_exact_solution_checkbox.get():
            t = np.arange(list_x[0], list_x[-1], .001)
            line, = ax.plot(t, ExactSolution.function(t, list_x[0], euler_graph[0]))
            line.set_label("Exact Solution")
        if self.gui.show_tab1_euler_checkbox.get():
            ax.plot(list_x, euler_graph, label="Euler Approximation")
        if self.gui.show_tab1_improved_euler_checkbox.get():
            ax.plot(list_x, improved_euler_graph, label="Improved Euler Approximation")
        if self.gui.show_tab1_runge_kutta_checkbox.get():
            ax.plot(list_x, runge_kutta_graph, label="Runge Kutta Approximation")
        ax.set_title("Approximation")
        ax.grid()
        ax.set_xlabel('x', fontsize=20)
        ax.set_ylabel('y', rotation=0, fontsize=20, labelpad=10)
        ax.legend()
        GUI.create_canvas(fig, temp_window)

    def plot_all_error_graphs(self):
        list_x, euler_error_graph, improved_euler_error_graph, runge_kutta_error_graph = self.get_error_graphs()
        if list_x is None:
            return
        temp_window = Tk()
        temp_window.wm_title("Error")
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        if self.gui.show_tab1_euler_checkbox.get():
            ax.plot(list_x, euler_error_graph, label="Euler Error")
        if self.gui.show_tab1_improved_euler_checkbox.get():
            ax.plot(list_x, improved_euler_error_graph, label="Improved Euler Error")
        if self.gui.show_tab1_runge_kutta_checkbox.get():
            ax.plot(list_x, runge_kutta_error_graph, label="Runge Kutta Error")
        ax.set_title("Error")
        ax.grid()
        ax.set_xlabel('x', fontsize=20)
        ax.set_ylabel('e', rotation=0, fontsize=20, labelpad=10)
        ax.legend()
        GUI.create_canvas(fig, temp_window)

    def plot_all_error_analysis_graphs(self):
        list_n, euler_error_analysis_graph, improved_euler_error_analysis_graph, runge_kutta_error_analysis_graph = \
            self.get_error_analysis_graphs()
        if list_n is None:
            return
        temp_window = Tk()
        temp_window.wm_title("Error Analysis")
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        if self.gui.show_tab2_euler_checkbox.get():
            ax.plot(list_n, euler_error_analysis_graph, label="Euler Error Analysis")
        if self.gui.show_tab2_improved_euler_checkbox.get():
            ax.plot(list_n, improved_euler_error_analysis_graph, label="Improved Euler Error Analysis")
        if self.gui.show_tab2_runge_kutta_checkbox.get():
            ax.plot(list_n, runge_kutta_error_analysis_graph, label="Runge Kutta Error Analysis")
        ax.set_title("Error Analysis")
        ax.grid()
        ax.set_xlabel('n', fontsize=20)
        ax.set_ylabel('E', rotation=0, fontsize=20, labelpad=10)
        ax.legend()
        GUI.create_canvas(fig, temp_window)

    def __init__(self):
        self.gui = GUI(self.plot_all_approximation_graphs, self.plot_all_error_graphs,
                       self.plot_all_error_analysis_graphs)

    def start(self):
        self.gui.start()


controller = Controller()
controller.start()
