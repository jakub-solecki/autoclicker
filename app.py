
import tkinter as tk
from tkinter import  DISABLED, StringVar, IntVar
import time
from threading import Timer
import mouse
import keyboard
import winsound


root = tk.Tk()
root.title("Autoclicker")
root.resizable(False,False) # makes frame impossible to resize

running_variables = {"running": 0, "time": 100}


def stop_repeat():
    no_of_clicks_input["state"] = "disabled"
    print("stop repeat")

def no_of_clicks():
    no_of_clicks_input["state"] = "normal"
    
    print("No of clicks")

def check_no_of_clicks():
    global no_of_clicks_var
    a = no_of_clicks_var.get()
    number=1
    try:
        int(a)
        number=int(a)
    except:
        top= tk.Toplevel(root)
        top.geometry("280x70")
        top.title("Warning!")

        winsound.Beep(1635, 300)
        top.attributes('-topmost',True)
        tk.Label(top, text= "Number of clicks must be a integer number!").place(x=20, y=20)
        stop_program()
    print(number)
    return number
    

def check_if_number():
    global minutes_input_var, seconds_input_var, miliseconds_input_var
    c=minutes_input_var.get() 
    d=seconds_input_var.get() 
    e=miliseconds_input_var.get() 
    timee=0.1
    try:
        int(c)
        int(d)
        int(e)
        timee = int(e) + int( d) * 1000 + int(c)* 60000
        timee = round(timee/1000, 4)
    except:
        
        top= tk.Toplevel(root)
        top.geometry("250x70")
        top.title("Warning!")
        winsound.Beep(1635, 300)
        top.attributes('-topmost',True)
        tk.Label(top, text= "Every input must be a integer number!").place(x=20, y=20)
        stop_program()
        

    print(timee)
    return timee

def threaded_clicking():
    
    global running_variables,right_left_click_mode, single_double_click_mode,minutes_input_var, seconds_input_var, miliseconds_input_var, repeat_until_var, no_of_clicks_var

    right_left_click_inp =right_left_click_mode.get()
    single_double_click_inp= single_double_click_mode.get() 
    f=repeat_until_var.get()
   

    running_variables["time"]= check_if_number()
    if f == "stop":
        while running_variables["running"]==1:
            
            for i in range(single_double_click_inp):
                mouse.click(right_left_click_inp)
                print("Hello world")
            print(running_variables["time"])
            time.sleep(running_variables["time"])
    elif f=="clicks":
        number = check_no_of_clicks()
        for i in range(number):
            if running_variables["running"]==1:
                mouse.click(right_left_click_inp)
            else:
                break
            print("dziala")
            time.sleep(running_variables["time"])
        stop_program()




def start_program():
    start_button["state"] = "disabled"
    stop_button["state"] = "normal"
    global running_variables

    if running_variables["running"]==0:
        running_variables["running"]=1
        threaded_var = Timer(0.5, threaded_clicking)
        threaded_var.start()

    print("start program")

def stop_program():
    start_button["state"] = "normal"
    stop_button["state"] = "disabled"
    global running_variables
    running_variables["running"]=0

    print("stop program")




SMALL_FRAME_WIDTH = 150
LARGE_FRAME_WIDTH=300

right_left_click_mode = StringVar()
single_double_click_mode = IntVar()
minutes_input_var = StringVar()
seconds_input_var = StringVar()
miliseconds_input_var = StringVar()
repeat_until_var = StringVar()
no_of_clicks_var = StringVar()

#LABELS
top_labels = tk.Frame(root, width=LARGE_FRAME_WIDTH)
tk.Label(top_labels, text="Left or right click", padx=20).grid(row=0,column=0)
tk.Label(top_labels, text="Single/double click", padx=20).grid(row=0,column=1)

top_labels.grid(row=0,columnspan=2)

#ROW 1, COLLUMN 0
left_or_right_click_frame=tk.Frame(root,height=30,width=SMALL_FRAME_WIDTH, bd=3)

