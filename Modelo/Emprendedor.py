from Usuario import *
from sqlService import sqlService

class Emprendedor(Usuario):    

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono, IdEmprendedor, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspcialFinal, TiempoTurno, Descripcion, CategoriaTrabajoID, RedSocial1, RedSocial2, UsuarioId):
        super().__init__(IdUsuario, Apellido, Nombre, Email, Password, Telefono)
        self._IdEmprendedor = IdEmprendedor
        self._DiasTrabajar = DiasTrabajar
        self._HorarioDiaNormalInicio = HorarioDiaNormalInicio
        self._HorarioDiaNormalFinal = HorarioDiaNormalFinal
        self._HorarioDiaEspecialInicio = HorarioDiaEspecialInicio
        self._HorarioDiaEspcialFinal = HorarioDiaEspcialFinal
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
        
