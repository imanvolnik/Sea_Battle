from tkinter import *
from tkinter import messagebox
import time

tk = Tk()
app_running = True

size_canvas_x = 595
size_canvas_y = 595
s_x = s_y = 7 #The size of table
step_x = size_canvas_x // s_x # horizontal step
step_y = size_canvas_y // s_y # vertical step
menu_x = 250
ships = 7
ship_len1 = 4
ship_len2 = 2
ship_len3 = 1



def on_closing():
    global app_running 
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Sea Battle")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
tk.update()

def draw_table():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)

draw_table()

def button_show_enemy():
    pass


def button_restart():
    pass


b0 = Button(tk, text="Show the enemy ships", command= button_show_enemy)
b0.place(x = size_canvas_x + 20, y = 40)

b1 = Button(tk, text="Restart", command= button_restart)
b1.place(x = size_canvas_x + 20, y = 100)

def add_to_all(event):
    _type = 0
    if event.num == 3:
        _type = 1
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    print(ip_x, ip_y, "_type: ", _type)

canvas.bind_all("<Button-1>", add_to_all) #left mouse button
canvas.bind_all("<Button-3>", add_to_all) #right mouse button

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
