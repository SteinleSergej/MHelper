
import tkinter

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
equal_label = tkinter.Label(root,text="=")

#Run the root window
root.mainloop()