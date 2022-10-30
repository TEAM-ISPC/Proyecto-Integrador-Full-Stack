"""
En este módulo definiriamos la clase Turno.
Su función seria ser el modelo para implementar en la base de datos en la tabla Turnos.
Varios atributos de este módulo, lo utilizará un controlador para generar el turnero. 
Contará con los siguiente atributos:
    - IDTurno.
    - EmprendedorID.
    - Fecha.
    - HoraTurno.
    - ClienteID.
    - Trabajo.
    - Comentario.

    	IdTurnos	Fecha	HoraTurno	ClienteId	Trabajo	EmprendedorId	Comentario	

    
Definiríamos constructor, métodos getters(@property), setters(@xxx.setter) y toSting (__str__).
"""

from sqlService import sqlService

class Usuario():    

    def __init__(self, IdTurnos, Apellido, Nombre, Email, Password, Telefono):
        self._IdTurnos = IdTurnos
        self._Apellido = Apellido
        self._Nombre = Nombre
        self._Email = Email
        self._Password = Password
        self._Telefono = Telefono