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
       if (nom == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Nombre")
       if (pro == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Producto")
       if (can == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Cantidad")    
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
       
       if(nom1 == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Nombre")
       if (area == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Area")
       if (pue == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Puesto")        
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
       
       if(nom2 == ""):
           messagebox.showwarning("Aviso","Falto ingresar el dato Nombre")
       if(pro2 == ""):
           messagebox.showwarning("Aviso","Falto ingresar el dato Producto")
       if(can2 == ""):
           messagebox.showwarning("Aviso","Falto ingresar el dato Cantidad")
            
            
           
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
       
       if(nom3 == ""):
           messagebox.showwarning("aviso","falto ingresar el dato Nombre")
       if(area2 == ""):
           messagebox.showwarning("aviso","falto ingresar el dato Area")
       if(serie == ""):
           messagebox.showwarning("aviso","falto ingresar el dato Noｺ serie")
       if(can3 == ""):
           messagebox.showwarning("aviso","falto ingresar el dato Cantidad")   
       if(fecha == ""):
           messagebox.showwarning("aviso","falto ingresar el dato Fecha") 
           
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
        if area == "":
            messagebox.showinfo("Aviso","Falto ingresar el Area")
        if id == "":
            messagebox.showinfo("Aviso","Falto ingresar el ID")
        if (area == "clientes"):
            res=messagebox.askyesno("Alerta","Desea borrar registro de la bd")
            if res:
                cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
                messagebox.showinfo("Confirmacion","Se a eliminado correctamente de la BD")
            else:
                pass
        elif (area == "empleados"):
            res=messagebox.askyesno("Alerta","Desea borrar registro de la bd")
            if res:
                cursor.execute("DELETE FROM empleados WHERE id=?", (id,))
                messagebox.showinfo("Confirmacion","Se a eliminado correctamente de la BD")
            else:
                pass
            
        elif (area == "provedores"):
            res=messagebox.askyesno("Alerta","Desea borrar registro de la bd")
            if res:
                cursor.execute("DELETE FROM provedores WHERE id=?", (id,))
                messagebox.showinfo("Confirmacion","Se a eliminado correctamente de la BD")
            else:
                pass
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
        resp=messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        if resp:
            cursor.execute("DELETE FROM entradas WHERE id=?", (id,))
            messagebox.showinfo("Confirmacion","Se a eliminado correctamente de la BD")
        else:
            pass
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
    def buscarempleado(self,area,id):
        conx=self.conexionBD()
        if(area == ""):
            messagebox.showwarning("Cuidado","El ID es invalido o esta vacio")
            conx.close()
        if id == "":
            messagebox.showinfo("Aviso","Falto ingresar el ID")
            conx.close()
        else:
            try:
                if(area == "clientes"):
                    if(id == ""):
                        messagebox.showinfo("Error","Usuario no existe")
                        conx.close()
                        
                    else:   
                        cursor=conx.cursor()
                        selectQry="select * from clientes where id="+id
                        cursor.execute(selectQry)
                        rsUsuario=cursor.fetchall()
                        conx.close()
                        return rsUsuario
                if(area== "empleados"):
                    if(id == ""):
                        messagebox.showinfo("Error","Usuario no existe")
                        conx.close()
                    else:   
                        cursor=conx.cursor()
                        selectQry="select * from empleados where id="+id
                        cursor.execute(selectQry)
                        rsUsuario=cursor.fetchall()
                        conx.close()
                        return rsUsuario
                if(area == "provedores"):
                    if(id == ""):
                        messagebox.showinfo("Error","Usuario no existe")
                        conx.close()
                    else:   
                        cursor=conx.cursor()
                        selectQry="select * from provedores where id="+id
                        cursor.execute(selectQry)
                        rsUsuario=cursor.fetchall()
                        conx.close()
                        return rsUsuario
            except sqlite3.OperationalError:
                print("Error de consulta")
    def buscarentrada(self,id):
        conx=self.conexionBD()
        if (id == ""):
            messagebox.showerror("Error","No se encontro en BD")
            conx.close()
        else:
            cursor=conx.cursor()
            selectQry="select * from entradas where id="+id
            cursor.execute(selectQry)
            rsUsuario1=cursor.fetchall()
            conx.close()
            return rsUsuario1