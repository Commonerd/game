import tkinter

def check():
    if cval.get() ==  True:
        print("checked")
    else:
        print("not checked")
    
root = tkinter.Tk()
root.title("know check status")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="check button",
                           variable=cval,
                           command=check)
cbtn.pack()
root.mainloop()