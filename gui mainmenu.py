from tkinter import *
from tkinter import ttk

#update 2.0.
win = Tk()
win.geometry("1280x800+300+100")
win.title("student info")

def login_confirm():
    login_frame.pack_forget()
    main_frame.pack(fill= "both", expand= True)
    
def view():
    main_frame.pack_forget()
    view_f.pack(fill= "both", expand=True)
    
def add():
    main_frame.pack_forget()
    add_f.pack(fill= "both", expand=True)
    
def search():
    main_frame.pack_forget()
    search_f.pack(fill= "both", expand=True)

def all():
    main_frame.pack_forget()
    all_f.pack(fill= "both", expand=True)

def exit():
    add_f.pack_forget()
    view_f.pack_forget()
    search_f.pack_forget()
    all_f.pack_forget()
    main_frame.pack(fill= "both", expand=True)

    
def logout():
    main_frame.pack_forget()
    add_f.pack_forget()
    view_f.pack_forget()
    search_f.pack_forget()
    login_frame.pack(fill="both", expand= True)    
    
login_frame = Frame(win, bg= "#9B30FF")
login_frame.pack(fill= "both", expand= True)



enclosure_frame  = Frame(login_frame, bg="sky blue", padx = 20, pady=10, relief= "solid")
enclosure_frame.place(relx= 0.5, rely=0.5, anchor="center")
Label(enclosure_frame, text= "login continue", font= ("Century Gothic", 20), pady=20).pack()
login_btn = Button(enclosure_frame, text="login", width= 20, font=("Century Gothic", 20), command= login_confirm)
exit_btn = Button(enclosure_frame,text="exit", width=20, font=("Century Gothic", 20))
login_btn.pack(), exit_btn.pack()

main_frame= Frame(win, bg= "white")
Label(main_frame, text="main menu", font=("Century Gothic", 20), pady=20).pack()
viewB = Button(main_frame, text="view", width= 20, font=("Century Gothic", 20), command= view)
addB = Button(main_frame, text="add", width= 20, font=("Century Gothic", 20), command= add)
searchB = Button(main_frame, text="search", width= 20, font=("Century Gothic", 20), command= search)
allB = Button(main_frame, text="all in", width= 20, font=("Century Gothic", 20), command= all)
logoutB = Button(main_frame, text="logout",fg="red", width= 20, font=("Century Gothic", 20), command= logout)

viewB.pack(), addB.pack(), searchB.pack(), logoutB.pack(), allB.pack()
viewB.place(x= 50, y=50), searchB.place(x=50, y=100), addB.place(x=50, y=150), logoutB.place(x=50, y=450), allB.place(x=50, y=200)


view_f = Frame(win, bg= "green" )
Label(view_f, text="view", font=("Century Gothic", 20), pady=20).pack()
exit1 = Button(view_f, text="exit", width= 20, font=("Century Gothic", 20), command= exit)
exit1.pack()

add_f= Frame(win, bg= "blue" )
Label(add_f, text="add, hi ", font=("Century Gothic", 20), pady=20).pack()
exit2 = Button(add_f, text="exit", width= 20, font=("Century Gothic", 20), command= exit)
exit2.pack()

all_f= Frame(win, bg= "#7CFC00" )
Label(all_f, text="lahat nato", font=("Century Gothic", 20), pady=20).pack()
exit4 = Button(all_f, text="exit", width= 20, font=("Century Gothic", 20), command= exit)
exit4.pack()

search_f = Frame(win, bg= "pink" )
Label(search_f, text="search", font=("Century Gothic", 20), pady=20).pack()
Entry(search_f, font=("Century Gothic", 20)).pack()
exit3 = Button(search_f, text="exit", width= 20, font=("Century Gothic", 20), command= exit)
exit3.pack()



win.mainloop()