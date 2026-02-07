#importing library 

import tkinter as tk

#Window creation

win = tk.Tk()
win.title("Python Calculator by SBS SAHEL")
win.geometry("300x510")


#entry  widget(input field)

entry = tk.Entry(win, width=20, font=("Comic Sans MS",20),justify="right")
entry.pack(pady=10)


#button lay-out

buttons = [
    ('DEL','C','EXIT'),
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','=','%','+'),  #modulas here
    ('00','^','(',')') #Power as '^'
]



#button click event

def button_click(value):
    if value == "C":
        entry.delete(0,tk.END)

    elif value == "EXIT":
        win.quit()

    elif value == "DEL":
        current_text = entry.get()
        entry.delete(len(current_text)-1, tk.END)

    elif value== "=":
        try:
            expr = entry.get().replace("^", "**")     # replace '^' symble as  modulas 
            result = eval(expr)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except:
            entry.delete(0,tk.END)
            entry.insert("SYNTAX ERROR")
    else:
        entry.insert(tk.END,value)
    

#creating frame 

frame = tk.Frame(win)
frame.pack()



#Creating button

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()

    for button in row:
        if button in ["C", "EXIT", "DEL"]:
            bt_color = "#eb5e28"
            txt_color = "black"
        elif button in ["/", "*", "-","+", "=", "%", "^", "(", ")"]:
            bt_color = "#ccc5b9"
            txt_color = "black"
        else:
            bt_color = "#fffcf2"  
            txt_color = "black"
        
        btn = tk.Button(row_frame, width=5, height=2, text=button, bg=bt_color, fg=txt_color, font=("Comic Sans MS",13),
                        command=lambda b=button: button_click(b))
        btn.pack(side="left", padx=5, pady=5)


win.mainloop()


#SBS_SAHEL