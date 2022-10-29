from Usuario import *
from sqlService import sqlService

class Cliente(Usuario):    

    def __init__(self, IDCliente, Direccion, Calificacion, PuntosAcumulados, UsuarioId):
        super().__init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono)
        self._IDCliente = IDCliente
        self._Direccion = Direccion
        self._Calificacion = Calificacion
        self._PuntosAcumulados = PuntosAcumulados
        self._UsuarioId = UsuarioId

    # Getters y Setters

    @property            
    def IDCliente(self): 
        return self._IDCliente
    @IDCliente.setter    
    def IDCliente(self, value):   
        self._IDCliente = value

    @property            
    def Direccion(self): 
        return self._Direccion
    @Direccion.setter    
    def Direccion(self, value):   
        self._Direccion = value 

    @property            
    def Calificacion(self): 
        return self._Calificacion
    @Calificacion.setter    
    def Calificacion(self, value):   
        self._Calificacion = value 
    
    @property            
    def PuntosAcumulados(self): 
        return self._PuntosAcumulados
    @PuntosAcumulados.setter    
    def PuntosAcumulados(self, value):   
        self._PuntosAcumulados = value

    @property            
    def UsuarioId(self): 
        return self._Email
    @UsuarioId.setter    
    def UsuarioId(self, value):   
        self._UsuarioId = value  

    def __str__(self):
       return str(self.IDCliente) + ' ' + self.Direccion + ' ' + str(self.Calificacion) + ' ' + str(self.PuntosAcumulados) + ' ' + str(self.UsuarioId)

    def guardarUsuario(self, Cliente):
        Query = "INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, '" + usuario.Apellido + "', '" + usuario.Nombre + "', '" + usuario.Email + "', '" + usuario.Password + "', '" + usuario.Telefono + "');"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó usuario.", "Error al grabar usuario {}")

    def obtenerUsuarioPorId(self, id):           
        Query = "select * from Usuarios where idUsuario =" + str(id)
        Usuario = sqlService.ejecutarSqlR1(self, Query, "Error al obtener usuario {}")
        print(Usuario)
        return Usuario

    def borrarUsuarioPorId(self, id):
        Query = "DELETE FROM Usuarios WHERE IdUsuario =" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró usuario.", "Error al borrar usuario {}")

    def actualizarUsuarioPorId(self, id, usuario):
        Query = "UPDATE Usuarios SET apellido='" + usuario.Apellido + "', nombre='" + usuario.Nombre + "' , email='" + usuario.Email + "', password='" + usuario.Password + "', telefono='" + usuario.Telefono + "' WHERE idUsuario = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó usuario.", "Error al borrar usuario {}")

    def obtenerListaUsuarios(self):
        Query = "select * from Usuarios"
        UsuarioLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener usuario {}")
        print(UsuarioLista)
        return UsuarioLista


usuario1 = Usuario(0, "luna", "emanuel", "memonlunagmail.com", "1234", "12344213")
# usuario1.guardarUsuario(usuario1)
# usuario1.obtenerUsuarioPorId(2)
# usuario1.borrarUsuarioPorId(2)
# usuario2 = Usuario(0, "lunatico", "emanuel", "memonlunagmail.com", "1234", "12344213")
# usuario1.actualizarUsuarioPorId(1, usuario2)
usuario1.obtenerListaUsuarios()