left_click_radio=tk.Radiobutton(left_or_right_click_frame, text="Left", variable=right_left_click_mode, value="left")
left_click_radio.select()
left_click_radio.grid(row=1,column=0)
right_click_radio=tk.Radiobutton(left_or_right_click_frame, text="Right", variable=right_left_click_mode, value="right")
right_click_radio.deselect()
right_click_radio.grid(row=1,column=1)

left_or_right_click_frame.grid(row=1, column=0)

#ROW 1, COLLUMN 1
single_double_click_frame=tk.Frame(root,height=30,width=SMALL_FRAME_WIDTH)


single_click_radio=tk.Radiobutton(single_double_click_frame, text="Single", variable=single_double_click_mode, value=1)
single_click_radio.select()
single_click_radio.grid(row=0)
double_click_radio=tk.Radiobutton(single_double_click_frame, text="Double", variable=single_double_click_mode, value=2)
double_click_radio.deselect()
double_click_radio.grid(row=1)

single_double_click_frame.grid(row=1,column=1)

#ROW 2
time_between_clicks_frame=tk.Frame(root, height=60,width=LARGE_FRAME_WIDTH)

tk.Label(time_between_clicks_frame, text="Time between clicks").grid(row=0, columnspan=6)

minutes_between_clicks_input = tk.Entry(time_between_clicks_frame, textvariable=minutes_input_var, width=10 )
minutes_between_clicks_input.insert("0",0)
minutes_between_clicks_input.grid(row=1,column=0)
tk.Label(time_between_clicks_frame, text="min").grid(row=1, column=1)

seconds_between_clicks_input = tk.Entry(time_between_clicks_frame, textvariable=seconds_input_var, width=10 )
seconds_between_clicks_input.insert("0",0)
seconds_between_clicks_input.grid(row=1,column=2)
tk.Label(time_between_clicks_frame, text="s").grid(row=1, column=3)

miliseconds_between_clicks_input = tk.Entry(time_between_clicks_frame, textvariable=miliseconds_input_var, width=10 )
miliseconds_between_clicks_input.insert(1,100)
miliseconds_between_clicks_input.grid(row=1,column=4)
tk.Label(time_between_clicks_frame, text="ms").grid(row=1, column=5)


time_between_clicks_frame.grid(row=2, columnspan=2)

#ROW 3
repeat_until_frame=tk.Frame(root, height=30,width=LARGE_FRAME_WIDTH)

tk.Label(repeat_until_frame, text="Repeat until").grid(row=0, columnspan=3)

stop_radio = tk.Radiobutton(repeat_until_frame, text="Stop", variable=repeat_until_var, value="stop", command=stop_repeat)
stop_radio.select()
stop_radio.grid(row=1,column=0)

no_of_clicks_radio = tk.Radiobutton(repeat_until_frame, text="No. of clicks", variable=repeat_until_var, value="clicks", command=no_of_clicks)
no_of_clicks_radio.deselect()
no_of_clicks_radio.grid(row=1,column=1)

no_of_clicks_input = tk.Entry(repeat_until_frame, textvariable=no_of_clicks_var, width=10 )
no_of_clicks_input.insert(0,1)
no_of_clicks_input["state"] = "disabled"
no_of_clicks_input.grid(row=1,column=2)

repeat_until_frame.grid(row=3, columnspan=2,pady=10)

#ROW 4
start_stop_frame=tk.Frame(root, height=30, width=LARGE_FRAME_WIDTH)

start_button = tk.Button(start_stop_frame, text="Start [F5]", command=start_program)
start_button.grid(row=0,column=0,pady=10,padx=10)

stop_button = tk.Button(start_stop_frame,text="Stop [F6]", command=stop_program ,state=DISABLED)
stop_button.grid(row=0,column=1,pady=10,padx=10)


start_stop_frame.grid(row=4, columnspan=2)

#KEYBOARD INPUT

        
keyboard.add_hotkey("f5", lambda: start_program())
keyboard.add_hotkey("f6", lambda: stop_program())

#START GUI
root.attributes('-topmost',True) # makes GUI stay always on top
root.mainloop()