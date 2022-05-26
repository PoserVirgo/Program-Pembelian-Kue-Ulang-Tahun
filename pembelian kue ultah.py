from tkinter import * 
from tkinter import ttk
from tkinter import messagebox



top = Tk()
radio = IntVar()
stringnama = StringVar()
top.geometry("520x480")
top.title("TOKO KUE ULANG TAHUN")
frame1 = Frame(top, bd= 10, relief=GROOVE)
frame1.pack(side=TOP)
frame2 = Frame(top, bd= 5, height=400,width=300,relief=GROOVE)
frame2.pack(side=LEFT,fill="both",expand=1)
 
class label:
    mylabel = Label(frame1,font=('Helvetica',25,'bold'), text= 'Toko Kue Ulang Tahun',fg= 'white',bg='black',justify='left')
    mylabel.grid(row=1, column=1)
    lbnama = Label(frame2,font = ("Helvetica",15), text = "Nama\t:")
    lbnama.grid(row=7, column=0)
    lbnama2= Entry(frame2,font = ("Helvetica",15,'bold'), textvariable=stringnama,bd=6,width=8,bg="white",justify='left')
    lbnama2.grid(row=7,column=1)
    lbminum = Label(top,font = ("Helvetica",15), text = "Pilih kue ulang tahun :").place (x = 5, y = 120)
    lbhb = Label(top,font = ("Helvetica",15),text = "Beli berapa :").place(x=5, y=330)
 
psn = StringVar(value='...') 
class kueultah:
    R1 = Radiobutton(top, text="Blackforest cake       Rp. 150.000",font = ("Helvetica",15), variable=radio, value=1).place(x=150, y=120)  
    R2 = Radiobutton(top, text="Cheese cake            Rp. 100.000",font = ("Helvetica",15), variable=radio, value=2).place(x=150, y=150)  
    R3 = Radiobutton(top, text="Chocolate cake         Rp. 120.000",font = ("Helvetica",15), variable=radio, value=3).place(x=150, y=180)  
    R4 = Radiobutton(top, text="Red Velvet cake        Rp. 200.000",font = ("Helvetica",15), variable=radio, value=4).place(x=150, y=210)  
    R5 = Radiobutton(top, text="Cinnamon cake          Rp. 175.000",font = ("Helvetica",15), variable=radio, value=5).place(x=150, y=240)
    R6 = Radiobutton(top, text="Rainbow cake           Rp. 130.000",font = ("Helvetica",15), variable=radio, value=5).place(x=150, y=270) 
    R7 = Radiobutton(top, text="Pound cake             Rp. 110.000",font = ("Helvetica",15), variable=radio, value=5).place(x=150, y=300) 
    
    def setlabel(self, top):
        self.lbkueultah = top
        pass
     
    def settop(self):
        return self.lbkueultah 
Dt1 = ttk.Combobox(top, width = 5, textvariable = psn, state="readonly")
Dt1.place(x=140, y=335)
Dt1['values'] = ('1',
                 '2',
                 '3',
                 '4',
                 '5') 
def function_perintah():
    perkenalan=""
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error","Belum mengisi nama")

    if radio.get()== 0:
        messagebox.showerror("Error","Belum memilih kue")

    if psn.get() == '...':
        messagebox.showerror("Error","Belum memilih beli berapa")
        return
    pesan = "Halo " + perkenalan + stringnama.get() + " \nMembeli " + psn.get() + " kue \nTerima kasih sudah datang"
    messagebox.showinfo("TOKO KUE ULANG TAHUN", pesan)
btn1 = Button(top, command = function_perintah, text="KIRIM").place(x=120,y=380)

top.mainloop()
