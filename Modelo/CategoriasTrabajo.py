from sqlService import sqlService

class CategoriasTrabajo():    

    def __init__(self, IdCategorias, Tipo, Descripcion):
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
    @Descripcion.setter    
    def Descripcion(self, value):   
        self._Descripcion = value    

    def guardarCategoria(self, categoria):
        Query = "INSERT INTO categoriastrabajo (idCategoria, Tipo, Descripcion) VALUES (0, '" + categoria.Tipo + "', '" + categoria.Descripcion + "');"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó categoria.", "Error al grabar categoria {}")

    def obtenerCategoriaPorId(self, id):           
        Query = "select * from categoriastrabajo where idCategoria =" + str(id)
        Categoria = sqlService.ejecutarSqlR1(self, Query, "Error al obtener la categoria {}")
        print(Categoria)
        return Categoria

    def borrarCategoriaPorId(self, id):
        Query = "DELETE FROM categoriastrabajo WHERE IdCategoria=" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró la categoria.", "Error al borrar la categoria {}")

    def actualizarClientePorId(self, id, cliente):
        Query = "UPDATE clientes SET direccion='" + cliente.Direccion + "', calificacion='" + str(cliente.Calificacion) + "' , puntosAcumulados='" + str(cliente.PuntosAcumulados) + "', usuarioId='" + str(cliente.UsuarioId) + "' WHERE idCliente = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó usuario.", "Error al borrar usuario {}")

    def obtenerListaClientes(self):
        Query = "select * from clientes"
        ClienteLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener cliente {}")
        print(ClienteLista)
        return ClienteLista


categoria1 = CategoriasTrabajo(0, "zapatero", "descripcion")
categoria1.guardarCategoria(categoria1)
# categoria1.obtenerCategoriaPorId(4)
# categoria1.borrarCategoriaPorId(2)
# cliente1 = Usuario(0, "lunatico", "emanuel", "memonlunagmail.com", "1234", "12344213")
# cliente1.actualizarClientePorId(10, cliente1)
# cliente1.obtenerListaClientes()
# print(cliente1.Direccion)
