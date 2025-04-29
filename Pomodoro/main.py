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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    tick.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        if reps < 8:
            count_down(short_break_sec)
            label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        else:
            count_down(long_break_sec)
            label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        mark = ""
        work_sessions = math.floor(reps / 2)

        for i in range(work_sessions):
            mark += "✔"

        tick.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)



label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(column=2, row=0)

start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=1, row=2)

reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=timer_reset)
reset.grid(column=3, row=2,)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
tick.grid(column=2, row=3)




window.mainloop()