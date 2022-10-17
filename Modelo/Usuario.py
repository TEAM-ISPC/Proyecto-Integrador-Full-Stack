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

