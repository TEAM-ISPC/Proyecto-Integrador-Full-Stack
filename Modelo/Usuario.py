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

#listaUsuarios = [{"id":0,"apellido":"luna", "nombre":"emanuel", "email":"memonluna@gmail.com", "telefono":"12344213", "emprendedorId":0,"clienteId":0}]
listaUsuarios= []
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

    def guardarUsuario(self, usuario):
        listaUsuarios.append(usuario)

    def obtenerUsuarios(self):
        for x in range(len(listaUsuarios)):
            print(listaUsuarios[x])
        return listaUsuarios

    def obtenerUsuarioPorId(self, id):

        return filter(lambda x: x[0] == id, listaUsuarios)

    def borrarUsuarioPorId(id):
        try:
            conectar()
            mySql = " DELETE FROM Usuarios  WHERE Id =" + id
            cursor = connection.cursor()
            cursor.execute(mySql)
            connection.commit()
            print(cursor.rowcount, "registro(s) borrado") 

        except mysql.connector.Error as error:
            print("Error al borrar registro {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexion cerrada")
    
    def actualizarUsuarioPorId(id, usuario):
        try:
            conectar()
            mySql_insert_query = " UPDATE Usuarios SET  Apellido = " + usuario.Apellido + ", Nombre = " + usuario.Nombre + " , Email " + usuario.Email + ", Telefono " + usuario.Telefono + ", IdCliente " + usuario.IdCliente + ", IdEmprendedor " + usuario.IdEmprendedor + " WHERE Id=" + id           
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "registro(s) actualizado") 

        except mysql.connector.Error as error:
            print("Error al actualizar {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexion cerrada")

                


usuario1 = Usuario(0, "luna", "emanuel", "memonluna@gmail.com", "12344213", 0,0)
usuario1.guardarUsuario(usuario1)
usuario2 = Usuario(1, "lunasss", "emanuel", "memonluna@gmail.com", "12344213", 0,0)
usuario2.guardarUsuario(usuario2)
usuario1.obtenerUsuarios()
usuario1.obtenerUsuarioPorId(1)