
from sys import exit
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

NAVY_BLUE = '#000080'
WHITE = '#FFFFFF'

class Menu():
    def __init__(self, names_buttons):
        if not isinstance(names_buttons, list):
            raise ValueError(f'Argument buttons {names_buttons} must be a list, correct it')
        else:
            self.names_buttons = names_buttons

        self.ventana = tk.Tk()
        self.ventana.title("Menu principal")
        self.ventana.geometry("400x400")
        self.BLUE_NAVY = NAVY_BLUE
        self.ventana.configure(bg=self.BLUE_NAVY)
        self.buttons = {}
        self.dibujar_botones()

    def dibujar_botones(self):
        self.number_buttons = len(self.names_buttons)
        for i in range(self.number_buttons):
            # Dibuja el boton
            self.buttons[self.names_buttons[i]] = tk.Button(self.ventana, text=f'{self.names_buttons[i]}', bg=WHITE,fg=self.BLUE_NAVY, height=20)
            # Establecer boton en la grid
            self.buttons[self.names_buttons[i]].grid(row=i, column=0, sticky="ew", padx=10, pady=10)
            # Expansion de peso de la fila
            self.ventana.grid_rowconfigure(i, weight=1)

        # Expansion de peso de la columna
        self.ventana.grid_columnconfigure(0, weight=1)
        
    def activar_menu(self):
        self.ventana.mainloop()


class Sistema():
    def __init__(self, conexion_bd):
        self.conexion_bd = conexion_bd
        self.nombre_botones = ['INSERTAR', 'ELIMINAR', 'MOSTRAR', 'ACTUALIZAR']
        self.menu_principal = Menu(self.nombre_botones)
        self.tipo_operacion = ''
        self.botones_primer_menu()
        self.menu_principal.activar_menu()

    def botones_primer_menu(self):
        self.menu_principal.buttons['INSERTAR'].configure(command = lambda:self.activar_segundo_menu(tipo_operacion='INSERTAR'))
        self.menu_principal.buttons['ELIMINAR'].configure(command = lambda:self.activar_segundo_menu(tipo_operacion='ELIMINAR'))
        self.menu_principal.buttons['MOSTRAR'].configure(command = lambda: self.activar_segundo_menu(tipo_operacion='MOSTRAR'))
        self.menu_principal.buttons['ACTUALIZAR'].configure(command = lambda:self.activar_segundo_menu(tipo_operacion='ACTUALIZAR'))

    def activar_segundo_menu(self, tipo_operacion):
        self.tipo_operacion = tipo_operacion
        self.menu_principal.ventana.withdraw()
        self.segundo_menu = Menu(['CANCION', 'ARTISTA', 'ALBUM', 'GENERO'])
        self.segundo_menu.ventana.protocol("WM_DELETE_WINDOW",lambda: self.volver_primer_menu())
        # Imprimir la indicacion del segundo menu
        self.indicacion_segundo_menu = tk.Label(self.segundo_menu.ventana,text=F'ELIGE LA ENTIDAD QUE QUIERES {self.tipo_operacion}')
        # Ajustar el segundo menu a la grid
        self.indicacion_segundo_menu.grid(row=self.segundo_menu.number_buttons + 1, column=0, 
                                          sticky="ew", padx=10, pady=10)
        # Activar los botones del segundo menu
        self.segundo_menu.buttons['CANCION'].configure(command=lambda:self.division_operacion(entidad_elegida='CANCION'))
        self.segundo_menu.buttons['ALBUM'].configure(command=lambda:self.division_operacion(entidad_elegida='ALBUM'))
        self.segundo_menu.buttons['ARTISTA'].configure(command=lambda:self.division_operacion(entidad_elegida='ARTISTA'))
        self.segundo_menu.buttons['GENERO'].configure(command=lambda:self.division_operacion(entidad_elegida='GENERO'))

    def division_operacion(self, entidad_elegida):
        self.entidad_elegida = entidad_elegida
        match self.tipo_operacion:
            case 'INSERTAR':
                match self.entidad_elegida:
                    case 'CANCION':
                        Insertar_Cancion(self.conexion_bd)
                    case 'ALBUM':
                        Insertar_Album(self.conexion_bd)
                    case 'ARTISTA':
                        Insertar_Artista(self.conexion_bd)
                    case 'GENERO':
                        Insertar_Genero(self.conexion_bd)
            case 'ELIMINAR':
                match self.entidad_elegida:
                    case 'CANCION':
                        Eliminar_cancion(self.conexion_bd)
                    case 'ALBUM':
                        Eliminar_Album(self.conexion_bd)
                    case 'ARTISTA':
                        Eliminar_Artista(self.conexion_bd)
                    case 'GENERO':
                        Eliminar_Genero(self.conexion_bd)
            case 'MOSTRAR':
                match self.entidad_elegida:
                    case 'CANCION':
                        Mostrar_Cancion(self.conexion_bd)
                    case 'ALBUM':
                        Mostrar_Album(self.conexion_bd)
                    case 'ARTISTA':
                        Mostrar_Artista(self.conexion_bd)
                    case 'GENERO':
                        Mostrar_Genero(self.conexion_bd)

            case 'ACTUALIZAR':
                match self.entidad_elegida:
                    case 'CANCION':
                        Actualizar(self.conexion_bd,'CANCION')
                    case 'ALBUM':
                        Actualizar(self.conexion_bd,'ALBUM')
                    case 'ARTISTA':
                        Actualizar(self.conexion_bd,'ARTISTA')
                    case 'GENERO':
                        Actualizar(self.conexion_bd,'GENERO')
        
    def volver_primer_menu(self):
        self.segundo_menu.ventana.destroy()
        self.menu_principal.ventana.deiconify()
        
