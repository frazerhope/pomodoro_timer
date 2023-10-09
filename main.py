from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = '00:00')
    timer_label.config(text= 'Timer')
    check_mark_label.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text='Work',fg = GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Have a coffee! :)',fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text= 'Stretch your legs',fg= PINK)


    # count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print(count)
    global CHECK_MARK
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark_label.config(text=CHECK_MARK*int(reps/2))
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
canvas.create_image(105, 112, image=image_tomato)

timer_text = canvas.create_text(105, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset',command=reset_timer)
reset_button.grid(column=2, row=2)

# labels

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(text='', font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()
