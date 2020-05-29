import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(st):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(st)
    gpio.cleanup()

def backward(st):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(st)
    gpio.cleanup()

def turn_left(st):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(st)
    gpio.cleanup()

def turn_right(st):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(st)
    gpio.cleanup()

def pivot_left(st):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(st)
    gpio.cleanup()

def pivot_right(st):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(st)
    gpio.cleanup()


def key_input(event):
    init()
    print("Let's Go: ",event,end="")
    print("!")
    key_press=event.char
    sleepy=0.03
    if key_press=="left":
        turn_left(sleepy)
    elif key_press=="down":
        turn_down(sleepy)
    elif key_press=="up":
        turn_up(sleepy)
    elif key_press=="right":
        turn_right(sleepy)
    elif key_press=="control_r":
        pivot_right(sleepy)
    elif key_press=="control_l":
        pivot_left(sleepy)
    else:
        gpio.cleanup()

control_it=tk.Tk()
control_it.bind('<KeyPress>',key_input)
control_it.mainloop()
