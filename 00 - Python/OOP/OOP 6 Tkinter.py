import tkinter

main_window = tkinter.Tk()

label1 =tkinter.Label(main_window, text= "Label1")
label2 =tkinter.Label(main_window, text= "Label2")
button1 = tkinter.Button(main_window, text= 'Tombol')

# Method positioning
label1.pack()
label2.pack()
button1.pack()

# Method menampilkan GUI
main_window.mainloop()

# Huruf besar adalah kelas
# Huruf kecil adalah method atau fungsi