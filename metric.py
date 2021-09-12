
import tkinter
from tkinter import StringVar, font
from typing import Text

#define window
root= tkinter.Tk()
root.title("MHelper")
root.iconbitmap("ruler.ico")
root.resizable(0,0)

#Define fonts and color
field_font = ("Cambria",10)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg=bg_color)

#Define functions
def convert():
    output_field.delete(0,tkinter.END)
    convertion_values = {
        "Byte": 10**0,
        "kByte": 10**3,
        "MByte": 10**6,
        "GByte": 10**9
    }

    #Get user informations
    start_value = float(input_field.get())
    start_prefix = input_choice.get()
    end_prefix = output_choice.get()

    if start_value < 0 :
        print("Error")
    else:
        value = start_value * convertion_values[start_prefix] / convertion_values[end_prefix]
        print(value)
        output_field.insert(0,value)


#Define layout
input_field = tkinter.Entry(root,width=20,font=field_font)
output_field = tkinter.Entry(root,width=20,font=field_font)
equal_label = tkinter.Label(root,text="=",font=field_font,bg=bg_color)

input_field.grid(row=0,column=0,padx=10,pady=10)
equal_label.grid(row=0,column=1)
output_field.grid(row=0,column=2,padx=10,pady=10)

input_field.insert(0,"1")
input_field.focus()

#Create dropdowns for values
bin_list = ["Byte","kByte","MByte","GByte"]
input_choice = StringVar()
output_choice = StringVar()

#Drop downs
input_dropdown = tkinter.OptionMenu(root,input_choice,*bin_list)
output_dropdown = tkinter.OptionMenu(root,output_choice,*bin_list)
input_dropdown.grid(row=1,column=0,sticky="EW",pady=(10,4),padx=10)
output_dropdown.grid(row=1,column=2,sticky="EW",pady=(10,4),padx=10)

#set standard i/0-choices
input_choice.set("Byte")
output_choice.set("kByte")

#create convert button
convert_button = tkinter.Button(root,text="Convert",font=field_font,bg=button_color,command=convert)

convert_button.grid(row=2,column=0,columnspan=3,sticky="NESW")
#Run the root window
root.mainloop()