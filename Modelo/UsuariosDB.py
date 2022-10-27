def conectar():
        connection = mysql.connector.connect(host='localhost:3308',
                                            database='turnow',
                                            user='root',
                                            password='')
        return connection                    

    def guardarUsuario(self, usuario):
        try:
            connection = mysql.connector.connect(host='localhost', database='turnow', user='root', password='')
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

    def obtenerUsuarioPorId(id):
        try:
            conectar()
            mySql_query = "select * from Usuarios where idUsuario =" + id
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