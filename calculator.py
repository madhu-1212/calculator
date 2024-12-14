import ipywidgets as widgets
from IPython.display import display
import tkinter.messagebox

# Create a simple interactive widget
button = widgets.Button(description="Click me!")

# Create the display for the calculator
output = widgets.Output()

# Display the widget
display(button, output)

# Set up the layout
entry = widgets.Text(placeholder='Enter expression', description='', disabled=False)
button_clear = widgets.Button(description="Clear")
button_equal = widgets.Button(description="=")

# Function to handle button clicks
def myclick(number):
    entry.value += str(number)

def equal(_):
    try:
        result = str(eval(entry.value))
        entry.value = result
    except:
        entry.value = "Error"

def clear(_):
    entry.value = ""

# Set up button functionality
button_1 = widgets.Button(description='1')
button_2 = widgets.Button(description='2')
button_3 = widgets.Button(description='3')
button_4 = widgets.Button(description='4')
button_5 = widgets.Button(description='5')
button_6 = widgets.Button(description='6')
button_7 = widgets.Button(description='7')
button_8 = widgets.Button(description='8')
button_9 = widgets.Button(description='9')
button_0 = widgets.Button(description='0')
button_add = widgets.Button(description='+')
button_subtract = widgets.Button(description='-')
button_multiply = widgets.Button(description='*')
button_div = widgets.Button(description='/')

# Link button actions
button_1.on_click(lambda b: myclick(1))
button_2.on_click(lambda b: myclick(2))
button_3.on_click(lambda b: myclick(3))
button_4.on_click(lambda b: myclick(4))
button_5.on_click(lambda b: myclick(5))
button_6.on_click(lambda b: myclick(6))
button_7.on_click(lambda b: myclick(7))
button_8.on_click(lambda b: myclick(8))
button_9.on_click(lambda b: myclick(9))
button_0.on_click(lambda b: myclick(0))
button_add.on_click(lambda b: myclick('+'))
button_subtract.on_click(lambda b: myclick('-'))
button_multiply.on_click(lambda b: myclick('*'))
button_div.on_click(lambda b: myclick('/'))

button_clear.on_click(clear)
button_equal.on_click(equal)

# Arrange buttons and widgets
button_box = widgets.HBox([button_1, button_2, button_3])
button_box2 = widgets.HBox([button_4, button_5, button_6])
button_box3 = widgets.HBox([button_7, button_8, button_9])
button_box4 = widgets.HBox([button_0, button_add, button_subtract])
button_box5 = widgets.HBox([button_multiply, button_div, button_equal])

# Arrange everything in a vertical box layout
ui = widgets.VBox([entry, button_box, button_box2, button_box3, button_box4, button_box5, button_clear])

# Display the UI
display(ui)