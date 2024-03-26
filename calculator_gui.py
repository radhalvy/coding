import tkinter as tk
from tkinter import messagebox

class CalculatorGui:
    
    def __init__(self):
        # root creation, resolution and title setting
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Calculator")
        
        # Main title inside window creation
        self.label = tk.Label(self.root, text= "Calculator", font= ('Arial', 20))
        self.label.pack(padx=10, pady=10)
        
        # Textbox type Entry for the numbers display creation
        self.entry = tk.Entry(self.root, width= 20, font= ('Arial', 18))
        self.entry.pack(padx=10, pady=10)
        
        # Button frame creation for the numbers and operations
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight= 1)
        self.buttonFrame.columnconfigure(1, weight= 1)
        self.buttonFrame.columnconfigure(2, weight= 1)
        self.buttonFrame.columnconfigure(3, weight= 1)
        
        # Creation of buttons for numbers 0-9
        self.button1 = tk.Button(self.buttonFrame, text= "1", font= ('Arial', 18), command= lambda: self.set_text(1))
        self.button1.grid(row=0, column=0, sticky= tk.W+tk.E)
        
        self.button2 = tk.Button(self.buttonFrame, text= "2", font= ('Arial', 18), command= lambda: self.set_text(2))
        self.button2.grid(row=0, column=1, sticky= tk.W+tk.E)
        
        self.button3 = tk.Button(self.buttonFrame, text= "3", font= ('Arial', 18), command= lambda: self.set_text(3))
        self.button3.grid(row=0, column=2, sticky= tk.W+tk.E)
        
        self.button4 = tk.Button(self.buttonFrame, text= "4", font= ('Arial', 18), command= lambda: self.set_text(4))
        self.button4.grid(row=1, column=0, sticky= tk.W+tk.E)
        
        self.button5 = tk.Button(self.buttonFrame, text= "5", font= ('Arial', 18), command= lambda: self.set_text(5))
        self.button5.grid(row=1, column=1, sticky= tk.W+tk.E)
        
        self.button6 = tk.Button(self.buttonFrame, text= "6", font= ('Arial', 18), command= lambda: self.set_text(6))
        self.button6.grid(row=1, column=2, sticky= tk.W+tk.E)
        
        self.button7 = tk.Button(self.buttonFrame, text= "7", font= ('Arial', 18), command= lambda: self.set_text(7))
        self.button7.grid(row=2, column=0, sticky= tk.W+tk.E)
        
        self.button8 = tk.Button(self.buttonFrame, text= "8", font= ('Arial', 18), command= lambda: self.set_text(8))
        self.button8.grid(row=2, column=1, sticky= tk.W+tk.E)
        
        self.button9 = tk.Button(self.buttonFrame, text= "9", font= ('Arial', 18), command= lambda: self.set_text(9))
        self.button9.grid(row=2, column=2, sticky= tk.W+tk.E)
        
        self.button0 = tk.Button(self.buttonFrame, text= "0", font= ('Arial', 18), command= lambda: self.set_text(0))
        self.button0.grid(row=3, column=0, columnspan= 2, sticky= tk.W+tk.E)
        
        # Division button
        self.divisionButton = tk.Button(self.buttonFrame, text= "/", font= ('Arial', 18), command= lambda: [self.get_first_entry_values(), self.get_button_id(1)])
        self.divisionButton.grid(row=0, column=3, sticky= tk.W+tk.E)
        
        # Multiplication button
        self.multiplicationButton = tk.Button(self.buttonFrame, text= "*", font= ('Arial', 18), command= lambda: [self.get_first_entry_values(), self.get_button_id(2)])
        self.multiplicationButton.grid(row=1, column=3, sticky= tk.W+tk.E)
        
        # Subtraction button
        self.subtractionButton = tk.Button(self.buttonFrame, text= "-", font= ('Arial', 18), command= lambda: [self.get_first_entry_values(), self.get_button_id(3)])
        self.subtractionButton.grid(row=2, column=3, sticky= tk.W+tk.E)
        
        # Addition Button
        self.addButton = tk.Button(self.buttonFrame, text= "+", font= ('Arial', 18), command= lambda: [self.get_first_entry_values(), self.get_button_id(4)])
        self.addButton.grid(row=3, column=3, sticky= tk.W+tk.E)
        
        # Equals button
        self.equalsButton = tk.Button(self.buttonFrame, text= "=", font= ('Arial', 18), command= self.get_final_entry_values)
        self.equalsButton.grid(row=3, column=2, sticky=tk.W+tk.E)
        
        # Clear button
        self.clearButton = tk.Button(self.buttonFrame, text= "Clear", font= ('Arial', 18), command= self.clear_entry)
        self.clearButton.grid(row=4, column=0, columnspan=4, sticky=tk.W+tk.E)
        
        self.buttonFrame.pack(fill= 'x', padx=10, pady=10)
        
        # Executes a function when closing the application via the 'X' button
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.mainloop()
        
    # Prompts for a confirmation when trying to close the application via the 'X' button  
    def on_closing(self):
        if messagebox.askyesno(title= "Quit?", message= "Do you really want to exit?"):
            self.root.destroy()
            
    # Inserts values in the Entry        
    def set_text(self, value):
        self.entry.insert("insert", value)
        
    def get_first_entry_values(self):
        global firstEntryValue
        firstEntryValue = self.entry.get()
        self.entry.delete(0, "end")
        return firstEntryValue
    
    def get_button_id(self, buttonId):
        self.buttonId = buttonId
    
    def get_final_entry_values(self):
        finalEntryValue = self.entry.get()
        self.entry.delete(0, "end")
        if self.buttonId == 1:
            self.entry.insert(0, int(firstEntryValue) / int(finalEntryValue))
            
        elif self.buttonId == 2:
            self.entry.insert(0, int(firstEntryValue) * int(finalEntryValue))
            
        elif self.buttonId == 3:
            self.entry.insert(0, int(firstEntryValue) - int(finalEntryValue))
        else:
            self.entry.insert(0, int(firstEntryValue) + int(finalEntryValue))
            
    def clear_entry(self):
        self.entry.delete(0, "end")
        
        
        
CalculatorGui()