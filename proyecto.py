from asyncio import FIRST_EXCEPTION
from logicapi import *
import threading 
import tkinter as tk

acciones=logicap()


def guardarc():
   acciones.guardarcliente(nombrec.get(),productoc.get(),cantidadc.get())
   
def guardare():
   acciones.guardarempleado(nombree.get(),areae.get(),puestoe.get())
   
def guardarp():
   acciones.guardarprovedor(nombrep.get(),productop.get(),cantidadp.get())
def tabla():
    return acciones.mostrartablacliente()
def actualizar_tabla():
    for uno in a.get_children():
            a.delete(uno)
    datos=tabla()
    for b, row in enumerate(datos):
            a.insert("", "end", text=str(b+1), values=row)
    if datos==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
def nuevo() :
    prueba1=threading.Thread(target=actualizar_tabla)
    prueba1.start()
def tabla1():
    return acciones.mostrartablaempleados()
def actualizar_tablae():
    for uno1 in d.get_children():
            d.delete(uno1)
    datos1=tabla1()
    for e, row in enumerate(datos1):
            d.insert("", "end", text=str(e+1), values=row)
    if datos1==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
def nuevo2() :
    prueba2=threading.Thread(target=actualizar_tablae)
    prueba2.start()
def tabla2():
    return acciones.mostrartablaeprovedores()
def actualizar_tablap():
    for uno2 in f.get_children():
            f.delete(uno2)
    datos2=tabla2()
    for h, row in enumerate(datos2):
            f.insert("", "end", text=str(h+1), values=row)
    if datos2==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
def nuevo3() :
    prueba3=threading.Thread(target=actualizar_tablap)
    prueba3.start()
    
def eliminacion():
   acciones.eliminar_registro(areaaa.get(),iddd.get())
def actual():
   acciones.mactualizarclientes(id.get(),nom.get(),pro.get(),cand.get())
def actuali():
   acciones.mactualizarempleados(id2.get(),nom2.get(),are.get(),pue.get())
def actualiz():
   acciones.mactualizarprovedores(id3.get(),nom3.get(),pro3.get(),cand3.get())
def buscador():
   usuario= acciones.buscarempleado(areab.get(),idb.get())
   if areab.get()=="clientes":
      for usu in usuario:
        cadena="ID: "+str(usu[0])+" ,"+ "Nombre: "+str( usu[1])+", "+"Producto: "+ str(usu[2])+" ,"+"Cantidad: " +str(usu[3])
   elif areab.get()=="empleados":
      for usu in usuario:
        cadena="ID: "+str(usu[0])+" ,"+ "Nombre: "+str( usu[1])+", "+"Area: "+ str(usu[2])+" ,"+"Puesto: " +str(usu[3])
   if areab.get()=="provedores":
      for usu in usuario:
        cadena="ID: "+str(usu[0])+" ,"+ "Nombre: "+str( usu[1])+", "+"Producto: "+ str(usu[2])+" ,"+"Cantidad: " +str(usu[3])
   if(usuario):
      print(cadena)
   else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")
   textenc.insert(tk.INSERT,cadena)


# ventanas base de datos

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()




#registro clientes
    
    
clientes = Frame(note,width=400,height=400)
clientes.pack(expand=True,fill='both')
note.add(clientes,text="R. Clientes")
texto=Label(clientes,text="registro de clientes")


texto=Label(clientes,text="nombre")
texto.place(x=20, y=20)
nombrec=StringVar()
nombre1=Entry(clientes,textvariable=nombrec)
nombre1.place(x=110, y=20)

texto=Label(clientes,text="id de producto")
texto.place(x=20, y=60)
productoc=StringVar()
producto1=Entry(clientes,textvariable=productoc)
producto1.place(x=110, y=60)

texto=Label(clientes,text="cantidad:")
texto.place(x=20, y=100)
cantidadc=StringVar()
cantidad1=Entry(clientes,textvariable=cantidadc)
cantidad1.place(x=110, y=100)

boton=Button(clientes,text="registrar",command=guardarc)
boton.place(x=150, y=140)





#registrar empleados 

    
empleados = Frame(note,width=400,height=400)
empleados.pack(expand=True,fill='both')
note.add(empleados,text="R. Empleados")
texto=Label(empleados,text="registro de empleados")

