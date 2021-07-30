#importing tkinter module for GUI application
from tkinter import *

def save_info():
    
    Name = name.get()
    
    Email = email.get()

    mobile_no = mobileno.get()

    print(Name,Email,mobile_no)
    
    
    file = open("user.txt","w")
    
    file.write("Your Name " + Name)
    
    file.write("\n")
    
    file.write("Your Email " + Email)
    
    file.write("\n")
    
    file.write("Your mobile no " + str(mobileno))
    
    file.close() 
    
root = Tk()
root.geometry("500x500")

root.title('Registration form')
label_0 =Label(root,text="Registration form", width=20,font=("bold",20)).place(x=90,y=60)

label_1 =Label(root,text="Name", width=20,font=("bold",10)).place(x=80,y=130)
entry_1=Entry(root).place(x=240,y=130)

label_2 =Label(root,text="Email", width=20,font=("bold",10)).place(x=68,y=180)
entry_2=Entry(root).place(x=240,y=180)

lable_3=Label(root,text="mobile no", width=20,font=("bold",10)).place(x=68,y=220)
entry_3=Entry(root).place(x=240,y=220)

Name = StringVar()
Email = StringVar()
mobile_no = IntVar()


Button(root, text='Submit data' ,command=save_info, width=20,height=2,bg="black",fg='white').place(x=180,y=380)

root.mainloop()


