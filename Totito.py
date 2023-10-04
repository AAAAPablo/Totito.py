from tkinter import*
from tkinter import messagebox
ventana=Tk()
ventana.geometry("700x500")

ventana.title("Totito")

# X verdadero
click=True
contador=0

#Resetear funcuines
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global click,contador
    click=True
    contador=0

# Deshabilitar botones
def Bloquear_botones():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Verificación de los If
def verificar():
    global gana
    gana=False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] =="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X") #Se definen automaticamente las etiquetas solamente es de continuar escribiendo
        Bloquear_botones()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] =="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] =="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] =="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] =="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] =="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] =="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] =="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó X")
        Bloquear_botones()

        ### verificar O 


    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] =="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] =="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] =="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] =="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] =="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] =="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O Wins!!")
        Bloquear_botones()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] =="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] =="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        gana=True
        messagebox.showinfo("Totito","Felicitaciones ganó O")
        Bloquear_botones()


def b_click(b):
    global click,contador

    if b["text"] ==" " and click==True:
        b["text"]="X"
        click=False
        contador+=1
        verificar()

    elif b["text"] ==" " and click==False:
        b["text"]="O"
        click=True
        contador+=1
        verificar

    else:
        messagebox.showerror("Totito", "La casilla seleccionada ya se marcó")

#Programación de botones
b1=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b1))
b2=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b2))
b3=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b3))

b4=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b4))
b5=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b5))
b6=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b6))

b7=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b7))
b8=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b8))
b9=Button(ventana,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b9))

#Botones en pantalla
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid (row=0,column=2)

b4.grid (row=1,column=0)
b5.grid (row=1,column=1)
b6.grid (row=1,column=2)

b7.grid (row=2,column=0)
b8.grid (row=2,column=1)
b9.grid (row=2,column=2)

# Crear menú
my_menu=Menu(ventana)
ventana.config(menu=my_menu)

# Crear menú de opciones
options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="optciones",menu=options_menu)
options_menu.add_command(label='Reiniciar jeugo',command=reset)
reset()
ventana.mainloop ()
