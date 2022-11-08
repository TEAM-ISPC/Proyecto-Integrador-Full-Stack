from Usuario import *
from CategoriasTrabajo import *
from sqlService import sqlService

class Emprendedor(Usuario, CategoriasTrabajo):    

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono, IdEmprendedor, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspecialFinal, TiempoTurno, Descripcion, CategoriaTrabajoID, RedSocial1, RedSocial2, UsuarioId):
        super().__init__(IdUsuario, Apellido, Nombre, Email, Password, Telefono)
        self._IdEmprendedor = IdEmprendedor
        self._DiasTrabajar = DiasTrabajar
        self._HorarioDiaNormalInicio = HorarioDiaNormalInicio
        self._HorarioDiaNormalFinal = HorarioDiaNormalFinal
        self._HorarioDiaEspecialInicio = HorarioDiaEspecialInicio
        self._HorarioDiaEspecialFinal = HorarioDiaEspecialFinal
        self._TiempoTurno = TiempoTurno
        self._Descripcion = Descripcion
        self._CategoriaTrabajoID = CategoriaTrabajoID
        self._RedSocial1 = RedSocial1
        self._RedSocial2 = RedSocial2
        self._UsuarioId = UsuarioId                 

    @property            
    def IdEmprendedor(self): 
        return self._IdEmprendedor
    @IdEmprendedor.setter
    def IdEmprendedor(self, value):   
        self._IdEmprendedor = value

    @property            
    def DiasTrabajar(self): 
        return self._DiasTrabajar
    @DiasTrabajar.setter    
    def DiasTrabajar(self, value):
        self._DiasTrabajar = value
    
    @property            
    def HorarioDiaNormalInicio(self): 
        return self._HorarioDiaNormalInicio
    @HorarioDiaNormalInicio.setter    
    def HorarioDiaNormalInicio(self, value):   
        self._HorarioDiaNormalInicio = value
        
    @property            
    def HorarioDiaNormalFinal(self): 
        return self._HorarioDiaNormalFinal
    @HorarioDiaNormalFinal.setter    
    def HorarioDiaNormalFinal(self, value):   
        self._HorarioDiaNormalFinal = value

    @property            
    def HorarioDiaEspecialInicio(self): 
        return self._HorarioDiaEspecialInicio
    @HorarioDiaEspecialInicio.setter    
    def HorarioDiaEspecialInicio(self, value):   
        self._HorarioDiaEspecialInicio = value    

    @property            
    def HorarioDiaEspecialFinal(self): 
        return self._HorarioDiaEspecialFinal
    @HorarioDiaEspecialFinal.setter    
    def HorarioDiaEspecialFinal(self, value):   
        self._HorarioDiaEspecialFinal = value   

    @property            
    def TiempoTurno(self): 
        return self._TiempoTurno
    @TiempoTurno.setter    
    def TiempoTurno(self, value):   
        self._TiempoTurno = value       

    @property            
    def Descripcion(self): 
        return self._Descripcion
    @Descripcion.setter    
    def Descripcion(self, value):   
        self._Descripcion = value        

    @property            
    def CategoriaTrabajoID(self): 
        return self._CategoriaTrabajoID
    @CategoriaTrabajoID.setter    
    def CategoriaTrabajoID(self, value):   
        self._CategoriaTrabajoID = value     

    @property            
    def RedSocial1(self): 
        return self._RedSocial1
    @RedSocial1.setter    
    def RedSocial1(self, value):   
        self._RedSocial1 = value        

    @property            
    def RedSocial2(self): 
        return self._RedSocial2
    @RedSocial2.setter    
    def RedSocial2(self, value):   
        self._RedSocial2 = value    

    @property            
    def UsuarioId(self): 
        return self._UsuarioId
    @UsuarioId.setter    
    def UsuarioId(self, value):   
        self._UsuarioId = value    

    def guardarEmprendedor(self, emprendedor):
        Query = "INSERT INTO emprendedores (idEmprendedor, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspecialFinal, TiempoTurno, Descripcion, CategoriaTrabajoID, RedSocial1, RedSocial2, UsuarioId) VALUES (0, '"+ str(emprendedor.DiasTrabajar) + "', '"+ str(emprendedor.HorarioDiaNormalInicio) + "', '"+ str(emprendedor.HorarioDiaNormalFinal) + "', '"+ str(emprendedor.HorarioDiaEspecialInicio) + "', '"+ str(emprendedor.HorarioDiaEspecialFinal) + "', '"+ str(emprendedor.TiempoTurno) + "', '"+ emprendedor.Descripcion + "', '"+ str(emprendedor.CategoriaTrabajoID) + "', '"+ emprendedor.RedSocial1 + "', '"+ emprendedor.RedSocial2 + "', '"+ str(emprendedor.UsuarioId) + "' );"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó Emprendedor.", "Error al grabar Emprendedor {}")



usuario1 = Usuario(1, "Rios", "Agustin", "agustin@correo.com", "1234", "12344213")
categoria1 = CategoriasTrabajo(0, "peluqueria", "descripcion de categoria")
emprendedor1 = Emprendedor(usuario1.IdUsuario, usuario1.Apellido, usuario1.Nombre, usuario1.Email, usuario1.Password, usuario1.Telefono, 0, 5, 8, 16, 8, 12, 1, "descripcion", categoria1.IdCategorias , "Facebook.com/", "instagram.com/", usuario1.IdUsuario)
emprendedor1.guardarEmprendedor(emprendedor1)
# cliente1.obtenerClientePorId(8)
# cliente1.borrarClientePorId(8)
# cliente1 = Usuario(0, "lunatico", "emanuel", "memonlunagmail.com", "1234", "12344213")
# cliente1.actualizarClientePorId(10, cliente1)
# cliente1.obtenerListaClientes()
# print(cliente1.Direccion)

