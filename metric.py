
import tkinter
from tkinter import StringVar, font

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


#Define layout
input_field = tkinter.Entry(root,width=20,font=field_font)
output_field = tkinter.Entry(root,width=20,font=field_font)
equal_label = tkinter.Label(root,text="=",font=field_font,bg=bg_color)

input_field.grid(row=0,column=0,padx=10,pady=10)
equal_label.grid(row=0,column=1)
output_field.grid(row=0,column=2,padx=10,pady=10)

input_field.insert(0,"The input comes here")


#Create dropdowns for values
bin_list = ["Bit","Byte","KByte","MByte","GByte"]
input_choice = StringVar()
output_choice = StringVar()

#Drop downs
input_dropdown = tkinter.OptionMenu(root,input_choice,*bin_list)
output_dropdown = tkinter.OptionMenu(root,output_choice,*bin_list)
input_dropdown.grid(row=1,column=0,sticky="EW",pady=(10,4),padx=10)
output_dropdown.grid(row=1,column=2,sticky="EW",pady=(10,4),padx=10)

#set standard i/0-choices
input_choice.set("Bit")
output_choice.set("Byte")

#create convert button
convert_button = tkinter.Button(root,text="Convert",font=field_font,bg=button_color)

convert_button.grid(row=2,column=0,columnspan=3,sticky="NESW")
#Run the root window
root.mainloop()