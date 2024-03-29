import tkinter as tk
from tkinter import messagebox
import random

def get_random_hand():
    machineHand = random.choice(["rock", "paper", "scissors"])
    return machineHand

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Game")
        
        self.machineHand = get_random_hand()
        
        self.mainLabel = tk.Label(self.root, text= "Rock, Paper and Scissors", font= ('Arial', 20))
        self.mainLabel.pack(padx=10, pady=10)
        
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight= 1)
        self.buttonframe.columnconfigure(1, weight= 1)
        self.buttonframe.columnconfigure(2, weight= 1)
        
        self.rockImage = tk.PhotoImage(file= "D:\\Coding\\resources\\National-Pet-Rock-Day-1200x834.png")
        self.rockButton = tk.Button(self.buttonframe, image= self.rockImage, command= lambda: [self.get_id("rock"), self.play()])
        self.rockButton.grid(row= 0, column=0, sticky=tk.W+tk.E)
        
        self.paperImage = tk.PhotoImage(file= "D:\\Coding\\resources\\paper.png")
        self.paperButton = tk.Button(self.buttonframe, image= self.paperImage, command= lambda: [self.get_id("paper"), self.play()])
        self.paperButton.grid(row= 0, column=1, sticky=tk.W+tk.E)
        
        self.scissorsImage = tk.PhotoImage(file= "D:\\Coding\\resources\\scissors.png")
        self.scissorsButton = tk.Button(self.buttonframe, image= self.scissorsImage, command= lambda: [self.get_id("scissors"), self.play()])
        self.scissorsButton.grid(row= 0, column=2, sticky=tk.W+tk.E)
        
        self.buttonframe.pack(padx=10, pady=10)
        
        self.resultLabel = tk.Label()
        
        
        self.root.mainloop()
        
    def get_id(self, buttonId):
        self.buttonId = buttonId
        
    def play(self):
        if self.machineHand == self.buttonId:
            
            self.resultLabel.destroy()
            self.resultLabel = tk.Label(self.root, text= "It's a tie!", font= ('Arial', 20))
            self.resultLabel.pack(padx=10, pady=10)
            self.machineHand = get_random_hand()
        
        elif (self.machineHand == "rock" and self.buttonId == "paper") or (self.machineHand == "paper" and self.buttonId == "scissors") or (self.machineHand == "scissors" and self.buttonId == "rock"):
            
            self.resultLabel.destroy()
            self.resultLabel = tk.Label(self.root, text= "You win!", font= ('Arial', 20))
            self.resultLabel.pack(padx=10, pady=10)
            self.machineHand = get_random_hand()
        
        else:
            
            self.resultLabel.destroy()
            self.resultLabel = tk.Label(self.root, text= "You lost.", font= ('Arial', 20))
            self.resultLabel.pack(padx=10, pady=10)
            self.machineHand = get_random_hand()
            
        
        
GUI()