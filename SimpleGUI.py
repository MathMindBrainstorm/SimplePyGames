# SimpleGUI program template

# Import the module
import simpleguitk as simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter +1

# Define event handler functions
def tick():
    increment()
    print(counter)

def buttonpress():
    global counter
    counter = 0

# Create a frame
frame = simplegui.create_frame("Nome que aparece no Frame",100,100)

# Register event handlers
timer = simplegui.create_timer(1000,tick)
frame.add_button("Me clica",buttonpress)

# Start frame and timers
frame.start()
timer.start()
