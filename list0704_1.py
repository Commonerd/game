import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("info", "click button")

root = tkinter.Tk()
root.title("first message button")
root.geometry("400x200")
btn = tkinter.Button(text="test", command=click_btn)
btn.pack()
root.mainloop()