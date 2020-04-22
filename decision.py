from tkinter import*
from random import*
class App(Frame):
    def __init__(self, master):
        self.master = master
        master.title("Random Order Generator")
        ndict = {}
        self.label = Label(master, text = 'Guess a number from 1 to 100')
        self.nameLab = Label(master, text = 'Name : ')
        self.numLab = Label(master, text = 'Guess # : ')
        self.nameEnt = Entry(master, bg = 'white')
        self.numEnt = Entry(master, bg = 'white')
        self.nlist = Listbox(master, bg = 'white', fg = 'blue')
        self.addB = Button(master, text='Add', command=lambda : self.nameList(ndict))
        self.resetB = Button(master, text='Reset', fg = 'red', command=lambda : self.resetList(ndict))
        self.randB = Button(master, text='Random #')
       
        self.label.grid(row =0, column=0)
        self.nameLab.grid(row=1, column=0, sticky=W)
        self.numLab.grid(row=2, column=0, sticky=W)
        self.nlist.config(width=30, height=20)

        
        self.nameEnt.grid(row=1, column=1, columnspan=2, sticky=W+E)
        self.numEnt.grid(row=2, column=1, columnspan=2, sticky=W+E)

        self.addB.grid(row=3, column=2, sticky=E)
        self.randB.grid(row=4, column=2, sticky=E)
        self.nlist.grid(row=6, column=1, columnspan=2)
        self.resetB.grid(row=7,column=2, sticky=E)

        
    
    def nameList(self, ndict):
        name = self.nameEnt.get()
        guess = self.numEnt.get()
        ndict[str(name)] = int(guess)
        self.nameEnt.delete(0,END)
        self.numEnt.delete(0,END)
        self.nlist.insert(END,str(name) + " : " + str(guess))
        self.nameEnt.delete(0,END)
        self.numEnt.delete(0,END)
        


    def resetList(self, ndict):
        self.nameEnt.delete(0,END)
        self.numEnt.delete(0,END)
        self.nlist.delete(0,END)
        ndict.reset() 
                  

    def validate(self, new_text):
        if not new_text: # the field is being reseted
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def randomNum():
        randNum = randint(1,100)
root = Tk()
root.geometry("340x480") 
app = App(root)
root.mainloop()