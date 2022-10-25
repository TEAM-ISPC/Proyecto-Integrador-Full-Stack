"""
En esta módulo definiriamos la clase Usuario, la cual sería padre de Cliente y Emprendedor.
Su función seria ser el modelo para implementar en la base de datos en la tabla Usuarios. 
Contará con los siguiente atributos:
    - IdUsuario.
    - Apellido.
    - Nombre.
    - Email.
    - Telefono.
    - IdCliente.
    - IdEmprendedor.

Definiríamos constructor, métodos getters(@property), setters(@xxx.setter) y toSting (__str__).

"""
class Usuario():

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Telefono, IdCliente, IdEmprendedor):
        self.IdUsuario = IdUsuario
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Email = Email
        self.Telefono = Telefono
        self.IdCliente = IdCliente
        self.IdEmprendedor = IdEmprendedor

    def __str__(self):
       return str(self.IdUsuario) + ' ' + self.Apellido + ' ' + self.Nombre + ' ' + self.Email + ' ' + self.Telefono + ' ' + str(self.IdCliente) + ' ' + str(self.IdEmprendedor)

    def guardarUsuario(usuario):
        try:
            conectar()
            mySql_insert_query = "INSERT INTO Usuarios (IdUsuario, Apellido, Nombre, Email, Telefono, IdCliente, IdEmprendedor) VALUES (0, " + usuario.Apellido + ", " + usuario.Nombre + ", " + usuario.Email + ", " + usuario.Telefono + ", 0, 0)"

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Se grabó usuario.")
            cursor.close()

        except mysql.connector.Error as error:
            print("Error al grabar usuario {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("Conexion cerrada")

    def obtenerUsuarioPorId(Id):
        try:
            conectar()
            mySql_query = "select * from productos where idUsuario =" + id
            cursor = connection.cursor()
            cursor.execute(mySql_query)       
            rows=cursor.fetchall()
            for row in rows:
                print(row)     
            cursor.close()

        except mysql.connector.Error as error:
            print("Error al obtener usuario {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("Conexion cerrada")

    def conectar():
        connection = mysql.connector.connect(host='localhost',
                                            database='Turnow',
                                            user='root',
                                            password='')