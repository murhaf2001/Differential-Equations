from tkinter import ttk, messagebox
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

X0_POSITION_X = 50
X0_POSITION_Y = 60
Y0_POSITION_X = 170
Y0_POSITION_Y = 60
X_POSITION_X = 50
X_POSITION_Y = 130
NUM_STEP_POSITION_X = 170
NUM_STEP_POSITION_Y = 130
N0_POSITION_X = 50
N0_POSITION_Y = 100
N_POSITION_X = 170
N_POSITION_Y = 100
TAB1_EXACT_SOLUTION_CHECKBOX_X = 10
TAB1_EXACT_SOLUTION_CHECKBOX_Y = 230
TAB1_EULER_CHECKBOX_X = 160
TAB1_EULER_CHECKBOX_Y = 230
TAB1_IMPROVED_EULER_CHECKBOX_X = 10
TAB1_IMPROVED_EULER_CHECKBOX_Y = 260
TAB1_RUNGE_KUTTA_CHECKBOX_X = 160
TAB1_RUNGE_KUTTA_CHECKBOX_Y = 260
TAB2_EULER_CHECKBOX_X = 100
TAB2_EULER_CHECKBOX_Y = 230
TAB2_IMPROVED_EULER_CHECKBOX_X = 10
TAB2_IMPROVED_EULER_CHECKBOX_Y = 260
TAB2_RUNGE_KUTTA_CHECKBOX_X = 160
TAB2_RUNGE_KUTTA_CHECKBOX_Y = 260
INITIAL_X0 = 1.0
INITIAL_X = 7.0
INITIAL_Y0 = 0.0
INITIAL_NUM_STEP = 20
INITIAL_N0 = 20
INITIAL_N = 25


