class Usuario:
    """
    Creación de la super clase: class Usuario.
    Clase padre/madre va a contener los siguientes atributos y mėtodos que esos serån:
    Atributos:
    ----------
        nombre: str
        apellido: str
        gmail: str
        usuario: str
        contrasena: str
        fechaNacimiento: str
        sexo: str
        usuarios: lista[]
    Mėtodos:
    ----------
    def __init__(self,nombre,apellido,gmail,usuario,contrasena,fechaNacimiento,sexo):
        Mėtodo constructor que contiene los atributos de la clase.
    def listado(self,usuarios):
        Mėtodo constructor que guardará los datos de los usuarios registrados.
    def mostrarLista(self):
        Mėtodo constructor que devolverá o mostrará la lista de usuarios.
    """
    def __init__(self,nombre,apellido,gmail,usuario,contrasena,fechaNacimiento,sexo):
        """
        Paramétros: 
        -----------
        nombre: str
            nombre del usuario
        apellido: str
            apellido del usuario
        gmail: str
            correo del usuario
        usuario: str
            nombre o ID del usuario
        contrasena: str
            contraseña del usuario
        fechaNacimiento: str
            fecha de nacimiento del usuario
        sexo: str
            sexualidad del usuario
        usuarios: lista[]
            Lista donde guarda los datos   
        """
        self.nombre=nombre
        self.apellido=apellido
        self.gmail=gmail
        self.usuario=usuario
        self.contrasena=contrasena
        self.fechaNacimiento=fechaNacimiento
        self.sexo=sexo
        self.usuarios=[]
    def listado(self,usuarios):
        """
        Método constructor: que ingresa los datos en la lista.
        Parámetros:
        ------------
        usuarios: str

        Retorna:
        -------
        return usuarios in self.usuarios
            Busca si el usuario se encuentra en la lista
        """
        return usuarios in self.usuarios
    def mostrarListado(self):
        """
        Método de constructor: Muestra los datos que se encuentran en la lista.

        Retorna:
        --------
        return(self.usuarios)
            Retorna lo que contiene la lista.
        """
        return(self.usuarios)

class Actividad(Usuario):
    """
    Creación de la clase hija(Actividad).
        Clase Actividad hereda los atributos de la clase Usuario.

    Atributos(Atributos que hereda de la superClase que es Usuario):
    ----------
        nombre(heredado): str
        apellido(heredado): str
        gmail(heredado): str
        usuario(heredado): str
        contrasena(heredado): str
        fechaNacimiento(heredado): str
        sexo(heredado): str
        usuarios(heredado): lista[]
        mostrador(propio): int
    
    Métodos:
    --------
    def __init__(self,mostrador, nombre, apellido, gmail, usuario, contrasena, fechaNacimiento,sexo):
        Método constructor de la clase Actividad.
    def iniciarSesion(self,idUsuario,login):
        Método constructor que verifica si la condició es True o False.
    """
    def __init__(self,mostrador, nombre, apellido, gmail, usuario, contrasena, fechaNacimiento,sexo):
        """

        Método de contructor de la clase Actividad.

        Paramétros:
        -----------
        mostrador: int
            Número de mostrador que es el usuario.
        """
        """
        Asignación de un número de mostrador al objeto
        """
        self.mostrador=mostrador
        """
        Constructor de la super clase o clase Usuario.
        """
        super().__init__(nombre, apellido, gmail, usuario, contrasena, fechaNacimiento,sexo)
    def iniciarSesion(self,idUsuario,login):
        """
        Metodo constructor que calculo el valor del sueldo del empleado
        Paramétros:
        -----------
            idUsuario: str
                Nombre creado para el usuario.
            login: str
                Clave creada del usuario.
        
        Retorna:
        --------
            return ((self.usuario==idUsuario)&(self.contrasena==login))
                retorna si la operación lógica si ambos datos son iguales, será verdadero(True) o Falso(False).
        """
        return ((self.usuario==idUsuario)&(self.contrasena==login))