class Insertar_Cancion():
    def __init__(self, coneccion):
        # Inicializar variables
        self.conexion_bd = coneccion
        self.cursor = coneccion.cursor()
        self.artista_a_buscar = ''

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title ('VENTANA PARA PEDIR ARTISTA')
        self.ventana_principal.geometry('250x150')
        self.ventana_principal.resizable(False,False)
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.indicacion = tk.Label(self.ventana_principal,text='INTRODUCE EL NOMBRE DE UN ARTISTA', bg=WHITE, fg=NAVY_BLUE)
        self.indicacion.grid(row=0, column=0, pady=5, padx=5, sticky='ew')
        self.entrada_artista = tk.Entry(self.ventana_principal, fg=NAVY_BLUE)
        self.entrada_artista.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        self.boton_buscar = tk.Button(self.ventana_principal, text="BUSCAR ARTISTA", fg=NAVY_BLUE, bg=WHITE, height=2)
        self.boton_buscar.grid(row=2, column=0, padx=10, pady=10, sticky='ew')  
        self.boton_buscar.config(command=self.buscar_artista)
        # Una vez se encuentre un artista valido
        self.ventana_principal.mainloop()

    def buscar_artista(self):
        artista_existe = False
        self.artista_a_buscar = self.entrada_artista.get()
        self.cursor.execute("SELECT COUNT(nombre) FROM artistas WHERE artistas.nombre = %s;", (self.artista_a_buscar,))
        self.artista_encontrado = self.cursor.fetchall()
        if self.artista_encontrado[0][0] == 0:
            messagebox.showwarning('ERROR', F'NO HAY ARTISTA CON EL NOMBRE {self.artista_a_buscar} EN LA BASE DE DATOS')
        else:
            artista_existe = True
            messagebox.showinfo('ARTISTA ENCONTRADO', F"El artista {self.artista_a_buscar} ha sido encontrado en la base de datos, Cierra la ventana para continuar")
        # Despues de que se cierre el messagebox

        if artista_existe:
            self.seleccionar_album()

        
    def seleccionar_album(self):
        # Preparar la ventana donde se escribiran los albums
        self.ventana_principal.withdraw()
        self.ventana_albums =  tk.Tk()
        self.ventana_albums.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())
        self.ventana_albums.title(f'Albums del artista {self.artista_a_buscar}')
        self.ventana_albums.geometry('400x450')
        self.ventana_albums.config(bg=NAVY_BLUE)
        # Imprimir la indicacion
        self.indicacion_select_albums = tk.Label(self.ventana_albums, text='Selecciona el album en el que quieres INSERTAR una cancion')
        self.indicacion_select_albums.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        # Imprimir los botones con los albums del artista
        # Pedir los datos a la base de datos
        self.cursor.execute("SELECT albums.nombre_album FROM albums JOIN artistas ON albums.artista_id = artistas.artista_id WHERE artistas.nombre = %s;", (self.artista_a_buscar,))
        self.albums_de_artista = self.cursor.fetchall()
        self.num_albums_artista = len(self.albums_de_artista)
        
        # Imprimir los datos en formato de boton
        self.botones_albums = {}
        for i in range(self.num_albums_artista):
            self.botones_albums[self.albums_de_artista[i][0]] = tk.Button(
                self.ventana_albums, text=f'Album: {self.albums_de_artista[i][0]}', bg=WHITE, fg=NAVY_BLUE,height=10
            )
            # Ajustar la grid
            self.botones_albums[self.albums_de_artista[i][0]].grid(row=i+1, column=0, sticky="ew", padx=10, pady=10)
                # Expansion de peso de la fila
            self.ventana_albums.grid_rowconfigure(i, weight=1)
            # Configurar el comando del boton
            self.botones_albums[self.albums_de_artista[i][0]].configure(command=lambda album=self.albums_de_artista[i][0]: self.insertar_cancion(album))
        self.ventana_albums.grid_columnconfigure(0, weight=1)

    def insertar_cancion(self, album):
        # Ventana para insertar la cancion en la base de datos
        self.ventana_albums.withdraw() # Retirar la ventana con los albums
        self.ventana_cancion = tk.Tk()
        self.ventana_cancion.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_ventana_albums())

        # Establecer la configuracion
        self.ventana_cancion.title('Ventana para introducir una cancion en la base de datos')
        self.ventana_cancion.geometry('400x450')
        self.ventana_cancion.config(bg=NAVY_BLUE)

        # Imprimir la indicacion de la ventana para introducir cancion
        self.indicacion_insert_cancion = tk.Label(self.ventana_cancion, 
                                                  text='Llena los siguientes campos para introducir una cancion')
        self.indicacion_select_albums.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # Introducir barras de texto
        # Nombre cancion, lyrics, numero de reproducciones
        # Entrada del nombre de la cancion
        indicacion_cancion = tk.Label(self.ventana_cancion, text='Introduce el nombre de la nueva cancion')
        indicacion_cancion.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.entrada_nombre = tk.Entry(self.ventana_cancion)
        self.entrada_nombre.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        # Entrada de las lyrics
        indicacion_lyrics = tk.Label(self.ventana_cancion, text='Introduce las Lyrics')
        indicacion_lyrics.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        self.entrada_lyrics = tk.Entry(self.ventana_cancion)
        self.entrada_lyrics.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

        # Entrada de los oyentes mensuales
        indicacion_oyentes = tk.Label(self.ventana_cancion, text='Introduce en un NUMERO ENTERO los oyentes mensuales')
        indicacion_oyentes.grid(row=5, column=0, sticky="ew", padx=10, pady=10)
        self.entrada_oyentes = tk.Entry(self.ventana_cancion)
        self.entrada_oyentes.grid(row=6, column=0, sticky="ew", padx=10, pady=10)

        # Boton para tratar de insertar
        boton_insertar_cancion = tk.Button(self.ventana_cancion, text='INSERTAR CANCION',bg=WHITE, fg=NAVY_BLUE,height=10)
        boton_insertar_cancion.grid(row=7, column=0, sticky="ew", padx=10, pady=10)
        boton_insertar_cancion.config(command=lambda:self.insertar_cancion_bd(album))
        
        #Ajustar los pesos de expansion de la columna
        for i in range(8):
            self.ventana_albums.grid_rowconfigure(i, weight=1)
        self.ventana_albums.grid_rowconfigure(0, weight=1)

    def insertar_cancion_bd(self, album):
        # Validar que el numero de oyentes sea entero
        if not self.entrada_oyentes.get().isdigit():
           messagebox.showerror('ERROR', 'El numero de oyentes no viene en formato entero') 
           return
        # Intentar realizar la consulta
        try:
            self.cursor.execute("""INSERT INTO canciones (nombre_cancion, lyrics, 
                                numero_reproducciones, album_id) VALUES (%s, %s
                                , %s, (SELECT album_id FROM albums WHERE albums.nombre_album = %s));""", 
                                (self.entrada_nombre.get(), self.entrada_lyrics.get(),self.entrada_oyentes.get(), album))
            messagebox.showinfo('SUCESS', 'La cancion ha sido agregada a la base de datos exitosamente')
            self.conexion_bd.commit()
            self.volver_a_ventana_albums()
        except Exception as e:
            print(e)
            messagebox.showerror('ERROR', 'No fue posible introducir la cancion en la base de datos')
        

                                                  
    def conexion_bd(self):

        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='info_musica'
            )

            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos MySQL")
                self.cursor = self.connection.cursor()
            else:
                exit('No hay conexión con la base de datos')

        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            exit(1)  # Salir del programa con un código de error

    def volver_a_principal(self):
        self.ventana_albums.destroy()
        self.ventana_principal.deiconify()

    def volver_a_ventana_albums(self):
        self.ventana_cancion.destroy()
        self.ventana_albums.deiconify()


