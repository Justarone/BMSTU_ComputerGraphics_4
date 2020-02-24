from math import pi
import tkinter as tk
import config as cfg
import tkinter.messagebox as mb

# button1.bind("<Button-1>", function) - вызов function при нажатии левой кнопкой мыши на кнопку
# root.bind(chr('a'), function) - действие на кнопке (применяется при наведении на окно root)
# entry.get()
# label['text'] = ''

figure_points = list()
back_list = list()
A, B, C, D, R = 0, 0, 0, 0, 1


def find_reversed_matrix(matrix):
    det = 0
    for i in range(3):
        det += matrix[0][i] * (matrix[1][(i + 1) % 3] * matrix[2][(i + 2) % 3] -
                               matrix[1][(i + 2) % 3] * matrix[2][(i + 1) % 3])
    new_matrix = list()
    for i in range(3):
        new_matrix.append(list())
        for j in range(3):
            new_matrix[i].append((matrix[(i + 1) % 3][(j + 1) % 3] * matrix[(i + 2) % 3][(j + 2) % 3] -
                                 matrix[(i + 2) % 3][(j + 1) % 3] * matrix[(i + 1) % 3][(j + 2) % 3]) / det)
    return new_matrix


def show_info():
    mb.showinfo("Информация.", cfg.INFORMATION)


def apply_command(matrix):
    for i in range(figure_points):
        new_point = [0, 0, 0]
        for j in range(3):
            for k in range(3):
                new_point[j] += figure_points[i][k] * matrix[j][k]

def enter_params(e_list):
    new_params = list()
    try:
        for e in e_list:
            new_params.append(float(e.get()))
    except ValueError:
        mb.showerror("Некорректные данные", "Ожидались действительные числа! (При этом R != 0)")
    else:
        global A, B, C, D, R, back_list
        A = new_params[0]
        B = new_params[1]
        C = new_params[2]
        D = new_params[3]
        R = new_params[4]
        back_list = list()
        fill_points()


    for e in e_list:
        e.delete(0, tk.END)


def fill_points():
    # t = 0
    # while (t < 2 * math.pi)
    pass


def change_params():
    top = tk.Toplevel(root)
    top.title("Параметры.")
    top["bg"] = cfg.MAIN_COLOUR
    top.resizable(height=False, width=False)

    labels = list()
    entrys = list()

    for i in "abcdr":
        labels.append(tk.Label(top, bg=cfg.MAIN_COLOUR, font=("Consolas", 15), fg=cfg.ADD_COLOUR, text=i))
        entrys.append(tk.Entry(top, bg=cfg.ADD_COLOUR, font=("Consolas", 15), fg=cfg.MAIN_COLOUR, justify="center"))

    for i in range(4):
        labels[i].grid(row=i, column=0, columnspan=1)
        entrys[i].grid(row=i, column=1, padx=10, columnspan=1)

    ok_btn = tk.Button(top, text="Ok", font=("Consolas", 14),
                       bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=lambda: enter_params(entrys),
                     activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)
    ok_btn.grid(row=4, column=0)

    top.mainloop()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x:g}".strip() + "; " + f"{self.y:g}".strip()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def move_figure():
    # try:
        # x = float(dx_entry.get())
        # y = float(dy_entry.get())
    # except ValueError:
        # mb.showerror("Неверный ввод",
                     # "Введите действительные числа в поля ввода")
        # dx_entry.delete(0, tk.END)
        # dy_entry.delete(0, tk.END)
        # return

    # dx_entry.delete(0, tk.END)
    # dy_entry.delete(0, tk.END)

    # new_state = list()
    # for point in state[-1]:
        # point
    pass

def rotate_figure():
    pass

def scale_figure():
    pass

def back_figure():
    pass

def translate_to_comp(point_vector):
    x = int((point_vector[0] - cfg.MIN_LIMIT_X) /
            (cfg.MAX_LIMIT_X - cfg.MIN_LIMIT_X) * cfg.FIELD_WIDTH)
    y = int((1 - (point_vector[1] - cfg.MIN_LIMIT_Y) /
             (cfg.MAX_LIMIT_Y - cfg.MIN_LIMIT_Y)) * cfg.FIELD_HEIGHT)
    return Point(x, y)


root = tk.Tk()
root.title("Computer graphics 2 lab.")
root["bg"] = cfg.MAIN_COLOUR
root.geometry(str(cfg.WINDOW_WIDTH) + "x" + str(cfg.WINDOW_HEIGHT))
root.resizable(height=False, width=False)
# root.bind("<Return>", lambda x: find_solution())


data_frame = tk.Frame(root)
data_frame["bg"] = cfg.MAIN_COLOUR

data_frame.place(x=int(cfg.BORDERS_WIDTH), y=int(cfg.BORDERS_HEIGHT),
                 width=cfg.DATA_WIDTH,
                 height=cfg.DATA_HEIGHT
                 )

# For move command.
dx_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 15),
                   fg=cfg.MAIN_COLOUR, justify="center")
dy_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 15),
                   fg=cfg.MAIN_COLOUR, justify="center")

# For rotate_command.
rx_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 13),
                   fg=cfg.MAIN_COLOUR, justify="center")
ry_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 13),
                   fg=cfg.MAIN_COLOUR, justify="center")
angle_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 13),
                       fg=cfg.MAIN_COLOUR, justify="center")

# For scale command.
sx_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 10),
                   fg=cfg.MAIN_COLOUR, justify="center")
sy_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 10),
                   fg=cfg.MAIN_COLOUR, justify="center")
scx_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 10),
                       fg=cfg.MAIN_COLOUR, justify="center")
scy_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Consolas", 10),
                       fg=cfg.MAIN_COLOUR, justify="center")


