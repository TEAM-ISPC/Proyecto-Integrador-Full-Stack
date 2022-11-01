from sqlService import sqlService

class turnos():    

    def __init__(self, IdTurnos, Fecha, HoraTurno, ClienteId, Trabajo, EmprendedorId, Comentario):
        self._IdTurnos = IdTurnos
        self._Fecha = Fecha
        self._HoraTurno = HoraTurno
        self._ClienteId = ClienteId
        self._Trabajo = Trabajo
        self._EmprendedorId = EmprendedorId
        self._Comentario = Comentario

    @property            
    def IdTurnos(self): 
        return self._IdTurnos
    @IdTurnos.setter    
    def IdTurnos(self, value):   
        self._IdTurnos = value    

    @property            
    def Fecha(self): 
        return self._Fecha
    @Fecha.setter    
    def Fecha(self, value):   
        self._Fecha = value    
 
     @property            
    def HoraTurno(self): 
        return self._HoraTurno
    @HoraTurno.setter    
    def HoraTurno(self, value):   
        self._HoraTurno = value       

        @property            
    def ClienteId(self): 
        return self._ClienteId
    @ClienteId.setter    
    def ClienteId(self, value):   
        self._ClienteId = value      

    @property            
    def Trabajo(self): 
        return self._Trabajo
    @Trabajo.setter    
    def Trabajo(self, value):   
        self._Trabajo = value   

    @property            
    def EmprendedorId(self): 
        return self._EmprendedorId
    @EmprendedorId.setter    
    def EmprendedorId(self, value):   
        self._EmprendedorId = value             

    @property            
    def Comentario(self): 
        return self._Comentario
    @Comentario.setter    
    def Comentario(self, value):   
        self._Comentario = value   

        # aca agregar toString