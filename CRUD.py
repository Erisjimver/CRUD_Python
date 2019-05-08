from tkinter import *
from tkinter import messagebox
import sqlite3



root=Tk()
root.iconbitmap("icono.ico")
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miFrameButton=Frame(root,width=500,height=200)
miFrameButton.pack()
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

#---------------------VARIABLES-------------------------

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


#---------------------FUNCIONES-------------------------
def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIO (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			APELLIDOS VARCHAR(50),
			PASSWORD VARCHAR(50),		
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100)
			)
			''')
		messagebox.showinfo("BBDD", "BBDD creada con exito")
	except:
		messagebox.showwarning("!Atencion!","La base de datos ya existe")

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miPass.set("")
	miDireccion.set("")
	textoComentarios.delete(1.0,END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIO VALUES(NULL,'"+miNombre.get()+
		"','"+miApellido.get()+
		"','"+miPass.get()+
		"','"+miDireccion.get()+
		"','"+textoComentarios.get("1.0",END)+"')")

	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con exito")

def crear2():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	datos=miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get(),textoComentarios.get("1.0",END)
	miCursor.execute("INSERT INTO DATOSUSUARIO VALUES (NULL,?,?,?,?,?)",datos)

	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con exito")

def leer():
	
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID="+miId.get())
	elusuario=miCursor.fetchall()
	for usuario in elusuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miApellido.set(usuario[2])
		miPass.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentarios.insert(1.0,usuario[5])
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO='"+miNombre.get()+
		"',APELLIDOS='"+miApellido.get()+
		"',PASSWORD='"+miPass.get()+
		"',DIRECCION='"+miDireccion.get()+
		"',COMENTARIOS='"+textoComentarios.get("1.0",END)+
		"' WHERE ID="+miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con exito")

def actualizar2():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	datos=miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get(),textoComentarios.get("1.0",END)
	miCursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO=?, APELLIDOS=?,PASSWORD=?,DIRECCION=?,COMENTARIOS=?"
		" WHERE ID="+miId.get(),datos)

	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()	

	miCursor.execute("DELETE FROM DATOSUSUARIO WHERE ID="+miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro eliminado con exito")

def informaconAdicional():
	
	messagebox.showinfo("prcoesador de Israel", "procesador de textos version 2019")

def avisoLicencia():
	
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	valor=messagebox.askokcancel("Salir","Deseas Salir de la aplicacion?")
	#valor=messagebox.askquestion("Salir","Deseas Salir de la aplicacion?")
	if valor == True:
		root.destroy()

def cerrarDocumento():
	valor= messagebox.askretrycancel("Reintentar","No es posible cerrar, documento bloqueado")
	if valor == False:
		root.destroy()

def codigoBoton():
	miNombre.set("Israel")


#---------------MENU------------------------

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Conectar",command=conexionBBDD)
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Borrar",command=limpiarCampos)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoCRUD=Menu(barraMenu,tearoff=0)
archivoCRUD.add_command(label="Crear",command=crear2)
archivoCRUD.add_command(label="Leer",command=leer)
archivoCRUD.add_command(label="Actualizar",command=actualizar2)
archivoCRUD.add_command(label="Borrar",command=eliminar)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=informaconAdicional)


barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="CRUD",menu=archivoCRUD)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


#-----------------labels---------------------------------
labelId=Label(miFrame,text="Id:")
labelId.grid(row=0,column=0,sticky="w",padx=8,pady=2)

labelNombre=Label(miFrame,text="Nombre:")
labelNombre.grid(row=1,column=0,sticky="w",padx=8,pady=2)

labelApellido=Label(miFrame,text="Apellido:")
labelApellido.grid(row=2,column=0,sticky="w",padx=8,pady=2)

labelPass=Label(miFrame,text="Password:")
labelPass.grid(row=3,column=0,sticky="w",padx=8,pady=2)

labelDireccion=Label(miFrame,text="Direccion:")
labelDireccion.grid(row=4,column=0,sticky="w",padx=8,pady=2)

labelComentarios=Label(miFrame,text="Comentarios:")
labelComentarios.grid(row=5,column=0,sticky="w",padx=8,pady=2)


#--------------------cajas de texto----------------------
cuadroId=Entry(miFrame,textvariable=miId)
cuadroId.grid(row=0,column=1,padx=8,pady=2)
cuadroId.config(fg="blue",justify="right")

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=8,pady=2)
cuadroNombre.config(fg="blue",justify="right")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=2,column=1,padx=8,pady=2)
cuadroApellido.config(fg="blue",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=3,column=1,padx=8,pady=2)
cuadroPass.config(fg="red",justify="right",show="*")

#cuadroPass.config(show="*")#pone astiriscos en el campo password
cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=8,pady=2)
cuadroDireccion.config(fg="blue",justify="right")

textoComentarios=Text(miFrame,width=15,height=5)
textoComentarios.grid(row=5,column=1,padx=8,pady=2)
scrollVert=Scrollbar(miFrame,command=textoComentarios.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentarios.config(yscrollcommand=scrollVert.set)


#---------------BOTONES-----------------------
	
botonCrear=Button(miFrameButton,text="Create",command=crear)
botonCrear.grid(row=1, column=0,sticky="e",padx=10,pady=10)
#botonCrear.pack()
botonLeer=Button(miFrameButton,text="Read",command=leer)
botonLeer.grid(row=1, column=1,sticky="e",padx=10,pady=10)
#botonLeer.pack()
botonActualiza=Button(miFrameButton,text="Update",command=actualizar)
botonActualiza.grid(row=1, column=2,sticky="e",padx=10,pady=10)
#botonActualiza.pack()
botonBorrar=Button(miFrameButton,text="Delete",command=eliminar)
botonBorrar.grid(row=1, column=3,sticky="e",padx=10,pady=10)
#botonBorrar.pack()



root.mainloop()