from tkinter import *

people = ["Justin", "Chris", "Juan"]

#-------------------------Helps print statment when clicking a button-----------------
def friend():
    if (x.get()==0):
        print("Justin we've known each other since beginning of college")
    elif(x.get()==1):
        print("Chris I've known you a year and half later after Justin")
    elif(x.get()==2):
        print("Juan your surprisingly a safe-ish driver")

def submit():
    print("On Scale of 1 to 100, they are a " + str(scale.get()))

#---------------------------makes title for your GUI--------------------
i = Tk()
i.geometry('270x325')
i.title("Another GUI")

#---------------------------------Make photo Icon for you GUI--------------------
pic = PhotoImage(file='img.png')
i.iconphoto(True,pic)

#---------------------------------Makes yout GUI background color-----------------
i.config(background='cyan')

#---------------------------------------Makes Label Title--------------------------
text = Label(i,text="Another Small GUI",
             background="red",
             foreground='Blue',
             font=('Times New Roman', 20, 'bold'),
             relief=RAISED, bd=10)
text.pack()

#----------------------------Makes Radio Buttons--------------------------------
x = IntVar()
for index in range(len(people)):
    radiobutton = Radiobutton(i,
                   text=people[index], #adds text to radiobuttons
                   variable=x,#groups all radiobuttons to 1 if share same value
                   value=index,#shows different value for each radiobutton
                   padx='10',
                   font=('Times New Roman', 20, 'bold'),
                   background='blue',
                   activebackground='white',
                   foreground='black',
                   activeforeground='black',
                   indicatoron=0,#changes to push buttons when selecting
                   width=15,
                   command=friend)

#-----------------------------Makes Vertical style radio button-----------------------
    radiobutton.pack(anchor=W) #use anchor to make vertical radiobutton instead of side

#---------------------------Making Scale------------------------------------------------

scale = Scale(i,
              from_=100,to=0,
              font=('Times New Roman', 10, 'bold'),
              background='#D9F7FA',
              activebackground='black',
              foreground='red',
              tickinterval=20, #values on scale go by 20's
              troughcolor='#158790')
scale.pack()

options = Button(i,
                 text='submit'
                 ,command=submit,
                 activebackground='#05B2BF')
options.pack()

i.mainloop()