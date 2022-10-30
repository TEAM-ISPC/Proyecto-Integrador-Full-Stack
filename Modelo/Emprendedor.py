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
    def HorarioDiaEspcialFinal(self): 
        return self._HorarioDiaEspcialFinal
    @HorarioDiaEspcialFinal.setter    
    def HorarioDiaEspcialFinal(self, value):   
        self._HorarioDiaEspcialFinal = value   

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