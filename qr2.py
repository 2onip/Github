import qrcode
from qrcode import QRCode
import qrcode.constants
from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()

def Pro(*args):
    # global pro_var
    global progress
    text=pro_var.get()
    if text=="99.0":
        messagebox.showinfo("Done","QRCode has generated.Thanks")
        progress.stop()
def create():
        url=e.get() #it is actual data whose qrcode will create
        save_name=e2.get() #save name
        save_type=var.get() #type of image
        if url!="" and save_name!="":
            qr=qrcode.QRCode(version=1,
                             error_correction=qrcode.constants.ERROR_CORRECT_H,
                             border=3,
                            
                            )
            qr.add_data(url) #it is actual data whose qrcode will create
            qr.make(fit=True)
            img=qr.make_image(fill_color="black",back_color="white")

            #Progressbar logic
            progress.start(1)          
            time.sleep(1)
            img.save(f"{save_name}.{save_type}")
            

             
        elif url=="" or save_name=="":
            messagebox.showerror("Error","Fill URL or Image-save portion.Thanks")


root.geometry("600x500")
root.config(background="#8fa3bf")
root.title("qr code generater".title())

pro_var=StringVar(root)
progress=ttk.Progressbar(root,variable=pro_var,mode="determinate",orient=HORIZONTAL,length=370)
progress.place(x=130,y=380)
pro_var.trace("w",Pro)

Label(text="Welcome to QR-Code Generater",bg="grey",font="halvatica 15 bold").pack(fill=X)

e=Entry(root,font="verdana 17 normal")
e.place(x=130,y=110,height=40,width=370)
e.insert(0,"url or text")
def focus(a):
    e.delete(0,END)
def focus_out(a):
    name=e.get()
    if name=="":
        e.insert(0,"url or text")
e.bind("<FocusIn>",focus)
e.bind("<FocusOut>",focus_out)
label2=Label(text="save Image as ",font="matemasie 15 bold",bg="#8fa3bf")
label2.place(x=50,y=170)
e2=Entry(root,font="verdana 17 normal")
e2.place(x=130,y=210,height=40,width=370)
e2.insert(0,"example")
# ////LOGIC FOR DESIGN///
def focus(a):
    e2.delete(0,END)
def focus_out(a):
    name=e2.get()
    if name=="":
        e2.insert(0,"example")
e2.bind("<FocusIn>",focus)
e2.bind("<FocusOut>",focus_out)
# image=PhotoImage(file="image2.png")
button=Button(text="Create",bd=0,bg="Grey",fg="Indigo",font="verdana 17 normal",command=create)
button.place(x=130,y=420,width=370,height=40)
var=StringVar(root)
var.set("png")
r=Radiobutton(text="png",variable=var,value="png",font="verdana 13 normal",background="#8fa3bf")
r.place(x=100,y=270)

r2=Radiobutton(text="jpg",variable=var,value="jpg",font="verdana 13 normal",background="#8fa3bf")
r2.place(x=100,y=320)



root.mainloop()

