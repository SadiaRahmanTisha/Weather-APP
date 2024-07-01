from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get ("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a052edbfd941f0c25d4fcb52e23a4911").json()

    wa_lbl.config(text=data["weather"][0]["main"])
    wb_lbl.config(text=data["weather"][0]["description"])
    wc_lbl.config(text=str(data["main"]["temp"]-273.15))
    wd_lbl.config(text=data["main"]["pressure"])


win =Tk()
win.config(bg= "blue")
win.geometry('500x570')

name_lbl = Label(win,text="weather App",
                 font=("Arial",30,"bold"))

name_lbl.place(x=25,y=40,height=50,width=450)

city_name = StringVar()
list_name =['Dhaka', 'Ishwardi', 'Pabna', 'Chattogram', 'Dinajpur', 'Gāzipura', 'Rājshāhi', 'Khulna', 'Rangapukur', 'Nārāyanganj', 'Mymensingh', 'Bogra', 'Savar', 'Tungi']

com  = ttk.Combobox(win,text="Weather App",values=list_name,
                      font=("Arial",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)



wa_lbl = Label(win,text="Weather Climate",
                 font=("Arial",20,))
wa_lbl.place(x=25,y=260,height=50,width=210)
wa_lbl = Label(win,text=" ",
                 font=("Arial",20,))
wa_lbl.place(x=250,y=260,height=50,width=210)


wb_lbl = Label(win,text="Weather Description",
                 font=("Arial",17,))
wb_lbl.place(x=25,y=330,height=50,width=210)
wb_lbl = Label(win,text=" ",
                 font=("Arial",17,))
wb_lbl.place(x=250,y=330,height=50,width=210)



wc_lbl = Label(win,text="Temperature",
                 font=("Arial",20,))
wc_lbl.place(x=25,y=400,height=50,width=210)

wc_lbl = Label(win,text=" ",
                 font=("Arial",16,))
wc_lbl.place(x=250,y=400,height=50,width=210)



wd_lbl = Label(win,text="Pressure",
                 font=("Arial",17,))
wd_lbl.place(x=25,y=470,height=50,width=210)
wd_lbl = Label(win,text=" ",
                 font=("Arial",17,))
wd_lbl.place(x=250,y=470,height=50,width=210)



done_button = Button(win,text="Done",
                 font=("Arial",20,"bold"),command=data_get)
done_button.place( x=200,y=190,height=50,width=100)



win.mainloop()



