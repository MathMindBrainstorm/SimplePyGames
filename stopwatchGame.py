# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:10:24 2014

@author: Wanderson
"""

# template for "Stopwatch: The Game"
import simpleguitk as simplegui

# define global variables
t = 0
time_display = '00:00.0'
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
#def format():
def format(t):
    seconds = t//10
    tenth_seconds = t%10
    minutes = seconds//60
    seconds = seconds%60
    if seconds<10 and minutes <10:
        time_display = '0'+str(minutes)+":0"+str(seconds)+"."+str(tenth_seconds)
    elif seconds>=10 and minutes <10:
        time_display = '0'+str(minutes)+":"+str(seconds)+"."+str(tenth_seconds)
    else:
        time_display = str(minutes)+":0"+str(seconds)+"."+str(tenth_seconds)
    return time_display

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()
    
def stop_button():
    global t,x,y
    if timer.is_running():
        y += 1
        if t%10 == 0:
            x += 1
    timer.stop()
#   print str(x)+'/'+str(y)

def reset():
    global x,y, t, time_display
    stop_button()
    t = 0
    x = 0
    y = 0
    time_display = '00:00.0'
    
    
# define event handler for timer with 0.1 sec interval
def increment():
    global t
    t += 1

# define draw handler
def draw(canvas):
    global x, y, t, time_display
    time_display = format(t)
    canvas.draw_text(time_display, [80,200], 60,'Red')
    score = str(x)+'/'+str(y)
    canvas.draw_text(score,[250,35],15,'Green')

# create frame
frame = simplegui.create_frame('Stopwatch: The Game',500,500)
frame.add_button('Start', start_button,200)
frame.add_button('Stop', stop_button,200)
frame.add_button('Reset', reset,200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100,increment)

# start frame
frame.start()