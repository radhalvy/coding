import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text= "Your message", font= ('Arial', 18))
        self.label.pack(padx=20, pady=20)
        
        self.textbox = tk.Text(self.root, height= 5, font= ('Arial', 16))
        # This is used to bind a keyboard shortcut to trigger an action like pressing Enter instead of clicking a button
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=20, pady=20)
        
        # This will store the state of the checkbox to see if it is checked or not
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text= "Show messagebox", font= ('Arial', 16), variable= self.check_state)
        self.check.pack(padx=20, pady=20)
        
        self.button = tk.Button(self.root, text= "Show message", font= ('Arial', 16), command=self.show_message)
        self.button.pack(padx=20, pady=20)
        
        self.menubar = tk.Menu(self.root)
        
        # The tearoff is to not have a line above the menu
        self.filemenu = tk.Menu(self.menubar, tearoff= 0)
        
        self.filemenu.add_command(label= "Close", command= self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label= "Close without confirming", command= exit)
        
        self.menubar.add_cascade(menu= self.filemenu, label= "File")
        
        self.root.config(menu= self.menubar)
        
        
        
        # Triggers a function when pressing the X button
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 1:
            # self.textbox.get("1.0", tk.END) means everything in the textbox from beginning to end
            messagebox.showinfo(title= "Message", message= self.textbox.get("1.0", tk.END))
        else:
            print(self.textbox.get("1.0", tk.END))
            
    def shortcut(self, event):
        # The event.state and event.keysym need to be checked beforehand by printing them like this: print(event.state)/print(event.keysym)
        if event.state == 4 and event.keysym == "Return":
            self.show_message()
            
    def on_closing(self):
        # Creates a window when pressing the X button to confirm if they want to exit or no
        if messagebox.askyesno(title= "Quit?", message= "Do you really want to exit?"):
            # Closes the application
            self.root.destroy()
        

            
MyGUI()