class Insertar_Album():
    def __init__(self, conexion_bd):
        self.artista_a_buscar = ''
        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title ('PEDIR ARTISTA')
        self.ventana_principal.geometry('250x150')
        self.ventana_principal.resizable(False,False)
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.indicacion = tk.Label(self.ventana_principal,text='INTRODUCE EL NOMBRE DE UN ARTISTA', bg=WHITE, fg=NAVY_BLUE)
        self.indicacion.grid(row=0, column=0, pady=5, padx=5, sticky='ew')
        self.entrada_artista = tk.Entry(self.ventana_principal, fg=NAVY_BLUE)
        self.entrada_artista.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        # Boton buscar
        self.boton_buscar = tk.Button(self.ventana_principal, text="BUSCAR ARTISTA", fg=NAVY_BLUE, bg=WHITE, height=2)
        self.boton_buscar.grid(row=2, column=0, padx=10, pady=10, sticky='ew')  
        self.boton_buscar.config(command=self.buscar_artista)
        # Una vez se encuentre un artista valido
        self.ventana_principal.mainloop()

    def buscar_artista(self):
        artista_existe = False
        self.artista_a_buscar = self.entrada_artista.get()
        self.artista_id = -1
        self.cursor.execute("SELECT COUNT(nombre), artistas.artista_id FROM artistas WHERE artistas.nombre = %s;", (self.artista_a_buscar,))
        self.artista_encontrado = self.cursor.fetchall()

        if self.artista_encontrado[0][0] == 0:
            messagebox.showwarning('ERROR', F'NO HAY ARTISTA CON EL NOMBRE {self.artista_a_buscar} EN LA BASE DE DATOS')
        else:
            artista_existe = True
            self.artista_id = int(self.artista_encontrado[0][1])
            messagebox.showinfo('ARTISTA ENCONTRADO', F"El artista {self.artista_a_buscar} ha sido encontrado en la base de datos, Cierra la ventana para continuar")
        
        # Si no hay errores y el artista esta bien
        if artista_existe:
            self.introducir_album()

    def introducir_album(self):
        self.ventana_principal.withdraw()
        self.ventana_introducir = tk.Tk()
        self.ventana_introducir.title('INSERTAR NUEVO ALBUM')
        self.ventana_introducir.geometry('600x300')
        self.ventana_introducir.config(bg=NAVY_BLUE)
        # Protocolo para el cierre de ventana
        self.ventana_introducir.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())

        # Label para las indicaciones
        self.indicaciones_introducir = tk.Label(self.ventana_introducir,
                                                text=F'INTRODUCE LOS SIGUIENTES CAMPOS PARA INSERTAR EL NUEVO ALBUM',
                                                  bg=WHITE, fg=NAVY_BLUE)
        self.indicaciones_introducir.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        self.label_artista = tk.Label(self.ventana_introducir,
                                                text=f'Artista: {self.artista_a_buscar.title()}',
                                                bg=WHITE, fg=NAVY_BLUE).grid(row=1, column=0, pady=5, padx=5, sticky='ew')
        
    
        # Instrucciones y entrada para el nombre del album
        self.indicacion_nombre = tk.Label(self.ventana_introducir,
                                          text=F'Introduce el nombre del nuevo album',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_nombre.grid(row=2, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_nombre = tk.Entry(self.ventana_introducir)
        self.entrada_nombre.grid(row=3, column=0, pady=15, padx=15, sticky='ew')
        
        # Instrucciones y entrada para el numero de canciones
        self.indicacion_num_canciones = tk.Label(self.ventana_introducir,
                                          text=F'Introduce el numero de canciones en formato de numero ENTERO',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_num_canciones.grid(row=4, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_num_canciones = tk.Entry(self.ventana_introducir)
        self.entrada_num_canciones.grid(row=5, column=0, pady=15, 
                                                                     padx=15, sticky='ew')
        # Boton de insertar
        self.boton_insertar = tk.Button(self.ventana_introducir, text="INSERTAR ALBUM", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.insertar_en_bd)
        self.boton_insertar.grid(row=6, column=0, pady=15, padx=15, sticky='ew')
        
        
        for i in range(6):
            self.ventana_introducir.grid_rowconfigure(i, weight=1)

        self.ventana_introducir.grid_columnconfigure(0, weight=1)
        
  
    def volver_a_principal(self):
        self.ventana_introducir.destroy()
        self.ventana_principal.deiconify()

    def insertar_en_bd(self):
        #print(self.entrada_nombre.get())
        nombre_album = self.entrada_nombre.get()
        numero_canciones = self.entrada_num_canciones.get()

        if not numero_canciones.isdigit():
            messagebox.showerror('ERROR', 'El numero de canciones no viene en formato numero entero') 
            return
        # Intentar realizar la consulta
        try:
            # Consulta con insert en la tabla album
            self.cursor.execute("""INSERT INTO albums (nombre_album, numero_canciones, artista_id) 
                                VALUES (%s, %s, %s);""", 
                                (nombre_album, numero_canciones,self.artista_id))
            messagebox.showinfo('SUCESS', 'El album ha sido agregada a la base de datos exitosamente')
            self.conexion_bd.commit()
        except Exception as e:
            # Si la consulta no se realiza se reporta al usuario
            print(e)
            messagebox.showerror('ERROR', f"""No fue posible introducir la cancion en la base de datos
                                 {e}""")
            
class Insertar_Artista():
    def __init__(self, conexion_bd):
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Ventana para introducir un nuevo artista
        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('INSERTAR UN NUEVO ARTISTA')
        self.ventana_principal.geometry('400x500')
        self.ventana_principal.config(bg=NAVY_BLUE)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introducir un nuevo artista', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Instrucciones y entrada para introducir un el nombre del nuevo artista
        self.indicacion_nombre = tk.Label(self.ventana_principal,
                                          text=F'Introduce el nombre del nuevo artista',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_nombre.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_nombre = tk.Entry(self.ventana_principal)
        self.entrada_nombre.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Instrucciones y entrada para introducir el numero de oyentes
        
        self.indicacion_num_oyentes = tk.Label(self.ventana_principal,
                                          text=F'Introduce el numero de oyentes en numero ENTERO',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_num_oyentes.grid(row=3, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_num_oyentes = tk.Entry(self.ventana_principal)
        self.entrada_num_oyentes.grid(row=4, column=0, pady=15, padx=15, sticky='ew')

        # Instrucciones y entrada para introducir el genero musica
        self.indicacion_genero= tk.Label(self.ventana_principal,
                                          text=F'Introduce el nombre del genero musical',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_genero.grid(row=5, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_genero = tk.Entry(self.ventana_principal)
        self.entrada_genero.grid(row=6, column=0, pady=15, padx=15, sticky='ew')

        # Boton de insertar
        self.boton_insertar = tk.Button(self.ventana_principal, text="INSERTAR Artista", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.insertar_en_bd)
        self.boton_insertar.grid(row=7, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(8):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def insertar_en_bd(self):
        nombre_artista = self.entrada_nombre.get()
        numero_oyentes = self.entrada_num_oyentes.get()
        genero = self.entrada_genero.get()

        # Chechar que el genero exista
        try:
            self.cursor.execute("""SELECT COUNT(*), generos.genero_id FROM generos
                                WHERE generos.nombre_genero = %s;""", (genero,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                raise Exception
            else:
                genero_id = resultados[0][1]
        except Exception as e:
            messagebox.showerror('ERROR', f"""El genero {genero} no existe en la base de datos; {e}""")
            return
        
        # Checar que el numero de digitos exista
        if not numero_oyentes.isdigit():
            messagebox.showerror('ERROR', 'El numero de oyentes no viene en formato de numero entero') 
            return
        
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""INSERT INTO artistas (nombre, oyentes_mensuales, genero_id) 
                                VALUES (%s, %s, %s);""" , (nombre_artista, numero_oyentes, genero_id))
            messagebox.showinfo('SUCESS', 'El artista ha sido agregado a la base de datos exitosamente')
            self.conexion_bd.commit()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible introducir la cancion en la base de datos
                                 {e}""")
            
class Insertar_Genero():
    def __init__(self, conexion_bd) :
        # Ventana para insertar genero
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('INSERTAR UN NUEVO ARTISTA')
        self.ventana_principal.geometry('250x250')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)
        
        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introducir un nuevo genero musical', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Instrucciones y entrada para introducir un el nombre del nuevo genero musical
        self.indicacion_nombre = tk.Label(self.ventana_principal,
                                          text=F'Introduce el nombre del nuevo genero',
                                          bg=WHITE, fg=NAVY_BLUE
                                          )
        self.indicacion_nombre.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        self.entrada_nombre = tk.Entry(self.ventana_principal)
        self.entrada_nombre.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Boton de insertar
        self.boton_insertar = tk.Button(self.ventana_principal, text="INSERTAR Genero", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.insertar_en_bd)
        self.boton_insertar.grid(row=3, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(4):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def insertar_en_bd(self):
        nombre_genero = self.entrada_nombre.get()
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""INSERT INTO generos (nombre_genero) 
                                VALUES (%s);""", (nombre_genero,))
            
            messagebox.showinfo('SUCESS', 'El genero ha sido agregado a la base de datos exitosamente')
            self.conexion_bd.commit()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible introducir la cancion en la base de datos
                                 {e}""")
        
# Clases de eliminar
class Eliminar_cancion():
    def __init__(self, conexion_bd):
        # Ventana para eliminar una cancion
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('ELIMINAR UNA CANCION')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre de la cancion a eliminar', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre de la cancion a eliminar
        self.entrada_nombre = tk.Entry(self.ventana_principal)
        self.entrada_nombre.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de eliminar
        self.boton_insertar = tk.Button(self.ventana_principal, text="Eliminar Cancion", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.eliminar_en_bd)
        self.boton_insertar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def eliminar_en_bd(self):
        cancion_a_eliminar = self.entrada_nombre.get()
        # Checar que la cancion exista en la base de datos
        try:
            self.cursor.execute('SELECT COUNT(*) FROM canciones WHERE canciones.nombre_cancion = %s;', (cancion_a_eliminar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe la cancion {cancion_a_eliminar} en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la consulta 

        try:
            # Ejecutar la querie
            self.cursor.execute("""DELETE FROM canciones WHERE canciones.nombre_cancion = %s;""", 
                                (cancion_a_eliminar,))
            
            messagebox.showinfo('SUCESS', f'La cancion {cancion_a_eliminar} ha sido eliminada de la base de datos')
            self.conexion_bd.commit()
        # Si hay un error en la querie, informar al usuario
        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible eliminar la cancion de la base de datos
                                 {e}""")

class Eliminar_Album():
    def __init__(self, conexion_bd):
        # Ventana para eliminar un album
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('ELIMINAR UN ALBUM')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre del album a eliminar', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre de la cancion a eliminar
        self.entrada_album = tk.Entry(self.ventana_principal)
        self.entrada_album.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de eliminar
        self.boton_insertar = tk.Button(self.ventana_principal, text="Eliminar Album", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.eliminar_en_bd)
        self.boton_insertar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def eliminar_en_bd(self):
        album_a_eliminar = self.entrada_album.get()
        # Checar si el album existe
        try:
            self.cursor.execute('SELECT COUNT(*) FROM albums WHERE albums.nombre_album = %s;', (album_a_eliminar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe el album {album_a_eliminar} en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""DELETE FROM albums WHERE albums.nombre_album = %s;""", 
                                (album_a_eliminar,))
            
            messagebox.showinfo('SUCESS', f'El album {album_a_eliminar} ha sido eliminado de la base de datos')
            self.conexion_bd.commit()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible eliminar la cancion de la base de datos
                                 {e}""")
            
class Eliminar_Artista():
    def __init__(self, conexion_bd):
        # Ventana para eliminar un artista
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('ELIMINAR UN ARTISTA')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre del ARTISTA a eliminar', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre de la cancion a eliminar
        self.entrada_artista = tk.Entry(self.ventana_principal)
        self.entrada_artista.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de eliminar
        self.boton_eliminar = tk.Button(self.ventana_principal, text="Eliminar Artista", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.eliminar_en_bd)
        self.boton_eliminar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def eliminar_en_bd(self):
        artista_a_eliminar = self.entrada_artista.get()
        # Checar si el album existe
        try:
            self.cursor.execute('SELECT COUNT(*) FROM artistas WHERE artistas.nombre = %s;', (artista_a_eliminar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe el artista: {artista_a_eliminar} en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""DELETE FROM artistas WHERE artistas.nombre = %s;""", 
                                (artista_a_eliminar,))
            
            messagebox.showinfo('SUCESS', f'El artista {artista_a_eliminar} ha sido eliminado de la base de datos')
            self.conexion_bd.commit()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible eliminar al artista de la base de datos
                                 {e}""")
            
class Eliminar_Genero():
    def __init__(self, conexion_bd):
        # Ventana para eliminar un genero
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('ELIMINAR UN GENERO')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre del GENERO a eliminar', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre del genero a eliminar
        self.entrada_genero = tk.Entry(self.ventana_principal)
        self.entrada_genero.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de eliminar
        self.boton_eliminar = tk.Button(self.ventana_principal, text="Eliminar Genero", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.eliminar_en_bd)
        self.boton_eliminar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def eliminar_en_bd(self):
        genero_a_eliminar = self.entrada_genero.get()
        # Checar si el genero existe
        try:
            self.cursor.execute('SELECT COUNT(*) FROM generos WHERE generos.nombre_genero = %s;', (genero_a_eliminar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe el genero: {genero_a_eliminar} en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""DELETE FROM generos WHERE generos.nombre_genero = %s;""", 
                                (genero_a_eliminar,))
            
            messagebox.showinfo('SUCESS', f'El genero musical, {genero_a_eliminar} ha sido eliminado de la base de datos')
            self.conexion_bd.commit()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible eliminar al genero de la base de datos
                                 {e}""")
            
class Mostrar_Cancion():
    def __init__(self, conexion_bd):
        # Ventana para mostrar una cancion
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('MOSTRAR INFORMACION DE UNA CANCION')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.ventana_principal.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre de la CANCION', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre de la cancion para mostrar informacion
        self.entrada_cancion = tk.Entry(self.ventana_principal)
        self.entrada_cancion.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de buscar
        self.boton_buscar = tk.Button(self.ventana_principal, text="Buscar Cancion", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.buscar_en_bd)
        self.boton_buscar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def buscar_en_bd(self):
        cancion_a_buscar = self.entrada_cancion.get()
        # Checar si la cancion existe
        try:
            self.cursor.execute('SELECT COUNT(*) FROM canciones WHERE canciones.nombre_cancion = %s;', (cancion_a_buscar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe la cancion: {cancion_a_buscar}  en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la consulta 
        try:
            self.cursor.execute("""SELECT canciones.nombre_cancion, canciones.lyrics, 
                                albums.nombre_album, artistas.nombre FROM canciones 
                                JOIN albums ON canciones.album_id = albums.album_id 
                                JOIN artistas ON albums.artista_id = artistas.artista_id
                                WHERE canciones.nombre_cancion = %s;""",
                                (cancion_a_buscar,))
            self.info_cancion = self.cursor.fetchall()
            self.conexion_bd.commit()
            self.informacion_cancion()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible recopilar la informacion de la cancion en la base de datos
                                 {e}""")
    def informacion_cancion(self):
        # Guardar en str's la informacion de las canciones
        self.lyrics_cancion = self.info_cancion[0][1]
        if self.lyrics_cancion == None:
            self.lyrics_cancion = 'Letra no disponible'

        self.informacion = {
            'NOMBRE': self.info_cancion[0][0],
            'ARTISTA': self.info_cancion[0][3],
            'ALBUM': self.info_cancion[0][2],
            'LYRYCS': self.lyrics_cancion
        }

        # Imprimir en una nueva ventana la informacion de la cancion
        self.ventana_principal.withdraw() # Cerrar la ventana principal
        self.ventana_informacion = tk.Tk()
        self.ventana_informacion.title('MOSTRAR INFORMACION DE UNA CANCION')
        self.ventana_informacion.geometry('500x300')
        self.ventana_informacion.config(bg=NAVY_BLUE)
        
        # Imprimir los datos de la cancion
        self.label_titulo = tk.Label(self.ventana_informacion, text='Informacion de la cancion', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_titulo.grid(row=0, column=0, pady=5, padx=5, sticky='ns')
        
        
        self.labels = []
        # Imprimir la informacion
        i = 1
        for dato in self.informacion:
            nuevo_label = tk.Label(self.ventana_informacion, 
                                   text=f'{dato}: {self.informacion[dato]}', fg=NAVY_BLUE, bg=WHITE)
            nuevo_label.grid(row=i, column=0,pady=5, padx=5, sticky='ns')
            self.labels.append(nuevo_label)
            i += 1
            self.ventana_informacion.grid_rowconfigure(i,weight=1)
        
        self.ventana_informacion.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())
        self.ventana_informacion.grid_columnconfigure(0, weight=1)

    def volver_a_principal(self):
        self.ventana_informacion.destroy()
        self.ventana_principal.deiconify()
class Mostrar_Album():
    def __init__(self, conexion_bd):
        # Ventana para mostrar un album
        # Conexion de la clase con la base de datos

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        # Configuracion basica
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('MOSTRAR INFORMACION DE UN ALBUM')
        self.ventana_principal.geometry('250x200')
        self.ventana_principal.config(bg=NAVY_BLUE)
        

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_principal, text='Introduce el nombre del ALBUM', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre del album para mostrar informacion
        self.entrada_album = tk.Entry(self.ventana_principal)
        self.entrada_album.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de buscar
        self.boton_buscar = tk.Button(self.ventana_principal, text="Buscar Album", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.buscar_en_bd)
        self.boton_buscar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_principal.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_principal.grid_columnconfigure(0, weight=1)
        
        self.ventana_principal.mainloop()

    def buscar_en_bd(self):
        album_a_buscar = self.entrada_album.get()
        # Checar si el album existe
        try:
            self.cursor.execute('SELECT COUNT(*) FROM albums WHERE albums.nombre_album = %s;', (album_a_buscar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe el album: {album_a_buscar}  en la base de datos')
                return
        except Exception as e:
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        # Intentar realizar la primera consulta
        # Buscar la informacion del album
        try:
            self.cursor.execute("""SELECT albums.nombre_album, albums.numero_canciones, 
                                artistas.nombre FROM albums 
                                JOIN artistas ON albums.artista_id = artistas.artista_id 
                                WHERE albums.nombre_album = %s;""",
                                (album_a_buscar,))
            self.info_album = self.cursor.fetchall()

            # Intentar realizar la segunda consulta
            # Buscar las canciones del album
            self.cursor.execute("""SELECT canciones.nombre_cancion FROM canciones 
                                JOIN albums ON albums.album_id = canciones.album_id 
                                WHERE albums.nombre_album = %s;""",(album_a_buscar,))
            self.info_canciones = self.cursor.fetchall()
            #print(self.info_album)
            #print(self.info_canciones)
            self.conexion_bd.commit()
            self.show_album()

        except Exception as e:
            messagebox.showerror('ERROR', f"""No fue posible recopilar la informacion del album en la base de datos
                                 {e}""")
    def show_album(self):
        # Guardar en str's la informacion de las canciones

        self.informacion = {
            'NOMBRE': self.info_album[0][0],
            'NUMERO CANCIONES': self.info_album[0][1],
            'GRUPO': self.info_album[0][2],
        }

        # Imprimir en una nueva ventana la informacion de la cancion
        self.ventana_principal.withdraw() # Cerrar la ventana principal
        self.ventana_informacion = tk.Tk()
        self.ventana_informacion.title('INFORMACION DEL ALBUM')
        self.ventana_informacion.geometry('200x500')
        self.ventana_informacion.config(bg=NAVY_BLUE)
        
        # Imprimir los datos de la cancion
        self.label_titulo = tk.Label(self.ventana_informacion, text='Informacion de la cancion', fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_titulo.grid(row=0, column=0, pady=5, padx=5, sticky='ns')
        
        
        self.labels = []
        # Imprimir la informacion
        i = 1
        for dato in self.informacion:
            nuevo_label = tk.Label(self.ventana_informacion, 
                                   text=f'{dato}: {self.informacion[dato]}', fg=NAVY_BLUE, bg=WHITE)
            nuevo_label.grid(row=i, column=0,pady=5, padx=5, sticky='ns')
            self.labels.append(nuevo_label)
            i += 1
        
        # Imprimir la lista de canciones
        self.labels_canciones = []
        for tupla_cancion in self.info_canciones:
            nuevo_label = tk.Label(self.ventana_informacion, 
                                   text=f'{tupla_cancion[0]}', fg=NAVY_BLUE, bg=WHITE)
            nuevo_label.grid(row=i, column=0,pady=5, padx=5, sticky='ns')
            self.labels_canciones.append(nuevo_label)
            i += 1

        
        for j in range(i):
            # Ajustar el peso de expansion de columna
            self.ventana_informacion.grid_rowconfigure(i,weight=1) 
        
        # Ajustar el peso de expansion de frio
            self.ventana_informacion.grid_columnconfigure(0,weight=1)
            
        self.ventana_informacion.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())
        self.ventana_informacion.grid_columnconfigure(0, weight=1)

    def volver_a_principal(self):
        self.ventana_informacion.destroy()
        self.ventana_principal.deiconify()

class Mostrar_Artista():
    def __init__(self, coneccion):
        # Inicializar variables
        self.conexion_bd = coneccion
        self.cursor = coneccion.cursor()
        self.artista_a_buscar = ''

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title ('VENTANA PARA BUSCAR ARTISTA')
        self.ventana_principal.geometry('250x150')
        self.ventana_principal.resizable(False,False)
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.indicacion = tk.Label(self.ventana_principal,text='INTRODUCE EL NOMBRE DE UN ARTISTA', bg=WHITE, fg=NAVY_BLUE)
        self.indicacion.grid(row=0, column=0, pady=5, padx=5, sticky='ew')
        self.entrada_artista = tk.Entry(self.ventana_principal, fg=NAVY_BLUE)
        self.entrada_artista.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        self.boton_buscar = tk.Button(self.ventana_principal, text="BUSCAR ARTISTA", fg=NAVY_BLUE, bg=WHITE, height=2)
        self.boton_buscar.grid(row=2, column=0, padx=10, pady=10, sticky='ew')  
        self.boton_buscar.config(command=self.buscar_artista)
        # Una vez se encuentre un artista valido
        self.ventana_principal.mainloop()

    def buscar_artista(self):
        artista_existe = False
        self.artista_a_buscar = self.entrada_artista.get()
        self.cursor.execute("SELECT COUNT(nombre) FROM artistas WHERE artistas.nombre = %s;", (self.artista_a_buscar,))
        self.artista_encontrado = self.cursor.fetchall()
        if self.artista_encontrado[0][0] == 0:
            messagebox.showwarning('ERROR', F'NO HAY ARTISTA CON EL NOMBRE {self.artista_a_buscar} EN LA BASE DE DATOS')
        else:
            artista_existe = True
            messagebox.showinfo('ARTISTA ENCONTRADO', F"El artista {self.artista_a_buscar} ha sido encontrado en la base de datos, Cierra la ventana para continuar")
        # Despues de que se cierre el messagebox
        # Seleccionar_album para mas informacion
        if artista_existe:
            self.imprimir_informacion()


    def imprimir_informacion(self):
        # Preparar la ventana donde se escribiran los albums
        self.ventana_principal.withdraw()
        self.ventana_albums =  tk.Tk()

        # Configuracion basica
        self.ventana_albums.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())
        self.ventana_albums.title(f'Albums del artista {self.artista_a_buscar}')
        self.ventana_albums.geometry('300x500')
        self.ventana_albums.config(bg=NAVY_BLUE)

        # Obten la informacion del artista
        self.cursor.execute("""SELECT artistas.nombre, artistas.oyentes_mensuales, 
                            generos.nombre_genero FROM artistas 
                            JOIN generos ON artistas.genero_id = generos.genero_id 
                            WHERE artistas.nombre = %s;""",(self.artista_a_buscar,))
        self.data_artista = self.cursor.fetchall()
        print(self.data_artista)

        #Pedir los albums del artista
        self.cursor.execute("""SELECT albums.nombre_album FROM albums JOIN artistas 
                            ON albums.artista_id = artistas.artista_id 
                            WHERE artistas.nombre = %s;""", (self.artista_a_buscar,))
        self.albums_de_artista = self.cursor.fetchall()
        
        # Imprimir la informacion del artista
        self.labels_info = {'NOMBRE': None, 'OYENTES MENSUALES':None, 'GENERO': None,}

        i = 0
        for row in self.labels_info:
            self.labels_info[row] = tk.Label(self.ventana_albums, 
                                             text=f"{row}: {self.data_artista[0][i]}", 
                                             bg=WHITE, fg=NAVY_BLUE)
            # Ajustar la grid
            self.labels_info[row].grid(row=i, column=0,padx=5, pady=5, sticky='ew')
            i += 1        

        # Imprimir los albums
        self.labels_info['ALBUMS'] = tk.Label(self.ventana_albums, 
                                             text=f"ALBUMS", 
                                             bg=WHITE, fg=NAVY_BLUE)
        self.labels_info['ALBUMS'].grid(row=i, column=0,padx=5, pady=5, sticky='ew')
        i += 1

        for album in self.albums_de_artista:
            self.labels_info[album[0]] = tk.Label(self.ventana_albums, 
                                             text=f"{album[0]}", 
                                             bg=WHITE, fg=NAVY_BLUE)
            # Ajustar la grid
            self.labels_info[album[0]].grid(row=i, column=0,padx=5, pady=5, sticky='ew')
            i += 1

        # Ajustar el peso de fila
        for j in range(i):
            self.ventana_albums.rowconfigure(j, weight=1)
        
        # Ajustar el peso de la columna
        self.ventana_albums.columnconfigure(0, weight=1)
        
    def volver_a_principal(self):
        self.ventana_albums.destroy()
        self.ventana_principal.deiconify()

    def volver_a_albums(self):
        self.ventana_informacion.destroy()
        self.ventana_albums.deiconify()


class Mostrar_Genero():
    def __init__(self, coneccion):
        # Inicializar variables
        self.conexion_bd = coneccion
        self.cursor = coneccion.cursor()
        self.genero_a_buscar = ''

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title ('VENTANA PARA MOSTRAR INFORMACION DE GENERO')
        self.ventana_principal.geometry('250x150')
        self.ventana_principal.resizable(False,False)
        self.ventana_principal.config(bg=NAVY_BLUE)
        self.indicacion = tk.Label(self.ventana_principal,text='INTRODUCE EL NOMBRE DE UN GENERO', bg=WHITE, fg=NAVY_BLUE)
        self.indicacion.grid(row=0, column=0, pady=5, padx=5, sticky='ew')
        self.entrada_genero = tk.Entry(self.ventana_principal, fg=NAVY_BLUE)
        self.entrada_genero.grid(row=1, column=0, pady=10, padx=10, sticky='ew')
        self.boton_buscar = tk.Button(self.ventana_principal, text="BUSCAR GENERO", fg=NAVY_BLUE, bg=WHITE, height=2)
        self.boton_buscar.grid(row=2, column=0, padx=10, pady=10, sticky='ew')  
        self.boton_buscar.config(command=self.buscar_genero)
        # Una vez se encuentre un genero valido
        self.ventana_principal.mainloop()

    def buscar_genero(self):
        genero_existe = False
        self.genero_a_buscar = self.entrada_genero.get()
        self.cursor.execute("""SELECT COUNT(generos.nombre_genero) 
                            FROM generos WHERE generos.nombre_genero = %s;""", (self.genero_a_buscar,))
        self.artista_encontrado = self.cursor.fetchall()
        if self.artista_encontrado[0][0] == 0:
            messagebox.showwarning('ERROR', F'NO HAY genero CON EL NOMBRE {self.genero_a_buscar} EN LA BASE DE DATOS')
        else:
            genero_existe = True
            messagebox.showinfo('GENERO ENCONTRADO', F"El genero {self.genero_a_buscar} ha sido encontrado en la base de datos, Cierra la ventana para continuar")
        # Despues de que se cierre el messagebox
        # Imprimir informacion de genero musical
        if genero_existe:
            self.imprimir_informacion()


    def imprimir_informacion(self):
        # Preparar la ventana donde se escribiran los albums
        self.ventana_principal.withdraw()
        self.ventana_albums =  tk.Tk()

        # Configuracion basica
        self.ventana_albums.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())
        self.ventana_albums.title(f'Artistas del genero {self.genero_a_buscar}')
        self.ventana_albums.geometry('300x500')
        self.ventana_albums.config(bg=NAVY_BLUE)

        # Obten los artistas del genero
        self.cursor.execute("""SELECT artistas.nombre FROM artistas 
                            JOIN generos ON artistas.genero_id = generos.genero_id 
                            WHERE generos.nombre_genero = %s;""",(self.genero_a_buscar,))
        self.data_genero = self.cursor.fetchall()

        i = 0     
        self.labels_info = {}
        # Imprimir los artistas
        self.labels_info['ARTISTAS'] = tk.Label(self.ventana_albums, 
                                             text=f"ARTISTAS DEL GENERO: {self.genero_a_buscar.strip()}", 
                                             bg=WHITE, fg=NAVY_BLUE)
        self.labels_info['ARTISTAS'].grid(row=i, column=0,padx=5, pady=5, sticky='ew')
        i += 1

        for artista in self.data_genero:
            self.labels_info[artista[0]] = tk.Label(self.ventana_albums, 
                                             text=f"{artista[0]}", 
                                             bg=WHITE, fg=NAVY_BLUE)
            # Ajustar la grid
            self.labels_info[artista[0]].grid(row=i, column=0,padx=5, pady=5, sticky='ew')
            i += 1

        # Ajustar el peso de fila
        for j in range(i):
            self.ventana_albums.rowconfigure(j, weight=1)
        
        # Ajustar el peso de la columna
        self.ventana_albums.columnconfigure(0, weight=1)
        
    def volver_a_principal(self):
        self.ventana_albums.destroy()
        self.ventana_principal.deiconify()

    def volver_a_albums(self):
        self.ventana_informacion.destroy()
        self.ventana_albums.deiconify()

class Elemento():
        def __init__(self, nombre_elemento, tipo_dato):
            self.nombre_elemento = nombre_elemento
            self.tipo_dato = tipo_dato


class Actualizar():
    def __init__(self, conexion_bd, entidad):
        # Ventana para mostrar un album
        # Conexion de la clase con la base de datos
        self.entidad = entidad
        self.tipo_dato = ""
        self.tabla = ""

        # Establecer las constantes de los elementos
        self.elementos = []
    
        

        self.conexion_bd = conexion_bd
        self.cursor = self.conexion_bd.cursor()

        match self.entidad:
            case 'CANCION':
                self.actualizar_cancion()
            case 'ARTISTA':
                self.actualizar_artista()
            case 'ALBUM':
                self.actualizar_album()
            case 'GENERO':
                self.actualizar_genero()
            case _: # Default
                raise KeyError('NO FUE PROPORCIONADA UNA ENTIDAD EN EL FORMATO CORRECTO')
            
    def actualizar_album(self):      
        self.tabla = "albums"
        self.elemento_query_buscar = 'nombre_album'
        self.elementos = [None, None]
        self.elementos[0] = Elemento('nombre_album', 'TEXTO')
        self.elementos[1] =  Elemento('numero_canciones', 'NUMERO ENTERO')
        self.buscar_entidad_gui()
            
    def actualizar_genero(self):
        self.tabla = "generos"
        self.elemento_query_buscar = 'nombre_genero'
        self.elementos = [None]
        self.elementos[0] = Elemento('nombre_genero', 'TEXTO')
        self.buscar_entidad_gui()       
            
        
    def actualizar_cancion(self):
        self.tabla = "canciones"
        self.elemento_query_buscar = 'nombre_cancion'
        self.elementos = [None, None, None]
        self.elementos[0] = Elemento('nombre_cancion', 'NUMERO ENTERO')
        self.elementos[1] =  Elemento('lyrics', 'TEXTO')
        self.elementos[2] =  Elemento('numero_reproducciones', 'NUMERO ENTERO')
        self.buscar_entidad_gui()
            
    def actualizar_artista(self):
        # Buscar que cancion se quiere actualizar
        self.elemento_query_buscar = 'nombre'
        self.tabla = "artistas"
        self.elementos = [None, None]
        self.elementos[0] = Elemento('nombre', 'TEXTO')
        self.elementos[1] =  Elemento('oyentes_mensuales', 'NUMERO ENTERO')

        self.buscar_entidad_gui()
        

    def buscar_entidad_gui(self):
        # Configuracion basica de la ventana para buscar
        self.ventana_buscar = tk.Tk()
        self.ventana_buscar.title(f'BUSCAR  {self.entidad} a ACTUALIZAR')
        self.ventana_buscar.geometry('300x200')
        self.ventana_buscar.config(bg=NAVY_BLUE)
        self.ventana_buscar.resizable(False, False)

        # Label para las intrucciones
        self.label_instruccions = tk.Label(self.ventana_buscar, 
                                           text=f'Introduce el nombre de {self.entidad} a ACTUALIZAR', 
                                           fg=NAVY_BLUE,
                                           bg=WHITE)
        self.label_instruccions.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        # Entrada para introducir el nombre de la cancion para mostrar informacion
        self.entrada_entidad_buscar = tk.Entry(self.ventana_buscar)
        self.entrada_entidad_buscar.grid(row=1, column=0, pady=15, padx=15, sticky='ew')
        
        # Boton de buscar
        self.boton_buscar = tk.Button(self.ventana_buscar, text=f"Buscar {self.entidad}", 
                                        fg=NAVY_BLUE, bg=WHITE, height=2, command=self.buscar_entidad_bd)
        self.boton_buscar.grid(row=2, column=0, pady=15, padx=15, sticky='ew')

        # Ajustar expansion de fila
        for i in range(3):
            self.ventana_buscar.grid_rowconfigure(i, weight=1)

        # Ajustar expansion de columna
        self.ventana_buscar.grid_columnconfigure(0, weight=1)
        
        self.ventana_buscar.mainloop()

    def buscar_entidad_bd(self):
        self.entidad_a_buscar = self.entrada_entidad_buscar.get()

        # Construir la query para la funcion buscar
        self.query_buscar = f"SELECT COUNT(*) FROM {self.tabla} WHERE {self.tabla}.{self.elemento_query_buscar} = %s;"
        # Checar si la entidad existe
        try:
            self.cursor.execute(self.query_buscar, (self.entidad_a_buscar,))
            resultados = self.cursor.fetchall()
            if resultados[0][0] == 0:
                messagebox.showerror('ERROR',f'No existe la {self.entidad}: {self.entidad_a_buscar}  en la base de datos')
                return
            else:
                messagebox.showinfo('FOUND', f'La {self.entidad}: {self.entidad_a_buscar} existe en la base de datos, cierra ventana para continuar')
        except Exception as e:
            print(e)
            messagebox.showerror('ERROR','Error en la base de datos, no se ejecuto la querie correctamente')
            return
        
        # Si no hay errores entonces se continua
        self.seleccionar_elemento()



    def seleccionar_elemento(self):
        self.ventana_buscar.withdraw()
         # Imprime una ventana 
        self.elemento_escogido = ''
        self.botontes_elementos = []
        # Configuracion basica de la ventana
        self.ventana_elemento = tk.Tk()
        self.ventana_elemento.title('VENTANA ELEMENTO')
        self.ventana_elemento.geometry('250x400')
        self.ventana_elemento.config(bg=NAVY_BLUE)
        self.ventana_elemento.protocol("WM_DELETE_WINDOW",lambda: self.volver_a_principal())

        self.label_instruccion = tk.Label(self.ventana_elemento, text='SELECCIONA UN ELEMENTO A ACTUALIZAR' ,
                                           fg=NAVY_BLUE, bg=WHITE)
        self.label_instruccion.grid(row=0, column=0, pady=5, padx=5, sticky='ew')
        self.ventana_elemento.grid_rowconfigure(0, weight=1)
        
        i = 1
        for elemento in self.elementos:
            nuevo_boton = tk.Button(self.ventana_elemento, text=elemento.nombre_elemento,
                                    bg=WHITE, fg=NAVY_BLUE,
                                    command=lambda elemento_s=elemento:self.actualizar_elemento(elemento_s))
            nuevo_boton.grid(row=i, column=0, pady=10, padx=5, sticky='nsew')
            # Ajustar el peso de la columna
            self.ventana_elemento.grid_rowconfigure(i, weight=1)
            i += 1
            self.botontes_elementos.append(nuevo_boton)

        self.ventana_elemento.grid_columnconfigure(0, weight=1)
        self.ventana_elemento.mainloop()

    def actualizar_elemento(self, elemento_escogido):
        # Cerrar la ventana anterior y establecer el elemento a actualizar elegido por el usuario
        self.ventana_elemento.withdraw()
        self.elemento_escogido = elemento_escogido

        # Configuracion basica
        self.ventana_actualizar = tk.Tk()
        self.ventana_actualizar.title(F'CAMBIAR ELEMENTO')
        self.ventana_actualizar.geometry('300x150')
        self.ventana_actualizar.config(bg=NAVY_BLUE)
        self.ventana_actualizar.resizable(False, False)
        self.ventana_actualizar.protocol("WM_DELETE_WINDOW",lambda: self.volver_ventana_elemento())

        # Imprimir instrucciones
        self.label_instruccion1 = tk.Label(self.ventana_actualizar, 
                                          text=f" ELEMENTO A ACTUALIZAR {self.elemento_escogido.nombre_elemento}")
        self.label_instruccion1.pack(padx=5,pady=10)
        self.label_instruccion2 = tk.Label(self.ventana_actualizar,
                                           text=F'El nuevo valor debe ser de tipo: {self.elemento_escogido.tipo_dato}'
                                           )
        self.label_instruccion2.pack(padx=5,pady=10)

        #Poner la barra de entrada del nuevo elemento
        self.entrada_nuevo_elemento = tk.Entry(self.ventana_actualizar)
        self.entrada_nuevo_elemento.pack()

        # Poner boton para actualizar
        self.boton_actualizar = tk.Button(self.ventana_actualizar, text='ACTUALIZAR',
                                          fg=NAVY_BLUE, bg=WHITE, height=1,
                                          command=self.actualizar_bd)
        self.boton_actualizar.pack(padx=10, pady=10)

    def actualizar_bd(self):
        self.nuevo_elemento = self.entrada_nuevo_elemento.get()
        self.query_actualizar = f"UPDATE {self.tabla} SET {self.tabla}.{self.elemento_escogido.nombre_elemento} = %s WHERE {self.tabla}.{self.elemento_query_buscar} = '{self.entidad_a_buscar}';"
        print(self.query_actualizar)

        # Asegurarse de que el tipo de dato sea el correcto
        match self.elemento_escogido.tipo_dato:
            case 'NUMERO ENTERO':
                if not self.nuevo_elemento.isdigit():
                    messagebox.showerror('ERROR', f"Valor introducido: {self.nuevo_elemento} es incorrecto. {self.elemento_escogido.nombre_elemento} tiene que ser de: {self.elemento_escogido.tipo_dato} corrigelo! ")
                    return
        # Intentar la actualizacion en la base de datos
        try:
            self.cursor.execute(self.query_actualizar,(self.nuevo_elemento,))
            self.conexion_bd.commit()
            messagebox.showinfo(f"SUCCESS", F"ACTUALIZACION COMPLETADA Y EXITOSA")
        except Exception as e:
            messagebox.showerror(f'ERROR', f"No fue posible hacer la actualizacion en la base de datos. Error tipo {e}")
            return
    def volver_a_principal(self):
        self.ventana_elemento.destroy()
        self.ventana_buscar.deiconify()
        
    def volver_ventana_elemento(self):
        self.ventana_actualizar.destroy()
        self.ventana_elemento.deiconify()

        
def main():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='info_musica'
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            cursor = connection.cursor()
        else:
            exit('No hay conexión con la base de datos')

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit(1)  # Salir del programa con un código de error

    principal = Sistema(connection)
    connection.commit()
    connection.close()

if __name__=="__main__":
    main()
