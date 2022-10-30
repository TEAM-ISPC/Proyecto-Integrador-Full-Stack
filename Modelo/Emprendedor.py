"""
En este módulo definiriamos la clase Emprendedor, va a ser hija de Usuario.
Su función seria ser el modelo para implementar en la base de datos en la tabla Emprendedor.
Varios atributos de este módulo, lo utilizará un controlador para generar el turnero. 
Contará con los siguiente atributos:
    - IdEmprendedor.
    - DiasTrabajar.
    - HorarioDiaNormalInicio.
    - HorarioDiaNormalFinal.
    - HorarioDiaEspecialInicio.
    - HorarioDiaEspcialFinal.
    - TiempoTurno.
    - Descripcion.
    - CategoriaTrabajoID.
    - RedSocial1.
    - RedSocial2.

Definiríamos constructor, métodos getters(@property), setters(@xxx.setter) y toSting (__str__).
"""

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

