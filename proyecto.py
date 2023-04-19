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
    print(type(cantidad[0]))
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
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cadena=f'UPDATE atleta SET nombre = "{nombre}", apellido = "{apellido}" WHERE NoInscripcion LIKE "{NoInscripcion}%"'
    CursorObj.execute(cadena)
    print(cadena)
    con.commit()
    
def main():
    conex=conexion_db()
    crear_tabla_atleta(conex)
    #atletacreado=ingresar()
    #insertar_tabla_atleta(conex, atletacreado)
    #consultar_atleta(conex)
    #consultar(conex)
    actualizar_atleta(conex)
main()