texto=Label(empleados,text="nombre")
texto.place(x=20, y=20)
nombree=StringVar()
nombre2=Entry(empleados,textvariable=nombree)
nombre2.place(x=110, y=20)

texto=Label(empleados,text="area")
texto.place(x=20, y=60)
areae=StringVar()
area1=Entry(empleados,textvariable=areae)
area1.place(x=110, y=60)

texto=Label(empleados,text="puesto")
texto.place(x=20, y=100)
puestoe=StringVar()
puesto1=Entry(empleados,textvariable=puestoe)
puesto1.place(x=110, y=100)

boton=Button(empleados,text="registrar",command=guardare)
boton.place(x=150, y=140)


#provedores 


provedores= Frame(note,width=400,height=280)
provedores.pack(expand=True,fill='both')
note.add(provedores,text="R. Provedores")
texto=Label(provedores,text="registrar provedores")

texto=Label(provedores,text="nombre")
texto.place(x=20, y=20)
nombrep=StringVar()
nombre3=Entry(provedores,textvariable=nombrep)
nombre3.place(x=110, y=20)

texto=Label(provedores,text="id productos")
texto.place(x=20, y=60)
productop=StringVar()
producto2=Entry(provedores,textvariable=productop)
producto2.place(x=110, y=60)

texto=Label(provedores,text="cantidad")
texto.place(x=20, y=100)
cantidadp=StringVar()
cantidad2=Entry(provedores,textvariable=cantidadp)
cantidad2.place(x=110, y=100)

boton=Button(provedores,text="registrar",command=guardarp)
boton.place(x=150, y=140)

# consultar clientes
cclientes= Frame(note,width=400,height=280)
cclientes.pack(expand=True,fill='both')
note.add(cclientes,text="Consultas")
texto=Label(cclientes,text="Consulta de clientes").pack()
botonconsultar=Button(cclientes,text="Consultar",command=nuevo).pack()
 
col=('id','nombre', 'producto','cantidad')
a=ttk.Treeview(cclientes,col=col ,show='headings' ,height=5)
a.heading('id', text='ID',anchor=CENTER)
a.heading('nombre',text='Nombre',anchor=CENTER)
a.heading('producto',text='Producto',anchor=CENTER)
a.heading('cantidad', text='Cantidad',anchor=CENTER)
a.pack(padx=5, pady=5)
datos=tabla()
for b, row in enumerate(datos):
   a.insert('', 'end' , text=str(b+1), values =row)
   if datos==[]:
      messagebox.showinfo("Error","La Base de Datos esta vacia.")
# consultar empleados
texto=Label(cclientes,text="Consulta de Empleados").pack()
botonconsultare=Button(cclientes,text="Consultar",command=nuevo2).pack()
colu=('id','nombre', 'area','puesto')
d=ttk.Treeview(cclientes,colu=colu ,show='headings' ,height=5)
d.heading('id', text='ID',anchor=CENTER)
d.heading('nombre',text='Nombre',anchor=CENTER)
d.heading('area',text='Area',anchor=CENTER)
d.heading('puesto', text='Puesto',anchor=CENTER)
d.pack(padx=5, pady=5)
datos1=tabla1()
for e, row in enumerate(datos1):
   d.insert('', 'end' , text=str(e+1), values =row)
   if datos1==[]:
      messagebox.showinfo("Error","La Base de Datos esta vacia.")
   
# consultar provedores
texto=Label(cclientes,text="Consulta de Provedores").pack()
botonconsultare=Button(cclientes,text="Consultar",command=nuevo3).pack()
colu=('id','nombrep', 'productop','cantidadp')
f=ttk.Treeview(cclientes,colu=colu ,show='headings' ,height=5)
f.heading('id', text='ID',anchor=CENTER)
f.heading('nombrep',text='Nombre',anchor=CENTER)
f.heading('productop',text='Producto',anchor=CENTER)
f.heading('cantidadp', text='Cantidad',anchor=CENTER)
f.pack(padx=5, pady=5)
datos2=tabla2()
for h, row in enumerate(datos2):
   f.insert('', 'end' , text=str(h+1), values =row)
   if datos2==[]:
      messagebox.showinfo("Error","La Base de Datos esta vacia.")

# eliminar regitro de cualquier area

