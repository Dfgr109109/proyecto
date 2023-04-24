import sqlite3
from sqlite3 import Error
from datetime import datetime
def conexion_db():
    try:
        con = sqlite3.connect('Nueva.db')
        return con
    except Error:
        print(Error)
def crear_tabla_atleta(con):
    cursorObj =con.cursor()
    cadena='''CREATE TABLE IF NOT EXISTS atleta(
                NoIdAtleta TEXT NOT NULL,
                NoInscripcion INTEGER NOT NULL,
                Nombre TEXT,
                Apellido TEXT,
                FechaNacimiento DATE, 
                PaisOrigen TEXT,
                CiudadOrigen TEXT,
                PRIMARY KEY (NoIdAtleta, NoInscripcion))'''
    cursorObj.execute(cadena)
    con.commit()
def ingresar():
    NoIdAtleta=input("Identificacion del atleta:")
    NoIdAtleta=NoIdAtleta.ljust(12)
    NoInscipcion=input("Numero de Inscripcion del atleta:")
    NoInscipcion=NoInscipcion.ljust(12)
    Nombre=input("Nombre del atleta:").upper()
    Nombre=Nombre.ljust(12)
    Apellido=input("Apellido del atleta:").upper()
    Apellido=Apellido.ljust(12)
    FechaNacimientoEntrada=input("Fecha de nacimiento (AAAA-MM-DD):")
    FechaNacimiento=datetime.strptime(FechaNacimientoEntrada,'%Y-%m-%d').date() #El date es para quitar segundos, minutos, horas
    PaisOrigen=input("Pais de origen del atleta:").upper()
    PaisOrigen=PaisOrigen.ljust(12)
    CiudadOrigen=input("Ciudad de origen del atleta:").upper()
    CiudadOrigen=CiudadOrigen.ljust(12)
    atleta=(NoIdAtleta, NoInscipcion, Nombre, Apellido, FechaNacimiento, PaisOrigen, CiudadOrigen)
    return atleta
def insertar_tabla_atleta(con, atleta):
    cursorObj =con.cursor()
    cadena='INSERT INTO atleta VALUES (?,?,?,?,?,?,?)'
    cursorObj.execute(cadena, atleta)
    con.commit()
def consultar_atleta(con):
    CursorObj=con.cursor()
    #cad='SELECT NoIdAtleta, NoInscripcion FROM atleta WHERE Nombre LIKE "%PAO%"'
    #cad='SELECT * FROM atleta WHERE Nombre LIKE "%PAOLA%"'
    cad='SELECT * FROM atleta WHERE NoInscripcion=1'
    CursorObj.execute(cad)
    filas=CursorObj.fetchall()
    print(type(filas))
    for row in filas:
        NoIdAtleta=row[0]
        NoInscripcion=row[1]
        print("La identificacion del atleta es: ", NoIdAtleta)
        print("El numero de inscripcion del atleta es: ", NoInscripcion)
    print(row)
def consultar(con):
    CursorObj =con.cursor()
    cadena='SELECT count(*) FROM atleta'
    CursorObj.execute(cadena)
    cantidad = CursorObj.fetchall()
    print(cantidad[0])
    for row in cantidad:
        cantidadatletas=row[0]
        
    cadena='SELECT SUM(NoInscripcion) FROM atleta'
    CursorObj.execute(cadena)
    Sumatoria = CursorObj.fetchall()
    print(type(Sumatoria[0]))
    for row in Sumatoria:
        suma=row[0]
    print("Sumatoria=", suma)
def actualizar_atleta(con):
    CursorObj=con.cursor()
    NoInscripcion = input("NoInscripcion: ")
    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    cadena=f'UPDATE atleta SET Nombre = "{Nombre}", Apellido = "{Apellido}" WHERE NoInscripcion LIKE "{NoInscripcion}%"'
    CursorObj.execute(cadena)
    con.commit()
def borrar_info_atleta(con):
    CursorObj=con.cursor()
    Nombre = input("Nombre: ")
    cadena=f'DELETE FROM atleta WHERE Nombre LIKE "{Nombre}%"'
    CursorObj.execute(cadena)
    con.commit()
def borrar_tabla(con):
    CursorObj=con.cursor()
    cadena=f'DROP TABLE atelta'
    CursorObj.execute(cadena)
    con.commit()    
                 
def menu_atleta(con):
    CursorObj=con.cursor()
    cadena="""
Digite 1 para ingresar atleta
Digite 2 para consultar atleta
Digite 3 para actualizar atleta
Digite 4 para borrar atleta

"""
    entrada=input(cadena)
    entrada=int(entrada)
    if entrada==1:
        atletacreado=ingresar()
        insertar_tabla_atleta(con, atletacreado)
    elif entrada==2:
        consultar(con)
    elif entrada==3:
        actualizar_atleta(con)
    elif entrada==4:
        borrar_info_atleta(con)
    con.commit()    
def cerrarConexionBD(con):
    con.close()
def main():
    conex=conexion_db()
    #crear_tabla_atleta(conex)
    menu_atleta(conex)
    #borrar_info_atleta(conex)
    #borrar_tabla(conex)
    cerrarConexionBD(conex)
main()