condicion=True
opc=int
if __name__=="__main__":
    """
    En nuestro main, lo que tenemos es una serie de estructuras de control los cuales, nos ayudara en el manejo de selección
    de nuestras opciones que queramos hacer.
    while opc!=3:
        opc=int(input("\n=============================== \n BIBLIOTECA VIRTUAL° \n=============================== \n 1: REGISTRARSE \n 2: INICIO SESION \n 3: SALIR \n=============================== \n INGRESE UNA OPCION:  "))
        if opc==1:
          
            nombre=Jordan
            apellido=Guevara
            gmail=jaguevara11@espe.edu.ec
            fechaNacimiento=26/03/2003
            sexo=Hombre
            nombreUsuario=Jo+Gue
            contrasena=26/03/Ho
            mostrador=1
            
            Ingresa los datos a la lista.
            persona.usuarios.append(mostrador)
            persona.usuarios.append(nombre)
            persona.usuarios.append(apellido)
            persona.usuarios.append(gmail)
            persona.usuarios.append(nombreUsuario)
            persona.usuarios.append(contrasena)
            persona.usuarios.append(fechaNacimiento,)
            persona.usuarios.append(sexo)
           
            Instancia a un objeto.
            persona=Actividad(mostrador,nombre,apellido,gmail,nombreUsuario,contrasena,fechaNacimiento,sexo)
            #Muestra los datos que se ingreso.
            print("--------------------------------------------------")
            print("            USUARIO N^ ",persona.mostrador)
            print("     ")
            #Atributo heredado de la superclase.
            print("Nombre y apellido:", persona.nombre, persona.apellido)
            print("Gmail:", persona.gmail, "Fecha de nacimiento:", persona.fechaNacimiento)
            print("Sexo:", persona.sexo)
            print("=======DATOS GENERADOS=======")
            print("Nombre de usuario:", persona.usuario)
            print("Contraseña:", persona.contrasena)
            print("=============================")
            print("---------------------------------------------------")
        
        elif opc==2:
            #Concicion repetitva hasta que sea su operación lógico sea lo contrario.
            while condicion==True:
                #Ingreso de los datos.
                idUsuario=str(input("Ingrese usuario: "))
                login=str(input("Ingrese contrasena: "))
                #condicional de verdadero o falso para iniciar sesión
                if persona.iniciarSesion(idUsuario,login):
                    print("*********************************************")
                    print("Inicio de sesión confirmado, bienvenido", persona.nombre)
                    print("*********************************************")
                    condicion=False
                else:
                    print("Error, por favor vuelva a intentarlo")
        elif opc==3:
            print("Gracias por ingresar.")
        else:
            print("Ingrese bien la opcion correcta.")
    """
    while opc!=3:
        opc=int(input("\n=============================== \n BIBLIOTECA VIRTUAL° \n=============================== \n 1: REGISTRARSE \n 2: INICIO SESION \n 3: SALIR \n=============================== \n INGRESE UNA OPCION:  "))
        if opc==1:
            """
            Ingreso de datos para el objeto persona.
            """
            nombre=str(input("Ingrese su nombre: "))
            apellido=str(input("Ingrese su apellido: "))
            gmail=str(input("Ingrese su gamil: "))
            fechaNacimiento=str(input("Ingrese su fecha de nacimiento: "))
            sexo=str(input("Ingrese su sexo: "))
            nombreUsuario=nombre[0:2]+apellido[0:3]
            contrasena=fechaNacimiento[0:6]+sexo[0:2]
            mostrador=1
            """
            Añade los datos a la lista.
            """
            persona.usuarios.append(mostrador)
            persona.usuarios.append(nombre)
            persona.usuarios.append(apellido)
            persona.usuarios.append(gmail)
            persona.usuarios.append(nombreUsuario)
            persona.usuarios.append(contrasena)
            persona.usuarios.append(fechaNacimiento,)
            persona.usuarios.append(sexo)
            """
            Instanciamiento con la clase hija Actividad.
            """
            persona=Actividad(mostrador,nombre,apellido,gmail,nombreUsuario,contrasena,fechaNacimiento,sexo)
            #Muestra los datos que se ingreso.
            print("---------------------------------------------------")
            print("                   USUARIO N^ ",persona.mostrador)
            print("     ")
            #Atributo heredado de la superclase.
            print("Nombre y apellido:", persona.nombre, persona.apellido)
            print("Gmail:", persona.gmail, "Fecha de nacimiento:", persona.fechaNacimiento)
            print("Sexo:", persona.sexo)
            print("-----------------DATOS GENERADOS-------------------")
            print("Nombre de usuario:", persona.usuario)
            print("Contraseña:", persona.contrasena)
            print("---------------------------------------------------")
        
        elif opc==2:
            #Concicion repetitva hasta que sea su operación lógico sea lo contrario.
            while condicion==True:
                #Ingreso de los datos.
                idUsuario=str(input("Ingrese usuario: "))
                login=str(input("Ingrese contrasena: "))
                #condicional de verdadero o falso para iniciar sesión
                if persona.iniciarSesion(idUsuario,login):
                    print("*********************************************")
                    print("Inicio de sesión confirmado, bienvenido", persona.nombre)
                    print("*********************************************")
                    condicion=False
                else:
                    print("Error, por favor vuelva a intentarlo")
        elif opc==3:
            print("Gracias por ingresar.")
        else:
            print("Ingrese bien la opcion correcta.")