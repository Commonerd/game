import tkinter

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    text.delete("1.0", tkinter.END)
    text.insert("1.0","check number is" + str(pts))

root = tkinter.Tk()
root.title("ネコ度診断アプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file='sumire.png')
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="診断する", 
                        font=("TImes New Roman", 32), 
                        bg="lightgreen", 
                        command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=30, height=3, font=("Times New Roman", 16))
text.place(x=400, y=30)

bvar = [None] * 7
cbtn = [None] * 7
ITEM = [
    "high place",
    "ball",
    "bikkuri",
    "nezumi",
    "nioi",
    "sakana",
    "yoru"
]

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("TImes New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)
root.mainloop()

                            