from tkinter import *


class GuardianLocator:

    def __init__(self, master):
        #self._name = ""
        frame = Frame(master)
        frame.grid()
        master.title("GUARDIAN LOCATOR")

        self.locator_label = Label(frame, text="Which Sailor Guardian are you looking for?", width=40, height=2)
        self.locator_label.grid()

        self.entry = Entry(frame)
        self.entry.grid()

        self.button1 = Button(frame, text="Search", command=self.guardian_name, pady=2)
        self.button1.grid()

    def guardian_name(self):
        self._name = self.entry.get()
        print(self.entry.get())


root = Tk()
locator = GuardianLocator(root)

root.mainloop()

# this will be executed after the root window is closed.
print("Name is", locator._name)