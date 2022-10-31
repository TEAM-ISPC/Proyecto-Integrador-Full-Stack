from sqlService import sqlService

class CategoriasTrabajo(Usuario):    

    def __init__(self, IdCategorias, Tipo, Descripcion):
        super().__init__()
        self._IdCategorias = IdCategorias
        self._Tipo = Tipo
        self._Descripcion = Descripcion

    @property            
    def IdCategorias(self): 
        return self._IdCategorias
    @IdCategorias.setter    
    def IdCategorias(self, value):   
        self._IdCategorias = value

        @property            
    def Tipo(self): 
        return self._Tipo
    @Tipo.setter    
    def Tipo(self, value):   
        self._Tipo = value

        @property            
    def Descripcion(self): 
        return self._Descripcion
    @IdTurnos.setter    
    def Descripcion(self, value):   
        self._Descripcion = value    
