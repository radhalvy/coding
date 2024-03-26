import tkinter as tk

# Needed to do everything
root = tk.Tk()

# Size and title of the window itself
root.geometry("1000x700")
root.title("First GUI application")

# Text inside the window. pack() is necessary to display the object in the window, but they're more functions for this purpose
label = tk.Label(root, text="Hello, world!", font= ('Arial', 20))
label.pack(padx=20, pady= 20)

# Creates a textbox that can be scroll down even if the height is 1. Note: Height means number of lines vertically and width means number of characters horizontally
textbox = tk.Text(root, height= 3, width= 25, font= ('Arial', 18))
textbox.pack(padx= 20)

# Creates a height 1 textbox that can't be scroll down
firstEntry = tk.Entry(root, width= 25, font= ('Arial', 18))
firstEntry.pack(padx= 20, pady= 20)

# Creates a button without any funcionality
firstButton = tk.Button(root, text= "Click!", font= ('Arial', 18))
firstButton.pack(padx= 20)

buttonframe = tk.Frame(root)
# Helps the button to streach instead of leaving a lot of empty space to the sides. It needs to be done for every column
buttonframe.columnconfigure(0, weight= 1)
buttonframe.columnconfigure(1, weight= 1)
buttonframe.columnconfigure(2, weight= 1)

# The button is inside the Frame of buttonframe which is inside root. It needs to have a sticky parameter to make sure it fills the grid
button1 = tk.Button(buttonframe, text= "1", font= ('Arial', 18))
button1.grid(row= 0, column= 0, sticky= tk.W+tk.E)

button2 = tk.Button(buttonframe, text= "2", font= ('Arial', 18))
button2.grid(row= 0, column= 1, sticky= tk.W+tk.E)

button3 = tk.Button(buttonframe, text= "3", font= ('Arial', 18))
button3.grid(row= 0, column= 2, sticky= tk.W+tk.E)

button4 = tk.Button(buttonframe, text= "4", font= ('Arial', 18))
button4.grid(row= 1, column= 0, sticky= tk.W+tk.E)

button5 = tk.Button(buttonframe, text= "5", font= ('Arial', 18))
button5.grid(row= 1, column= 1, sticky= tk.W+tk.E)

button6 = tk.Button(buttonframe, text= "6", font= ('Arial', 18))
button6.grid(row= 1, column= 2, sticky= tk.W+tk.E)

# The grid is inside the buttonframe, but buttonframe is on the pack layout, so we have to use pack() here. 'Fill= "x"'is to make it streach to the X dimension
buttonframe.pack(fill= 'x', padx= 20, pady= 20)

# Creates a button with the place method which places an object in a specific location in the window
anotherButton = tk.Button(root, text= "HI", font= ('Arial', 18))
anotherButton.place(x= 200, y= 200, height= 100, width= 100)

root.mainloop()