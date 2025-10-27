from customtkinter import *

window = CTk()
window.geometry("480x480")

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            color = "black"
        else:
            color = "white"

        button = CTkButton(window,text="", fg_color=color,width=56,height=56)
        button.grid(row=i, column=j, padx=2,pady=2)


window.mainloop()