move_btn = tk.Button(data_frame, text="Переместить", font=("Consolas", 14),
                     bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=move_figure,
                     activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)
rotate_btn = tk.Button(data_frame, text="Повернуть", font=("Consolas", 14),
                       bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=rotate_figure,
                       activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)
scale_btn = tk.Button(data_frame, text="Масштабировать", font=("Consolas", 14),
                      bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=scale_figure,
                      activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)

back_btn = tk.Button(data_frame, text="<--", font=("Consolas", 24),
                      bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=scale_figure,
                      activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)


move_label = tk.Label(data_frame, text="ПЕРЕМЕЩЕНИЕ.\n(Ввод dx, dy,\nгде dx, dy - перемещение\nпо х и по у соответственно)",
                      font=("Consolas", 9), bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

rotate_label = tk.Label(data_frame, text="ПОВОРОТ.\n(Ввод x, y, angle,\nгде x, y - координаты \nцентра поворота,"\
                      " angle - \nугол поворота в радианах)", font=("Consolas", 9), bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR,
                        relief=tk.GROOVE)

scale_label = tk.Label(data_frame, text="МАСШТАБИРОВАНИЕ.\n(Ввод kx, ky, Mx, My,\nгде М - центр масштабирования,\n" \
                      "kx, ky - коэффициенты \nмасштабирования)", font=("Consolas", 9), bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR,
                       relief=tk.GROOVE)

move_label.place(x=0, y=0, width=cfg.DATA_WIDTH, height = 2 * cfg.DATA_HEIGHT // cfg.COLUMNS)
dx_entry.place(x=0, y=2 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH // 2, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
dy_entry.place(x=cfg.DATA_WIDTH // 2, y=2 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH // 2,
               height = cfg.DATA_HEIGHT // cfg.COLUMNS)
move_btn.place(x=0, y=3 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = cfg.DATA_HEIGHT // cfg.COLUMNS)

rotate_label.place(x=0, y=4 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = 2 * cfg.DATA_HEIGHT // cfg.COLUMNS)
rx_entry.place(x=0, y=6 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH // 3, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
ry_entry.place(x=cfg.DATA_WIDTH // 3, y=6 * cfg.DATA_HEIGHT // cfg.COLUMNS,
              width=cfg.DATA_WIDTH // 3, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
angle_entry.place(x=2 * cfg.DATA_WIDTH // 3, y=6 * cfg.DATA_HEIGHT // cfg.COLUMNS,
                 width=cfg.DATA_WIDTH // 3, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
rotate_btn.place(x=0, y=7 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = cfg.DATA_HEIGHT // cfg.COLUMNS)

scale_label.place(x=0, y=8 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = 2 * cfg.DATA_HEIGHT // cfg.COLUMNS)
sx_entry.place(x=0, y=10 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH // 4, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
sy_entry.place(x=cfg.DATA_WIDTH // 4, y=10 * cfg.DATA_HEIGHT // cfg.COLUMNS,
               width=cfg.DATA_WIDTH // 4, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
scx_entry.place(x=2 * cfg.DATA_WIDTH // 4, y=10 * cfg.DATA_HEIGHT // cfg.COLUMNS,
               width=cfg.DATA_WIDTH // 4, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
scy_entry.place(x=3 * cfg.DATA_WIDTH // 4, y=10 * cfg.DATA_HEIGHT // cfg.COLUMNS,
               width=cfg.DATA_WIDTH // 4, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
scale_btn.place(x=0, y=11 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = cfg.DATA_HEIGHT // cfg.COLUMNS)
back_btn.place(x=0, y=12 * cfg.DATA_HEIGHT // cfg.COLUMNS, width=cfg.DATA_WIDTH, height = cfg.DATA_HEIGHT // cfg.COLUMNS)


field_frame = tk.Frame(root, bg=cfg.ADD_COLOUR)
field = tk.Canvas(field_frame, bg=cfg.ADD_COLOUR)

field_frame.place(x=3 * cfg.BORDERS_WIDTH + cfg.DATA_WIDTH, y=cfg.BORDERS_HEIGHT, width=cfg.FIELD_WIDTH, height=cfg.FIELD_HEIGHT)

field.place(x=0, y=0, width=cfg.FIELD_WIDTH, height=cfg.FIELD_HEIGHT)


info_frame = tk.Frame(root)
info_frame["bg"] = cfg.ADD_COLOUR

info_frame.place(x=cfg.BORDERS_WIDTH, y=cfg.DATA_HEIGHT + 2 * cfg.BORDERS_HEIGHT,
                 width=cfg.INFO_WIDTH, height=cfg.INFO_HEIGHT)

info_button = tk.Button(info_frame, text="i", font=("Consolas", 20),
                        bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=show_info,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)

params_btn = tk.Button(info_frame, text="Параметры", font=("Consolas", 15),
                        bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=change_params,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)

res_label = tk.Label(info_frame, text="", font=("Consolas", 12), fg=cfg.MAIN_COLOUR, bg=cfg.ADD_COLOUR)

res_label.place(x=0, y=0, width=cfg.INFO_WIDTH, height=cfg.INFO_HEIGHT * (cfg.INFO_COLS - 1) // cfg.INFO_COLS)
params_btn.place(x=0, y=cfg.INFO_HEIGHT * (cfg.INFO_COLS - 1) // cfg.INFO_COLS,
                  width=4 / 5 * cfg.INFO_WIDTH, height=cfg.INFO_HEIGHT // cfg.INFO_COLS)
info_button.place(x=4 / 5 * cfg.INFO_WIDTH, y=cfg.INFO_HEIGHT * (cfg.INFO_COLS - 1) // cfg.INFO_COLS,
                  width=1 / 5 * cfg.INFO_WIDTH, height=cfg.INFO_HEIGHT // cfg.INFO_COLS)

root.mainloop()