from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt


class logicap:
    
    def __init__(self) -> None:
        pass
    
    
    #conexion 
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/EMMANUEL NORIEGA/Desktop/github/pryecto/PROYECTO INTEGRADOR.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")
            
            
    def guardarcliente (self,nom,pro,can):
        
       conx=self.conexionBD()
       
       if(nom == "" or pro=="" or can ==""):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom,pro,can)
           qrisert="insert into clientes (nombre,producto,cantidad) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
    def guardarempleado (self,nom1,area,pue):
        
       conx=self.conexionBD()
       
       if(nom1 == "" or area==""  or pue==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom1,area,pue)
           qrisert="insert into empleados (nombre,area,puesto) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def guardarprovedor (self,nom2,pro2,can2):
        
       conx=self.conexionBD()
       
       if(nom2 == "" or pro2=="" or can2 ==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom2,pro2,can2)
           qrisert="insert into provedores (nombrep,productop,cantidadp) values (?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
           
    def registraentrada (self,nom3,area2,serie,can3,fecha):
        
       conx=self.conexionBD()
       
       if(nom3 == "" or area2=="" or serie =="" or can3 =="" or fecha =="" ):
           messagebox.showwarning("aviso","fomulario incompleto")
           
       else:
           
           cursor=conx.cursor()
           datos=(nom3,area2,serie,can3,fecha)
           qrisert="insert into entradas (nombre,area,serie,cantidad,fecha) values (?,?,?,?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
    def mostrartablacliente(self):

            conx=self.conexionBD()
            cursor=conx.cursor()
            selectQry="select id,nombre,producto,cantidad from clientes"
            cursor.execute(selectQry)
            resultado=cursor.fetchall()
            conx.close()
            datos=[]
            for row in resultado:
                datos.append(list(row))
            return datos
    def mostrartablaempleados(self):

            conx=self.conexionBD()
            cursor=conx.cursor()
            selectQry="select id,nombre,area,puesto from empleados"
            cursor.execute(selectQry)
            resultado1=cursor.fetchall()
            conx.close()
            datos1=[]
            for row in resultado1:
                datos1.append(list(row))
            return datos1
    def mostrartablaeprovedores(self):

            conx=self.conexionBD()
            cursor=conx.cursor()
            selectQry="select id,nombrep,productop,cantidadp from provedores"
            cursor.execute(selectQry)
            resultado2=cursor.fetchall()
            conx.close()
            datos2=[]
            for row in resultado2:
                datos2.append(list(row))
            return datos2
    def eliminar_registro(self,area,id):
        conx=self.conexionBD()
        cursor=conx.cursor()
        if area == "clientes":
            cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
            messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        elif area == "empleados":
            cursor.execute("DELETE FROM empleados WHERE id=?", (id,))
            messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        elif area == "provedores":
            cursor.execute("DELETE FROM provedores WHERE id=?", (id,))
            messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        else:
            pass
            
        conx.commit()
        conx.close()
    def mactualizarclientes(self,id,nombre,producto,cantidad):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nom=nombre
                pro=producto
                can=cantidad
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE clientes SET nombre=?, producto=?, cantidad=? WHERE id=?", (nom,pro,can,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
    def mactualizarempleados(self,id,nombre,area,puesto):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nom=nombre
                are=area
                pue=puesto
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE empleados SET nombre=?, area=?, puesto=? WHERE id=?", (nom,are,pue,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
    def mactualizarprovedores(self,id,nombre,producto,cantidad):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nom=nombre
                can=cantidad
                pro=producto
                
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE provedores SET nombrep=?, productop=?, cantidadp=? WHERE id=?", (nom,pro,can,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
    def consulta_entradas(self):
         conx=self.conexionBD()
         cursor=conx.cursor()
         selectQry="select id,nombre,area,serie,cantidad,fecha from entradas"
         cursor.execute(selectQry)
         resultadoe=cursor.fetchall()
         conx.close()
         datose=[]
         for row in resultadoe:
             datose.append(list(row))  
         return datose 
    def eliminar_entradas(self,id):
        conx=self.conexionBD()
        cursor=conx.cursor()
        cursor.execute("DELETE FROM entradas WHERE id=?", (id,))
        messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        conx.commit()
        conx.close()
    def Actualizar_Entradas(self,id,nombre,area,serie,cantidad,fecha):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nom=nombre
                are=area
                se=serie
                can=cantidad
                fe=fecha
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE entradas SET nombre=?, area=?, serie=?,cantidad=?,fecha=? WHERE id=?", (nom,are,se,can,fe,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")