class GUI:
    def read_values_tab1(self):
        error_occ = False
        try:
            x0 = float(self.input_x0.get())
        except ValueError:
            x0 = INITIAL_X0
            error_occ = True
        try:
            y0 = float(self.input_y0.get())
        except ValueError:
            y0 = INITIAL_Y0
            error_occ = True
        try:
            X = float(self.input_X.get())
        except ValueError:
            X = INITIAL_X
            error_occ = True
        try:
            steps = int(self.input_num_step.get())
        except ValueError:
            steps = INITIAL_NUM_STEP
            error_occ = True
        if x0 * y0 == -2 and x0 * X <= 0:
            x0 = INITIAL_X0
            y0 = INITIAL_Y0
            X = INITIAL_X
            error_occ = True
        elif x0 * y0 == -2:
            x0 = INITIAL_X0
            y0 = INITIAL_Y0
            error_occ = True
        elif x0 * X <= 0:
            x0 = INITIAL_X0
            X = INITIAL_X
            error_occ = True
        if error_occ:
            messagebox.showerror("Error Reading Values From Tab 1",
                                 "The initial values changed to:\nx0 = {0}\ny0 = {1}\nX = {2}\nN = {3}".format(x0, y0,
                                                                                                               X,
                                                                                                               steps))
        return x0, y0, X, steps

    def read_values_tab2(self):
        error_occ = False
        try:
            N0 = int(self.input_N0.get())
        except ValueError:
            N0 = INITIAL_N0
            error_occ = True
        try:
            N = int(self.input_N.get())
        except ValueError:
            N = INITIAL_N
            error_occ = True
        if not 0 < N0 < N:
            N0 = INITIAL_N0
            N = INITIAL_N
            error_occ = True
        if error_occ:
            messagebox.showerror("Error Reading Values From Tab 1",
                                 "The values taken are:\nN0 = {0}\nN = {1}\n".format(N0, N))
        return N0, N

    # A method to create inputs.
    @staticmethod
    def create_input(win, position_x, position_y, initial_val):
        temp = Entry(win, width=10)
        temp.place(x=position_x, y=position_y)
        temp.insert(END, str(initial_val))
        return temp

    # A method to create labels.
    @staticmethod
    def create_label(win, position_x, position_y, txt):
        temp = Label(win, text=str(txt))
        temp.place(x=position_x, y=position_y, anchor="center")
        return temp

    # A method to create checkboxes.
    @staticmethod
    def create_checkbox(win, txt, var, position_x, position_y):
        checkbox = Checkbutton(win, text=txt, variable=var, onvalue=True, offvalue=False)
        checkbox.select()
        checkbox.place(x=position_x, y=position_y)

    # A method to create canvas to embed matlab graph on window win.
    @staticmethod
    def create_canvas(fig, win):
        canvas = FigureCanvasTkAgg(fig, master=win)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, win)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def __init__(self, command1, command2, command3):
        # Creating the main window of the application.
        self.window = Tk()
        self.window.title("Main self.window")
        self.window.minsize(300, 300)
        self.window.resizable(0, 0)

        # Creating two tabs.
        self.my_notebook = ttk.Notebook(self.window)
        self.my_notebook.pack()

        self.tab1 = Frame(self.my_notebook, width=300, height=300)
        self.tab2 = Frame(self.my_notebook, width=300, height=300)

        self.tab1.pack(fill="both", expand=1)
        self.tab2.pack(fill="both", expand=1)

        self.my_notebook.add(self.tab1, text="Approximation Error")
        self.my_notebook.add(self.tab2, text="Error Analysis")

        # Adding the first tab's inputs.
        self.input_x0 = GUI.create_input(self.tab1, X0_POSITION_X, X0_POSITION_Y, INITIAL_X0)

        self.input_y0 = GUI.create_input(self.tab1, Y0_POSITION_X, Y0_POSITION_Y, INITIAL_Y0)

        self.input_X = GUI.create_input(self.tab1, X_POSITION_X, X_POSITION_Y, INITIAL_X)

        self.input_num_step = GUI.create_input(self.tab1, NUM_STEP_POSITION_X, NUM_STEP_POSITION_Y, INITIAL_NUM_STEP)

        # Adding the first tab's buttons.
        self.plot_button1 = Button(self.tab1, text="Plot Approximation", command=command1)
        self.plot_button1.place(anchor="center", x=90, y=200)

        self.error_button = Button(self.tab1, text="Plot Error", command=command2)
        self.error_button.place(anchor="center", x=215, y=200)

        # Adding the first tab's labels.
        self.label_title = GUI.create_label(self.tab1, 150, 10, "y' = 4/x^2 - y/x - y^2")

        self.label_x0 = GUI.create_label(self.tab1, X0_POSITION_X, X0_POSITION_Y - 20, "x0:")

        self.label_y0 = GUI.create_label(self.tab1, Y0_POSITION_X, Y0_POSITION_Y - 20, "y0:")

        self.label_X = GUI.create_label(self.tab1, X_POSITION_X, X_POSITION_Y - 20, "X:")

        self.label_num_step = GUI.create_label(self.tab1, NUM_STEP_POSITION_X, NUM_STEP_POSITION_Y - 20,
                                               "Number of steps:")

        # Adding the first tab's checkboxes
        self.show_tab1_exact_solution_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab1, "Exact solution", self.show_tab1_exact_solution_checkbox,
                            TAB1_EXACT_SOLUTION_CHECKBOX_X,
                            TAB1_EXACT_SOLUTION_CHECKBOX_Y)

        self.show_tab1_euler_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab1, "Euler method", self.show_tab1_euler_checkbox, TAB1_EULER_CHECKBOX_X,
                            TAB1_EULER_CHECKBOX_Y)

        self.show_tab1_improved_euler_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab1, "Improved Euler method", self.show_tab1_improved_euler_checkbox,
                            TAB1_IMPROVED_EULER_CHECKBOX_X,
                            TAB1_IMPROVED_EULER_CHECKBOX_Y)

        self.show_tab1_runge_kutta_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab1, "Runge Kutta method", self.show_tab1_runge_kutta_checkbox,
                            TAB1_RUNGE_KUTTA_CHECKBOX_X,
                            TAB1_RUNGE_KUTTA_CHECKBOX_Y)

        # Adding the second tab's button.
        self.plot_button2 = Button(self.tab2, text="Plot Error Analysis", command=command3)
        self.plot_button2.place(anchor="center", x=135, y=185)

        # Adding the second tab's inputs.
        self.input_N0 = GUI.create_input(self.tab2, N0_POSITION_X, N0_POSITION_Y, INITIAL_N0)

        self.input_N = GUI.create_input(self.tab2, N_POSITION_X, N_POSITION_Y, INITIAL_N)

        # Adding the second tab's labels.
        self.label_N0 = GUI.create_label(self.tab2, N0_POSITION_X, N0_POSITION_Y - 20, "N0:")

        self.label_N = GUI.create_label(self.tab2, N_POSITION_X, N_POSITION_Y - 20, "N:")

        self.show_tab2_euler_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab2, "Euler method", self.show_tab2_euler_checkbox, TAB2_EULER_CHECKBOX_X,
                            TAB2_EULER_CHECKBOX_Y)

        self.show_tab2_improved_euler_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab2, "Improved Euler method", self.show_tab2_improved_euler_checkbox,
                            TAB2_IMPROVED_EULER_CHECKBOX_X,
                            TAB2_IMPROVED_EULER_CHECKBOX_Y)

        self.show_tab2_runge_kutta_checkbox = BooleanVar()
        GUI.create_checkbox(self.tab2, "Runge Kutta method", self.show_tab2_runge_kutta_checkbox,
                            TAB2_RUNGE_KUTTA_CHECKBOX_X,
                            TAB2_RUNGE_KUTTA_CHECKBOX_Y)

    def start(self):
        self.window.mainloop()