eliminar= Frame(note,width=400,height=280)
eliminar.pack(expand=True,fill='both')
note.add(eliminar,text="Eliminar Registro")
texto=Label(eliminar,text="Ingrese Area a eliminar").pack()
areaaa=StringVar()
area1=Entry(eliminar,textvariable=areaaa).pack()
texto=Label(eliminar,text="Ingrese ID a eliminar").pack()
iddd=StringVar()
id1=Entry(eliminar,textvariable=iddd).pack()
botoneliminar=Button(eliminar,text="Eliminar",command=eliminacion).pack()

#actualizar datos 
actualizar= Frame(note,width=400,height=280)
actualizar.pack(expand=True,fill='both')
note.add(actualizar,text="Actualizar Registro")
titulo=Label(actualizar,text="Actualizar datos del Cliente",fg="red").place(x=20, y=0)
titulo=Label(actualizar,text="Ingrese ID que desee Actualizar").place(x=20, y=22)
id=StringVar()
id1=Entry(actualizar,textvariable=id).place(x=40, y=40)
titulo=Label(actualizar,text="Ingrese nuevo Nombre").place(x=20, y=62)
nom=StringVar()
nom1=Entry(actualizar,textvariable=nom).place(x=40, y=80)
titulo=Label(actualizar,text="Ingrese nuevo Producto").place(x=20, y=104)
pro=StringVar()
pro1=Entry(actualizar,textvariable=pro).place(x=40, y=120)
titulo=Label(actualizar,text="Ingrese nueva Cantidad").place(x=20, y=146)
cand=StringVar()
can1=Entry(actualizar,textvariable=cand).place(x=40, y=168)
botonact=Button(actualizar,text="Actualizar",command=actual).place(x=60, y=190)
#actualizar datos empleado
titulo=Label(actualizar,text="Actualizar datos del Empleado",fg="red").pack()
titulo=Label(actualizar,text="Ingrese ID que desee Actualizar").pack()
id2=StringVar()
id22=Entry(actualizar,textvariable=id2).pack()
titulo=Label(actualizar,text="Ingrese nuevo Nombre").pack()
nom2=StringVar()
nom22=Entry(actualizar,textvariable=nom2).pack()
titulo=Label(actualizar,text="Ingrese nuevo Area").pack()
are=StringVar()
are1=Entry(actualizar,textvariable=are).pack()
titulo=Label(actualizar,text="Ingrese nueva Puesto").pack()
pue=StringVar()
pue1=Entry(actualizar,textvariable=pue).pack()
botonactu=Button(actualizar,text="Actualizar",command=actuali).pack()
#actualizar datos del provedor
titulo=Label(actualizar,text="Actualizar datos del Provedor",fg="red").place(x=600, y=0)
titulo=Label(actualizar,text="Ingrese ID que desee Actualizar").place(x=600, y=22)
id3=StringVar()
id33=Entry(actualizar,textvariable=id3).place(x=640, y=40)
titulo=Label(actualizar,text="Ingrese nuevo Nombre").place(x=620, y=62)
nom3=StringVar()
nom33=Entry(actualizar,textvariable=nom3).place(x=640, y=80)
titulo=Label(actualizar,text="Ingrese nuevo Producto").place(x=620, y=104)
pro3=StringVar()
pro33=Entry(actualizar,textvariable=pro3).place(x=640, y=120)
titulo=Label(actualizar,text="Ingrese nueva Cantidad").place(x=620, y=146)
cand3=StringVar()
can33=Entry(actualizar,textvariable=cand3).place(x=640, y=168)
botonact=Button(actualizar,text="Actualizar",command=actualiz).place(x=660, y=190)

#buscar 
buscar= Frame(note,width=400,height=280)
buscar.pack(expand=True,fill='both')
note.add(buscar,text="Buscar")
titulo=Label(buscar,text="Ingrese los Datos").pack()
titulo=Label(buscar,text="Ingrese Area a buscar").pack()
areab=StringVar()
areabb=Entry(buscar,textvariable=areab).pack()
titulo=Label(buscar,text="Ingrese ID a buscar",fg="red").pack()
idb=StringVar()
idbb=Entry(buscar,textvariable=idb).pack()
textenc=tk.Text(buscar,height=5,width=52)
textenc.pack()
botonbusqueda=Button(buscar,text="buscar",command=buscador).pack()
ventana.mainloop()
