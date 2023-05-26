from tkinter import *
import os
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 1, 4))

sorting_ascending = True 

root = Tk()
root.title("Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "../assets/rumah.png")

    logo_image = PhotoImage(file=image_path)
    top.image = logo_image

    frame = LabelFrame(top, padx=10, pady=10, width=400, height=300)
    frame.pack(padx=10, pady=10)
    
    frame_label = Label(frame, image=logo_image)
    frame_label.pack()

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.pack()

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.pack()

def daftar():
    top = Toplevel()
    top.title("Daftar Residen")

    sorted_hunians = sorted(hunians, key=lambda h: h.get_nama_pemilik(), reverse=not sorting_ascending)

    frame = LabelFrame(top, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    for index, h in enumerate(sorted_hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type_label.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name_label = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)
        else:
            name_label = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    sort_btn = Button(top, text="Ubah Urutan", command=toggle_sorting)
    sort_btn.pack()

    b_close = Button(top, text="Close", command=top.destroy)
    b_close.pack()

def toggle_sorting():
    global sorting_ascending
    sorting_ascending = not sorting_ascending
    daftar()  

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "../assets/hunian.png")

logo_image = PhotoImage(file=image_path)
frame = LabelFrame(root, padx=10, pady=10, width=400, height=300)
frame.pack(padx=10, pady=10)

frame_label = Label(frame, text="RESIDEN HUNIAN")
frame_label.pack()
frame_label = Label(frame, image=logo_image)
frame_label.pack()

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_daftar = Button(opts, text="Lihat Daftar Residen", command=daftar)
b_daftar.grid(row=0, column=0)

root.mainloop()

# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="db_praktikum"
# )

# dbcursor = mydb.cursor()

# sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
# val = ("Indah", "Jalan Soekarno Hatta")
# dbcursor.execute(sql, val)

# mydb.commit()

# print(dbcursor.rowcount, "record inserted.")

# dbcursor = mydb.cursor()

# dbcursor.execute("SELECT * FROM customers")

# myresult = dbcursor.fetchall()

# for x in myresult:
#     print(x)
    
# dbcursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE name = 'Indah'"

# dbcursor.execute(sql)

# mydb.commit()

# print(dbcursor.rowcount, "record(s) deleted")